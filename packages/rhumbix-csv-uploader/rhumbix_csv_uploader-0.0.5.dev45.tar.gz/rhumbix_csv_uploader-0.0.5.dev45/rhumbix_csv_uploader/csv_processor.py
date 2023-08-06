import argparse
import json
import glob
import logging
import time
import os
from os.path import dirname, abspath
import rhumbix_csv_uploader.employee_processor as employee_processor
import rhumbix_csv_uploader.project_processor as project_processor
import rhumbix_csv_uploader.cost_code_processor as cost_code_processor
import rhumbix_csv_uploader.budget_processor as budget_processor
from rhumbix_csv_uploader.processor_utils import update_url_config


employee_filename_pattern = "rhumbix_employee*.csv"
project_filename_pattern = "rhumbix_project*.csv"
cost_code_filename_pattern = "rhumbix_cost_code*.csv"
budget_filename_pattern = "rhumbix_budget*.csv"
DEFAULT_API_URL = "https://prod.rhumbix.com/public_api/v2"
TWO_WEEKS_IN_SECONDS = 2 * 7 * 24 * 60 * 60


def clean_processed_folder(base_path):
    logging.info("Cleaning processed directory of expired files")
    processed_path = os.path.join(base_path, "processed")
    processed_path = os.path.join(processed_path, '')
    if not os.path.exists(processed_path):
        return
    paths = glob.glob("{}{}".format(processed_path, "*.csv"))
    for path in paths:
        if time.time() - os.path.getmtime(path) > TWO_WEEKS_IN_SECONDS:
            logging.info("Removing {} as it has expired".format(path))
            os.remove(path)


def move_file_to_processed(path):
    if os.path.exists(path):
        parent_path = (dirname(abspath(path)))
        processed_path = os.path.join(parent_path, "processed")
        if not os.path.exists(processed_path):
            # Create the processed directory
            os.makedirs(processed_path)
        processed_path = os.path.join(processed_path, os.path.basename(path))
        if os.path.exists(processed_path):
            logging.warning("Overwriting {} in processed directory!".format(processed_path))
        os.rename(path, processed_path)
    else:
        logging.warning("move_file_to_processed received nonexistent file: {}".format(path))


def handle_responses(responses, path):
    failed_responses = [x for x in responses if x.status_code != 200]
    if failed_responses:
        logging.error("Request(s) failed!\n{}".format(failed_responses))
    else:
        logging.info('{} successfully processed in {} batches'.format(path, len(responses)))
        move_file_to_processed(path)


def process_resource(csvs_directory, resource_name, filename_pattern, processor):
    paths = glob.glob("{}{}".format(csvs_directory, filename_pattern))
    logging.info("{} files={}".format(resource_name, paths))

    for path in paths:
        logging.info("Processing {} file: {}".format(resource_name, path))

        responses = processor.process_csv(path)
        handle_responses(responses, path)


def main():
    global employee_filename_pattern
    global project_filename_pattern
    global cost_code_filename_pattern
    global budget_filename_pattern
    parser = argparse.ArgumentParser()
    parser.add_argument("csvs_directory")
    parser.add_argument('api_key', nargs='?')
    parser.add_argument('api_url', nargs='?')
    args = parser.parse_args()

    config_dict = None
    if os.path.exists('config.json'):
        config_dict = json.load(open('config.json'))
        for name in ["api_key", "api_url"]:
            if not getattr(args, name, None):
                setattr(args, name, config_dict.get(name, None))

    if not getattr(args, "api_key", None):
        logging.error("api_key is not set. It can be passed as a command line argument or in config.json")

    if args.api_url is None:
        args.api_url = DEFAULT_API_URL

    # Load custom file name patterns
    if config_dict is not None:
        if "employee_filename_pattern" in config_dict:
            employee_filename_pattern = config_dict["employee_filename_pattern"]
        if "project_filename_pattern" in config_dict:
            project_filename_pattern = config_dict["project_filename_pattern"]
        if "cost_code_filename_pattern" in config_dict:
            cost_code_filename_pattern = config_dict["cost_code_filename_pattern"]
        if "budget_filename_pattern" in config_dict:
            budget_filename_pattern = config_dict["budget_filename_pattern"]

    args.csvs_directory = os.path.join(args.csvs_directory, '')

    logging.info("Processing directory {} with and api_key={} and api_url={}".format(
        args.csvs_directory, args.api_key, args.api_url))

    clean_processed_folder(args.csvs_directory)

    update_url_config(args.api_key, args.api_url)

    process_resource(args.csvs_directory, "Employee", employee_filename_pattern, employee_processor)
    process_resource(args.csvs_directory, "Project", project_filename_pattern, project_processor)
    process_resource(args.csvs_directory, "Cost Code", cost_code_filename_pattern, cost_code_processor)
    process_resource(args.csvs_directory, "Budget", budget_filename_pattern, budget_processor)


if __name__ == "__main__":
    main()
