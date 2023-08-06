# -*- coding: utf-8 -*-

"""Top-level package for jobWrapper."""

__author__ = """Antoine Tavant"""
__email__ = 'antoinetavant@hotmail.fr'
__version__ = '0.1'
name = "jobwrapper"

from .inputclass import inputparams
from .inspect_exec import is_debug
from .job_watcher import JobState, is_memo_created, last_file_created, get_errfile_notempty
from .mail import sendmail
from .preporc import test_expected, main as preproc, get_hostname
from .readTemp import main as readTemp
from .run_sbatch import main as runSbatch
from .slurm_wrapper import launch_job, return_status, kill_job, exist_job
