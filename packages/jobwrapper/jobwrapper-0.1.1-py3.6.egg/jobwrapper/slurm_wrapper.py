import subprocess as sbp
import time


def launch_job():
    jobID = sbp.check_output(["sbatch", "--parsable", "LPPic2D"])
    jobID = jobID.decode('ascii')[:-1]  # the output is a byte string with "\n" at the end
    print("Job launched with number : ", jobID)

    return jobID


def return_status(jobId):
    data = sbp.check_output(["sacct", '-j', str(jobId), "-n", "-o", 'state']).decode('ascii')
    lines = data.splitlines()

    if len(lines) < 1:
        print("job not found")
        print(jobId)
        print(lines)
        return -1

    jobstatus = lines[0].split()[0]  # the status is on the 3rd line !
    print("the statis is: ", jobstatus)

    return jobstatus


def exist_job(jobID):
    """check if a job existe in the slurm queue"""
    data = sbp.check_output(["sacct", "-j", jobID, "-n", "-o", 'state'])
    data = data.decode('ascii')
    lines = data.splitlines()

    if len(lines) < 1:
        return False

    jobstatus = return_status(jobID)
    if jobstatus == "PENDING" or jobstatus == "RUNNING":
        return True

    return False


def kill_job(jobID):
    """kill a job"""
    print("~~~~~~~~~~~~~~~~~")
    if exist_job(jobID):
        print("Killing the job ")
        sbp.call(["scancel", jobID])
    else:
        print(f"the Job id={jobID} do not exist, we cannot kill it")

    time.sleep(1)
