# AWS implementation of backend.py

# todo: move EFS mounting into userdata for things to happen in parallel
# TODO: fix remote_fn must be absolute for uploading with check_with_existing
import os
import shlex
import signal
import sys
import threading
import time
from typing import Union

from . import backend
from . import aws_util as u
from . import util
from . import aws_create_resources as create_lib

TMPDIR = '/tmp/ncluster'  # location for temp files on launching machine
AWS_LOCK_FN = '/tmp/aws.lock'  # lock file used to prevent concurrent creation of AWS resources by multiple workers in parallel
NCLUSTER_DEFAULT_REGION = 'us-east-1'  # used as last resort if no other method set a region
LOGDIR_ROOT = '/ncluster/runs'


def get_logdir_root():
  return LOGDIR_ROOT


def set_global_logdir_root(logdir_root):
  """Globally changes logdir root for all runs."""
  global LOGDIR_ROOT
  LOGDIR_ROOT = logdir_root


class Task(backend.Task):
  """AWS task is initialized with an AWS instance and handles initialization,
  creation of SSH session, shutdown"""

  def __init__(self, name, instance, *, install_script='', image_name='',
               job=None,
               **extra_kwargs):

    self._can_run = False  # indicates that things needed for .run were created
    self.initialize_called = False

    self.name = name
    self.instance = instance
    self.install_script = install_script
    self.job = job
    self.extra_kwargs = extra_kwargs

    self.public_ip = u.get_public_ip(instance)
    self.ip = u.get_ip(instance)
    self._linux_type = 'ubuntu'

    # heuristic to tell if I'm using Amazon image name
    # default image has name like 'amzn2-ami-hvm-2.0.20180622.1-x86_64-gp2'
    if 'amzn' in image_name.lower() or 'amazon' in image_name.lower():
      self._log('Detected Amazon Linux image')
      self._linux_type = 'amazon'
    self.run_counter = 0

    launch_id = util.random_id()
    self.local_scratch = f"{TMPDIR}/{name}-{launch_id}"
    self.remote_scratch = f"{TMPDIR}/{name}-{launch_id}"

    os.system('mkdir -p ' + self.local_scratch)

    self._initialized_fn = f'{TMPDIR}/{self.name}.initialized'

    # _current_directory tracks current directory on task machine
    # used for uploading without specifying absolute path on target machine
    if self._linux_type == 'ubuntu':
      #      self._current_directory = '/home/ubuntu'
      self.ssh_username = 'ubuntu'  # default username on task machine
    elif self._linux_type == 'amazon':
      #      self._current_directory = '/home/ec2-user'
      self.ssh_username = 'ec2-user'

    self.ssh_client = u.ssh_to_task(self)
    self._setup_tmux()
    self._run_raw('mkdir -p ' + self.remote_scratch)
    self._mount_efs()

    if self._is_initialized_fn_present():
      self._log("reusing previous initialized state")
    else:
      self._log("running install script")

      # bin/bash needed to make self-executable or use with UserData
      self.install_script = '#!/bin/bash\n' + self.install_script
      self.install_script += f'\necho ok > {self._initialized_fn}\n'
      self.file_write('install.sh', util.shell_add_echo(self.install_script))
      self.run('bash -e install.sh')  # fail on errors
      # TODO(y): propagate error messages printed on console to the user
      # right now had to log into tmux to see them
      assert self._is_initialized_fn_present()

    self.connect_instructions = f"""
ssh -i {u.get_keypair_fn()} -o StrictHostKeyChecking=no {self.ssh_username}@{self.public_ip}
tmux a
""".strip()
    self._log("Initialize complete")
    self._log(self.connect_instructions)

  # todo: replace with file_read
  def _is_initialized_fn_present(self):
    self._log("Checking for initialization status")
    try:
      return 'ok' in self.file_read(self._initialized_fn)
    except Exception:
      return False

  def _setup_tmux(self):
    self._log("Setting up tmux")

    self._tmux_window = f"{self.name}-main:0".replace('.', '=')
    tmux_session = self._tmux_window[:-2]

    tmux_cmd = [f'tmux set-option -g history-limit 50000 \; ',
                f'set-option -g mouse on \; ',
                f'new-session -s {tmux_session} -n 0 -d']

    # hack to get around Amazon linux not having tmux
    if self._linux_type == 'amazon':
      self._run_raw('sudo yum install tmux -y')
      del tmux_cmd[1]  # Amazon tmux is really old, no mouse option

    self._run_raw(f'tmux kill-session -t {tmux_session}')
    self._run_raw(''.join(tmux_cmd))

    self._can_run = True

  def _mount_efs(self):
    self._log("Mounting EFS")
    region = u.get_region()
    efs_id = u.get_efs_dict()[u.get_prefix()]
    dns = f"{efs_id}.efs.{region}.amazonaws.com"
    self.run('sudo mkdir -p /ncluster')

    # ignore error on remount (efs already mounted)
    self.run(
      f"sudo mount -t nfs -o nfsvers=4.1,rsize=1048576,wsize=1048576,hard,timeo=600,retrans=2 {dns}:/ /ncluster",
      ignore_errors=True)
    self.run('sudo chmod 777 /ncluster')

    # Hack below may no longer be needed
    # # make sure chmod is successful, hack to fix occasional permission errors
    # while 'drwxrwxrwx' not in self.run_and_capture_output('ls -ld /ncluster'):
    #   print(f"chmod 777 /ncluster didn't take, retrying in {TIMEOUT_SEC}")
    #   time.sleep(TIMEOUT_SEC)
    #   self.run('sudo chmod 777 /ncluster')

  def join(self):
    while not self._is_initialized_fn_present():
      self._log(
        f"wait_until_ready: Not initialized, retrying in {u.RETRY_INTERVAL_SEC}")
      time.sleep(u.RETRY_INTERVAL_SEC)

  # TODO: also chmod the file so that 755 files remain 755
  def upload(self, local_fn, remote_fn='', dont_overwrite=False):
    """Uploads file to remote instance. If location not specified, dumps it
    into default directory."""

    self._log('uploading ' + local_fn + ' to ' + remote_fn)
    sftp = self.ssh_client.open_sftp()

    if not remote_fn:
      remote_fn = os.path.basename(local_fn)
    if dont_overwrite and self.file_exists(remote_fn):
      self._log("Remote file %s exists, skipping" % (remote_fn,))
      return

    if os.path.isdir(local_fn):
      u._put_dir(sftp, local_fn, remote_fn)
    else:
      assert os.path.isfile(local_fn), "%s is not a file" % (local_fn,)
      sftp.put(local_fn, remote_fn)

  def download(self, remote_fn, local_fn=''):
    self._log("downloading %s" % remote_fn)
    sftp = self.ssh_client.open_sftp()
    if not local_fn:
      local_fn = os.path.basename(remote_fn)
      self._log("downloading %s to %s" % (remote_fn, local_fn))
    sftp.get(remote_fn, local_fn)

  def file_exists(self, remote_fn):
    stdout, stderr = self._run_raw('stat ' + remote_fn)
    return 'No such file' not in stdout

  def file_write(self, remote_fn, contents):
    tmp_fn = self.local_scratch + '/' + str(util.now_micros())
    open(tmp_fn, 'w').write(contents)
    self.upload(tmp_fn, remote_fn)

  def file_read(self, remote_fn):
    tmp_fn = self.local_scratch + '/' + str(util.now_micros())
    self.download(remote_fn, tmp_fn)
    return open(tmp_fn).read()

  def run(self, cmd, async=False, ignore_errors=False,
          max_wait_sec=365 * 24 * 3600,
          check_interval=0.5) -> int:

    self.run_counter += 1
    cmd = cmd.strip()
    if cmd.startswith('#'):  # ignore empty/commented out lines
      return -1
    self._log("tmux> %s", cmd)

    cmd_fn = f'{self.remote_scratch}/{self.run_counter}.cmd'
    status_fn = f'{self.remote_scratch}/{self.run_counter}.status'

    cmd = util.shell_strip_comment(cmd)
    assert '&' not in cmd, f"cmd {cmd} contains &, that breaks things"

    # modify command to dump shell success status into file
    self.file_write(cmd_fn, cmd + '\n')
    modified_cmd = f'{cmd}; echo $? > {status_fn}'
    modified_cmd = shlex.quote(modified_cmd)

    tmux_cmd = f"tmux send-keys -t {self._tmux_window} {modified_cmd} Enter"
    self._run_raw(tmux_cmd)
    if async:
      return 0

    self.wait_for_file(status_fn)
    contents = self.file_read(status_fn)

    # if empty wait a bit to allow for race condition
    if len(contents) == 0:
      time.sleep(check_interval)
      contents = self.file_read(status_fn)
    status = int(contents.strip())

    if status != 0:
      if not ignore_errors:
        raise RuntimeError(f"Command {cmd} returned status {status}")
      else:
        self._log(f"Warning: command {cmd} returned status {status}")

    return status

  def _run_raw(self, cmd):
    """Runs given cmd in the task using current SSH session, returns
    stdout/stderr as strings. Because it blocks until cmd is done, use it for
    short cmds. Silently ignores failing commands.

    This is a barebones method to be used during initialization that have
    minimal dependencies (no tmux)
    """
    #    self._log("run_ssh: %s"%(cmd,))

    # TODO(y), transition to SSHClient and assert fail on bad error codes
    # https://stackoverflow.com/questions/3562403/how-can-you-get-the-ssh-return-code-using-paramiko
    stdin, stdout, stderr = self.ssh_client.exec_command(cmd, get_pty=True)
    stdout_str = stdout.read().decode()
    stderr_str = stderr.read().decode()
    # TODO: use shell return status to see if it failed
    if 'command not found' in stdout_str or 'command not found' in stderr_str:
      self._log(f"command ({cmd}) failed with ({stdout_str}), ({stderr_str})")
      assert False, "run_ssh command failed"
    return stdout_str, stderr_str


