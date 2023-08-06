import logging
from rhumbix_csv_uploader.processor_utils import read_csv, get_headers, post_chunked_data, update_url_config, filter_values


logging.basicConfig(level=logging.INFO)
fieldnames = ["job_number", "name", "is_active", "address"]
required_fields = ["job_number", "name"]
PROCESSOR_NAME = "project_processor"


def read_project_csv(path):
    return read_csv(path, fieldnames)


def prepare_data(data):
    data = filter_values(data, required_fields, PROCESSOR_NAME)
    data = transform_values(data)
    return data


def transform_values(data):
    """
    Transforms the csv values into the Rhumbix API format
    """
    for d in data:
        d["status"] = "ACTIVE" if d["is_active"] == "A" else "INACTIVE"
        del d["is_active"]
    return data


def process_csv(path, api_key=None, api_url=None):
    update_url_config(api_key, api_url)
    data = read_project_csv(path)
    data = prepare_data(data)
    return post_chunked_data('projects', data, PROCESSOR_NAME)
