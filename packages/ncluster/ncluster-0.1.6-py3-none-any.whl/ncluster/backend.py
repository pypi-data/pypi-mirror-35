"""Interface for job launching backend."""
# Job launcher Python API: https://docs.google.com/document/d/1yTkb4IPJXOUaEWksQPCH7q0sjqHgBf3f70cWzfoFboc/edit
# AWS job launcher (concepts): https://docs.google.com/document/d/1IbVn8_ckfVO3Z9gIiE0b9K3UrBRRiO9HYZvXSkPXGuw/edit
import threading
import time
from typing import List, Tuple, Any

from . import util

# aws_backend.py
# local_backend.py

LOGDIR_ROOT: str = None  # location of logdir for this backend


def get_logdir_root():
  raise NotImplementedError()  # this must be implemented in concrete backends


def set_global_logdir_root(logdir_root):
  """Globally changes logdir root for all runs."""
  raise NotImplementedError()  # this must be implemented in concrete backends
  global LOGDIR_ROOT
  LOGDIR_ROOT = logdir_root


"""
backend = aws_backend # alternatively, backend=tmux_backend to launch jobs locally in separate tmux sessions
run = backend.make_run("helloworld")  # sets up /efs/runs/helloworld
worker_job = run.make_job("worker", instance_type="g3.4xlarge", num_tasks=4, ami=ami, setup_script=setup_script)
ps_job = run.make_job("ps", instance_type="c5.xlarge", num_tasks=4, ami=ami, setup_script=setup_script)
setup_tf_config(worker_job, ps_job)
ps_job.run("python cifar10_main.py --num_gpus=0")  # runs command on each task
worker_job.run("python cifar10_main.py --num_gpus=4")

tb_job = run.make_job("tb", instance_type="m4.xlarge", num_tasks=1, public_port=6006)
tb_job.run("tensorboard --logdir=%s --port=%d" %(run.logdir, 6006))
# when job has one task, job.task[0].ip can be accessed as job.ip
print("See TensorBoard progress on %s:%d" %(tb_job.ip, 6006))
print("To interact with workers: %s" %(worker_job.connect_instructions))


To reconnect to existing job:

"""


def _current_timestamp() -> str:
  # timestamp format from https://github.com/tensorflow/tensorflow/blob/155b45698a40a12d4fef4701275ecce07c3bb01a/tensorflow/core/platform/default/logging.cc#L80
  current_seconds = time.time()
  remainder_micros = int(1e6 * (current_seconds - int(current_seconds)))
  time_str = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(current_seconds))
  full_time_str = "%s.%06d" % (time_str, remainder_micros)
  return full_time_str


class Task:
  name: str
  ip: str
  public_ip: str
  run_counter: int
  # location where temporary files from interfacing with task go locally
  local_scratch: str
  # location where temporary files from interfacing with task go on task
  remote_scratch: str
  job: Any  # can't declare Job because of circular dependency

  def __init__(self):
    self.name = None
    self.instance = None
    self.install_script = None
    self.job = None
    self.kwargs = None
    self.public_ip = None
    self.ip = None
    self.logdir_ = None

  @property
  def logdir(self):
    self.setup_logdir()  # creates logdir if necessary, stores it in associated run_.logdir_
    return self.job.run_.logdir_

  @property
  def run_name(self):
    return self.job.run_.name

  def is_chief(self):
    return self.job.tasks.index(self) == 0 and self.job.is_chief()

  def setup_logdir(self):
    """Create logdir for task/job/run. No-op if the task is not chief (0'th task of 0'th job of run)
    """
    if not self.is_chief():
      return
    if self.job.run_.logdir_:
      return  # already created logdir

    self._log("Creating logdir")

    # logdir root can differ between backends, hence get it from the actual backend being used
    logdir_root = self.get_logdir_root()

    self.run(f'mkdir -p {logdir_root}')
    find_command = f'find {logdir_root} -maxdepth 1 -type d'

    stdout, stderr = self.run_with_output(find_command)
    logdir = f"{logdir_root}/{self.run_name}"

    # TODO, simplify this logic, just get the largest logdir encountered, then do +1
    counter = 0
    while logdir in stdout:
      counter += 1
      lll = f'{logdir_root}/{self.run_name}.{counter:02d}'
      self._log(f'Warning, logdir {logdir} exists, deduping to {lll}')
      logdir = lll
    self.run(f'mkdir -p {logdir}')
    self.job.run_.logdir_ = logdir

  def run(self, cmd: str, async=False, ignore_errors=False):
    """Runs command on given task."""
    raise NotImplementedError()

  def run_with_output(self, cmd, async=False, ignore_errors=False) -> Tuple[
    str, str]:
    """

    Args:
      cmd: single line shell command to run
      async (bool): if True, does not wait for command to finish
      ignore_errors: if True, will succeed even if command failed

    Returns:
      Contents of stdout/stderr as strings.
    Raises
      RuntimeException: if command produced non-0 returncode

    """

    assert '\n' not in cmd, "Do not support multi-line commands"
    cmd: str = cmd.strip()
    if not cmd or cmd.startswith('#'):  # ignore empty/commented out lines
      return '', ''

    stdout_fn = f"{self.remote_scratch}/{self.run_counter+1}.stdout"
    stderr_fn = f"{self.remote_scratch}/{self.run_counter+1}.stderr"
    cmd2 = f"{cmd} > {stdout_fn} 2> {stderr_fn}"

    assert not async, "Getting output doesn't work with async"
    status = self.run(cmd2, False, ignore_errors=True)
    stdout = self.file_read(stdout_fn)
    stderr = self.file_read(stderr_fn)

    if status > 0:
      self._log(f"Warning: command '{cmd}' returned {status},"
                f" stdout was '{stdout}' stderr was '{stderr}'")
      if not ignore_errors:
        raise RuntimeError(f"Warning: command '{cmd}' returned {status},"
                           f" stdout was '{stdout}' stderr was '{stderr}'")

    return stdout, stderr

  def wait_for_file(self, fn, max_wait_sec=3600*24*365, check_interval=0.02):
    print("Waiting for file", fn)
    start_time = time.time()
    while True:
      if time.time() - start_time > max_wait_sec:
        assert False, f"Timeout exceeded ({max_wait_sec} sec) for {fn}"
      if not self.file_exists(fn):
        time.sleep(check_interval)
        continue
      else:
        break

  def _run_raw(self, cmd):
    """Runs command directly on every task in the job, skipping tmux interface. Use if want to create/manage additional tmux sessions manually."""
    raise NotImplementedError()

  def upload(self, local_fn: str, remote_fn: str='', dont_overwrite: bool=False):
    """Uploads given file to the task. If remote_fn is not specified, dumps it
    into task current directory with the same name.

    Args:
      local_fn: location of file locally
      remote_fn: location of file on task
      dont_overwrite: if True, will be no-op if target file exists
      """
    raise NotImplementedError()

  def download(self, remote_fn: str, local_fn: str=''):
    """Downloads remote file to current directory."""
    raise NotImplementedError()

  def file_write(self, fn, contents):
    """Write string contents to file fn in task."""
    raise NotImplementedError()

  def file_read(self, fn):
    """Read contents of file and return it as string."""
    raise NotImplementedError()

  def file_exists(self, fn):
    """Return true if file exists in task current directory."""
    raise NotImplementedError()

  def _log(self, message, *args):
    """Log to launcher console."""
    if args:
      message %= args

    print(f"{_current_timestamp()} {self.name}: {message}")


