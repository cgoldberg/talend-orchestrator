# Talend Orchestrator

This is a lightweight orchestration service for triggering Talend Cloud jobs
using Azure Functions and a Python CLI. It provides scheduled execution via
Azure Functions timer triggers, manual execution via a CLI tool, and a
reusable Python client for interacting with the Talend API.

- Copyright (c) 2026 [Corey Goldberg](https://github.com/cgoldberg)

<table>
  <tr>
    <td>Development</td>
    <td>
      <a href="https://github.com/cgoldberg/talend-orchestrator">
        GitHub
      </a>
    </td>
  </tr>
  <tr>
    <td>License</td>
    <td>
      <a href="https://raw.githubusercontent.com/cgoldberg/talend-orchestrator/refs/heads/master/LICENSE">
        MIT
      </a>
    </td>
  </tr>
    <td>Supported Python Versions</td>
    <td>
      3.13+
    </td>
  </tr>
</table>


---

## Features

- Trigger Talend jobs by name
- Azure Functions timer-based scheduling
- CLI for manual execution and debugging
- API client for Talend Cloud

---

## Architecture

Azure Timer Trigger → function_app.py → TalendClient → Talend Cloud API

CLI → TalendClient → Talend Cloud API

---

## Project Structure

```
.
├── src/
│   └── talend_etl/
│       ├── __init__.py
│       ├── cli.py
│       └── talend_client.py
├── function_app.py
├── pyproject.toml
└── requirements.txt
```

---

## Configuration

Environment variables (or `.env` file for CLI):

```
ACCESS_TOKEN=your_talend_api_token
API_URL=https://api.us-west.cloud.talend.com
```

---

## CLI Usage

Install:

```
pip install -e .
```

Run a job:

```
talend_cli --job Job_X
```

---

## Azure Functions (Scheduled Jobs)

Schedules use CRON expressions in UTC:

```
@app.timer_trigger(schedule="0 0 1 * * *")
def job_x(_):
    run("Job_X")
```
