import requests
import logging
from rhumbix_csv_uploader.processor_utils import read_csv, parse_arguments, get_headers

logging.basicConfig(level=logging.INFO)
fieldnames = ["job_number", "name", "cost_code", "phase",
              "description", "Project Manager - Unused", "Active - unused", "Incomplete - unused"]
company_key = None
api_key = None
PROCESSOR_NAME = "job_cost_processor"


def read_job_cost_csv(path):
    return read_csv(path, fieldnames)


def transform_values(data):
    """
    Transforms the csv values into the Rhumbix API format
    """
    for d in data:
        d["cost_codes"] = [
            {"code": '-'.join([d["phase"], d["cost_code"]]), "description": d["description"]}]
        del d["phase"]
        del d["cost_code"]
        del d["description"]
    return data


def post_data(data):
    url = 'https://async-api.rc.rhumbix.com/V1_0_1/{}/batch/project/import'.format(
        company_key)
    result = requests.post(url, headers=get_headers(api_key, PROCESSOR_NAME), json=data)
    return result


def get_batch_status(batch_id):
    url = 'https://async-api.rc.rhumbix.com/V1_0_1/{}/batch/project/import/{}/status'.format(
        company_key, batch_id)
    return requests.get(url, headers=get_headers(api_key, PROCESSOR_NAME))


def process_csv(path, _company_key, _api_key):
    global company_key
    global api_key
    company_key = _company_key
    api_key = _api_key
    data = read_job_cost_csv(path)
    data = transform_values(data)
    return post_data(data)


if __name__ == "__main__":
    args = args = parse_arguments()
    result = process_csv(args.csv_path, args.company_key, args.api_key)
    log_function = logging.info if 200 <= result.status_code <= 299 else logging.warning
    if log_function is logging.warning:
        log_function("Something went wrong with uploading csv data")
    log_function(result.status_code)
    log_function(result.json())