# TODO: remove?
class Job(backend.Job):
  pass


def maybe_start_instance(instance):
  """Starts instance if it's stopped, no-op otherwise."""

  if not instance:
    return

  if instance.state['Name'] == 'stopped':
    instance.start()
    while True:
      print(
        "Waiting  forever for instances to start. TODO: replace with proper wait loop")
      time.sleep(10)


# TODO: call tasks without names "unnamed-123123"
def maybe_create_resources():
  """Use heuristics to decide to possibly create resources"""

  def should_create_resources():
    """Check if gateway, keypair, vpc exist."""
    prefix = u.get_prefix()
    if u.get_keypair_name() not in u.get_keypair_dict():
      print(f"Missing {u.get_keypair_name()} keypair, creating resources")
      return True
    vpcs = u.get_vpc_dict()
    if prefix not in vpcs:
      print(f"Missing {prefix} vpc, creating resources")
      return True
    vpc = vpcs[prefix]
    gateways = u.get_gateway_dict(vpc)
    if prefix not in gateways:
      print(f"Missing {prefix} gateway, creating resources")
      return True
    return False

  if not should_create_resources():
    util.log("Resources already created, no-op")
    return

  if os.path.exists(AWS_LOCK_FN):
    pid, ts = open(AWS_LOCK_FN).read().split('-')
    pid = int(pid)
    ts = int(ts)
    util.log(f"Skipping aws resource creation, another resource initiation was "
             f"initiated {int(time.time()-ts)} seconds ago by "
             f"{'this process' if pid==os.getpid() else pid}, delete lock file "
             f"{AWS_LOCK_FN} if this is an error")
    return

  with open(AWS_LOCK_FN, 'w') as f:
    f.write(f'{os.getpid()}-{int(time.time())}')
  create_lib.create_resources()
  os.remove(AWS_LOCK_FN)


