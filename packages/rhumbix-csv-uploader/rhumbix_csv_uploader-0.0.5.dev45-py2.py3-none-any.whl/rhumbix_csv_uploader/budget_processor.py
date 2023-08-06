from rhumbix_csv_uploader.processor_utils import read_csv, get_headers, post_chunked_data, update_url_config, filter_values

fieldnames = ["cost_code", "job_number", "quantities", "hours"]
required_fields = ["cost_code", "job_number"]
PROCESSOR_NAME = "budget_processor"


def read_budget_csv(path):
    return read_csv(path, fieldnames)


def prepare_data(data):
    data = filter_values(data, required_fields, PROCESSOR_NAME)
    data = transform_values(data)
    return data


def transform_values(data):
    """
    Transforms the csv values into the Rhumbix API format
    :param data array of dicts that represent csv values
    """
    for d in data:
        d["quantities"] = float(d.get("quantities") or 0)
        d["hours"] = float(d.get("hours") or 0)

    return data


def process_csv(path, api_key=None, api_url=None):
    update_url_config(api_key, api_url)

    data = read_budget_csv(path)
    data = prepare_data(data)
    return post_chunked_data('budgets', data, PROCESSOR_NAME)
