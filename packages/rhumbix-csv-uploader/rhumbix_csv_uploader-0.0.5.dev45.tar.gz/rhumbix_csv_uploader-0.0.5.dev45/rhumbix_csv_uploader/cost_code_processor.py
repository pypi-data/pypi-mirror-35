import logging
from rhumbix_csv_uploader.processor_utils import read_csv, get_headers, post_chunked_data, update_url_config, filter_values

logging.basicConfig(level=logging.INFO)
fieldnames = ["job_number", "name", "cost_code", "phase",
              "description", "Project Manager - Unused", "is_active", "Incomplete - unused"]
required_fields = ["job_number", "phase", "cost_code"]
PROCESSOR_NAME = "cost_code_processor"


def read_cost_code_csv(path):
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
        d["code"] = '-'.join([d['phase'], d["cost_code"]])
        d["is_active"] = d["is_active"] == "A"

        valid_api_fields = ['code', 'job_number', 'units',
                            'erp_units', 'is_active', 'group', 'description']

        extra_fields = set(d) - set(valid_api_fields)
        for f in extra_fields:
            del d[f]

    return data


def process_csv(path, api_key=None, api_url=None):
    update_url_config(api_key, api_url)

    data = read_cost_code_csv(path)
    data = prepare_data(data)
    return post_chunked_data('cost_codes', data, PROCESSOR_NAME)
