import logging
import os
from urllib.parse import urljoin

import requests

TIMEOUT = 30


class TalendClient:
    def __init__(self):
        api_url = os.environ["API_URL"]
        self.access_token = os.environ["ACCESS_TOKEN"]
        self.base_url = urljoin(api_url, "processing")
        self.session = requests.Session()
        self.session.headers.update(
            {
                "Authorization": f"Bearer {self.access_token}",
                "Content-Type": "application/json",
            }
        )

    def _get(self, path):
        resp = self.session.get(
            f"{self.base_url}{path}",
            timeout=TIMEOUT,
        )
        resp.raise_for_status()
        return resp.json()

    def _post(self, path, payload):
        resp = self.session.post(
            f"{self.base_url}{path}",
            json=payload,
            timeout=TIMEOUT,
        )
        resp.raise_for_status()
        return resp.json()

    def get_jobs(self):
        """Gets job names and execution ids.

        Returns dict:
        {
            "Job_X": "exec_id_123",
            "Job_Y": "exec_id_456",
        }
        """
        result = self._get("/executables/tasks")
        return {item["name"]: item["executable"] for item in result["items"]}

    def get_job_id(self, job_name):
        jobs = self.get_jobs()
        if job_name not in jobs:
            raise ValueError(f"Talend job not found: {job_name}")
        return jobs[job_name]

    def run_job(self, job_name):
        """Starts a Talend job and returns execution_id."""
        executable_id = self.get_job_id(job_name)
        result = self._post(
            "/executions",
            {"executable": executable_id},
        )
        execution_id = result["executionId"]
        logging.info(
            "Started Talend job '%s' executionId=%s",
            job_name,
            execution_id,
        )
        return execution_id
