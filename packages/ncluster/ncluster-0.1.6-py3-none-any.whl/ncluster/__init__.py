import os

from . import aws_backend
from . import aws_util
from . import local_backend
from . import backend  # TODO: remove?

from .ncluster import get_backend
from .ncluster import set_backend

from .ncluster import make_task
from .ncluster import make_job
from .ncluster import make_run
from .ncluster import get_zone
from .ncluster import set_global_logdir_root
from .ncluster import get_logdir_root


# set default backend from environment
if 'NCLUSTER_BACKEND' in os.environ:
  set_backend(os.environ['NCLUSTER_BACKEND'])
else:
  set_backend('local')