def set_aws_environment():
  """Sets current zone/region environment variables.  """
  current_zone = os.environ.get('NCLUSTER_ZONE', '')
  current_region = os.environ.get('AWS_DEFAULT_REGION', '')

  if current_region and current_zone:
    assert current_zone.startswith(current_region)
    assert u.get_session().region_name == current_region  # setting from ~/.aws

  # zone is set, set region from zone
  if current_zone and not current_region:
    current_region = current_zone[:-1]
    os.environ['AWS_DEFAULT_REGION'] = current_region

  # neither zone nor region not set, use default setting for region
  # if default is not set, use NCLUSTER_DEFAULT_REGION
  if not current_region:
    current_region = u.get_session().region_name
    if not current_region:
      util.log(f"No default region available, using {NCLUSTER_DEFAULT_REGION}")
      current_region = NCLUSTER_DEFAULT_REGION
    os.environ['AWS_DEFAULT_REGION'] = current_region

  # zone not set, use first zone of the region
  if not current_zone:
    current_zone = current_region + 'a'
    os.environ['NCLUSTER_ZONE'] = current_zone

  util.log(f"Using account {u.get_account_number()}, zone {current_zone}")


def make_task(
        name: str = '',
        run_name: str = '',
        install_script: str = '',
        instance_type: str = '',
        image_name: str = '',
        preemptible: Union[None, bool] = None,
) -> Task:
  """
  Create task on AWS

  Args:
    name: see ncluster.make_task
    run_name: see ncluster.make_task
    install_script: see ncluster.make_task
    instance_type: instance type to use, ie t3.micro, defaults to $NCLUSTER_INSTANCE
    image_name: name of image, ie, "Deep Learning AMI (Ubuntu) Version 12.0", defaults to $NCLUSTER_IMAGE
    preemptible: use cheaper preemptible/spot instances

  Returns:

  """
  set_aws_environment()
  maybe_create_resources()

  # if name not specified, use name which is the same across script invocations
  if not name:
    main_script = os.path.abspath(sys.argv[0])
    script_id = util.alphanumeric_hash(main_script+instance_type+image_name)
    name = f"unnamed-{script_id}"

  if not run_name:
    run_name = f'default-{name}'

  if not image_name:
    image_name = os.environ.get('NCLUSTER_IMAGE',
                                'amzn2-ami-hvm-2.0.20180622.1-x86_64-gp2')
    util.log("Using image ", image_name)

  if preemptible is None:
    preemptible = os.environ.get('NCLUSTER_PREEMPTIBLE', False)
    preemptible = bool(preemptible)
    if preemptible:
      util.log("Using preemptible instances")

  if not instance_type:
    instance_type = os.environ.get('NCLUSTER_INSTANCE', 't3.micro')
    util.log("Using instance ", instance_type)

  image = u.lookup_image(image_name)
  keypair = u.get_keypair()
  security_group = u.get_security_group()
  subnet = u.get_subnet()
  ec2 = u.get_ec2_resource()

  instance = u.lookup_instance(name, instance_type,
                               image_name)  # todo: also add kwargs
  maybe_start_instance(instance)

  # create the instance if not present
  if not instance:
    util.log(f"Allocating {instance_type} for task {name}")
    args = {'ImageId': image.id,
            'InstanceType': instance_type,
            'MinCount': 1,
            'MaxCount': 1,
            'KeyName': keypair.name}

    args['TagSpecifications'] = [{
      'ResourceType': 'instance',
      'Tags': [{
        'Key': 'Name',
        'Value': name
      }]
    }]
    args['NetworkInterfaces'] = [{'SubnetId': subnet.id,
                                  'DeviceIndex': 0,
                                  'AssociatePublicIpAddress': True,
                                  'Groups': [security_group.id]}]
    placement_specs = {'AvailabilityZone': u.get_zone()}

    # if placement_group: placement_specs['GroupName'] = placement_group
    args['Placement'] = placement_specs
    args['Monitoring'] = {'Enabled': True}

    # Use high throughput disk (0.065/iops-month = about $1/hour)
    if 'NCLUSTER_AWS_FAST_ROOTDISK' in os.environ:
      ebs = {
        'VolumeSize': 500,
        'VolumeType': 'io1',
        'Iops': 11500
      }

      args['BlockDeviceMappings'] = [{
        'DeviceName': '/dev/sda1',
        'Ebs': ebs
      }]

    instances = []
    try:
      instances = ec2.create_instances(**args)
    except Exception as e:
      util.log(f"Instance creation for {name} failed with ({e})")
      util.log(
        "You can change availability zone using export NCLUSTER_ZONE=...")
      util.log("Terminating")
      os.kill(os.getpid(), signal.SIGINT)  # sys.exit() doesn't inside thread

    assert instances, f"ec2.create_instances returned {instances}"
    util.log(f"Allocated {len(instances)} instances")
    instance = instances[0]

  dummy_run = backend.Run(run_name)
  dummy_job = dummy_run.make_job()
  task = Task(name, instance,  # propagate optional args
              install_script=install_script,
              image_name=image_name,
              instance_type=instance_type)
  dummy_job.tasks.append(task)
  return task