class Job:
  name: str
  tasks: List[Task]

  #  run_: Run

  def __init__(self, name: str, run, tasks: List[Task] = None, **kwargs):
    if tasks is None:
      tasks = []
    self.name = name
    self.run_ = run
    self.tasks = tasks
    self.kwargs = kwargs
    # TODO: maybe backlinking is not needed
    for task in tasks:
      task.job = self

  @property
  def logdir(self):
    return self.tasks[0].logdir

  def is_chief(self):
    """Return true if this task is first task in the Run"""
    return self.run_.jobs.index(self) == 0

  def _async_wrapper(self, method, *args, **kwargs):
    """Runs given method on every task in the job. Blocks until all tasks finish. Propagates exception from first
    failed task."""

    exceptions = []

    def task_run(task):
      try:
        getattr(task, method)(*args, **kwargs)
      except Exception as e:
        exceptions.append(e)

    threads = [threading.Thread(name=f'task_{method}_{i}',
                                target=task_run, args=[t])
               for i, t in enumerate(self.tasks)]
    for thread in threads:
      thread.start()
    for thread in threads:
      thread.join()
    if exceptions:
      raise exceptions[0]

  def run(self, *args, **kwargs):
    """Runs command on every task in the job in parallel, blocks until all tasks finish.
    See Task for documentation of args/kwargs."""
    return self._async_wrapper("run", *args, **kwargs)

  def run_with_output(self, *args, **kwargs):
    """Runs command on every task in the job in parallel, blocks until all tasks finish.
    See Task for documentation of args/kwargs."""
    return self._async_wrapper("run_with_output", *args, **kwargs)

  def upload(self, *args, **kwargs):
    return self._async_wrapper("upload", *args, **kwargs)

  def file_write(self, *args, **kwargs):
    return self._async_wrapper("file_write", *args, **kwargs)

  def _run_raw(self, *args, **kwargs):
    return self._async_wrapper("_run_raw", *args, **kwargs)


class Run:
  """Run is a collection of jobs that share state. IE, training run will contain gradient worker job, parameter
  server job, and TensorBoard visualizer job. These jobs will use the same shared directory to store checkpoints and
  event files. """
  jobs: List[Job]

  def __init__(self, name='', jobs=None, **kwargs):
    """Creates a run. If install_script is specified, it's used as default
    install_script for all jobs (can be overridden by Job constructor)"""

    if not name:
      name = f'unnamed.{name}.{util.now_micros()}'

    if jobs is None:
      jobs = []
    self.name = name
    self.jobs = jobs
    self.kwargs = kwargs

    self.logdir_ = None

    # TODO: this back-linking logic may be unneeded
    for job in jobs:
      job.run_ = self

  @property
  def logdir(self):
    assert self.jobs
    return self.jobs[0].logdir

  def make_job(self, name='', **kwargs):
    return Job(name, self, **kwargs)

  # TODO: currently this is synchronous, use async wrapper like in Job to parallelize methods
  def run(self, *args, **kwargs):
    """Runs command on every job in the run."""

    for job in self.jobs:
      job.run(*args, **kwargs)

  def run_with_output(self, *args, **kwargs):
    """Runs command on every first job in the run, returns stdout."""
    for job in self.jobs:
      job.run_with_output(*args, **kwargs)

  def _run_raw(self, *args, **kwargs):
    """_run_raw on every job in the run."""

    for job in self.jobs:
      job._run_raw(*args, **kwargs)

  def upload(self, *args, **kwargs):
    """Runs command on every job in the run."""
    for job in self.jobs:
      job.upload(*args, **kwargs)

  # def log(self, message, *args):
  #   """Log to client console."""
  #   ts = _current_timestamp()
  #   if args:
  #     message = message % args
  #
  #   print("%s %s: %s" % (ts, self.name, message))


def make_task(**kwargs) -> Task:
  raise NotImplementedError()


def make_job(**kwargs) -> Job:
  raise NotImplementedError()


def make_run(**kwargs) -> Run:
  raise NotImplementedError()
