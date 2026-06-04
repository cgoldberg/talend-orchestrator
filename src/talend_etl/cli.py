#!/usr/bin/env python3

import logging
import argparse

from dotenv import load_dotenv

from talend_etl.talend_client import TalendClient

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--job",
        help="job name",
        required=True,
    )
    args = parser.parse_args()
    logging.info("Starting Talend CLI job")
    load_dotenv()
    client = TalendClient()
    client.run_job(args.job)


if __name__ == "__main__":
    main()