def make_job(
        name: str = '',
        run_name: str = '',
        num_tasks: int = 0,
        install_script: str = '',
        instance_type: str = '',
        image_name: str = '',
        **kwargs) -> Job:
  """
  Args:
    name: see backend.make_task
    run_name: see backend.make_task
    num_tasks: number of tasks to launch
    install_script: see make_task
    instance_type: see make_task
    image_name: see make_task

  Returns:

  """
  assert num_tasks > 0, f"Can't create job with {num_tasks} tasks"

  assert name.count(
    '.') <= 1, "Job name has too many .'s (see ncluster design: Run/Job/Task hierarchy for  convention)"

  set_aws_environment()
  maybe_create_resources()

  # make tasks in parallel
  exceptions = []
  tasks = [backend.Task()] * num_tasks  # dummy tasks to appease type-checker

  def make_task_fn(i: int):
    try:
      tasks[i] = make_task(f"{i}.{name}", run_name=run_name,
                           install_script=install_script,
                           instance_type=instance_type, image_name=image_name,
                           **kwargs)
    except Exception as e:
      exceptions.append(e)

  util.log("Creating threads")
  threads = [threading.Thread(name=f'make_task_{i}',
                              target=make_task_fn, args=[i])
             for i in range(num_tasks)]
  for thread in threads:
    thread.start()
  for thread in threads:
    thread.join()
  print("Exception are ", exceptions)
  if exceptions:
    raise exceptions[0]

  dummy_run = backend.Run(run_name)
  job = Job(name, dummy_run, tasks, **kwargs)
  dummy_run.jobs.append(job)
  return job

# def make_run(name, **kwargs):
#  return Run(name, **kwargs)
