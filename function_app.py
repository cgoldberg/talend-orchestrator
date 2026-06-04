import logging

from talend_client import TalendClient

client = TalendClient()


def run(job_name):
    try:
        logging.info("Triggering job: %s", job_name)
        client.run_job(job_name)
    except Exception:
        logging.exception("Job failed: %s", job_name)
        raise


@app.timer_trigger(schedule="0 0 1 * * *")
def job_x(timer):
    run("Job_X")


@app.timer_trigger(schedule="0 30 1 * * *")
def job_y(timer):
    run("Job_Y")
