import csv
import pkg_resources
import requests
import logging
MAX_POST_BATCH_SIZE = 200
config = {}


def update_url_config(api_key, api_url):
    global config
    _config = {}
    if api_key:
        _config['api_key'] = api_key
    if api_url:
        _config['api_url'] = api_url
    config.update(_config)


def read_csv(path, fieldnames):
    data = []
    with open(path) as csvfile:
        reader = csv.DictReader(csvfile, fieldnames=fieldnames)
        for row in reader:
            data.append(row)
    return data


def filter_values(data, required_fields, processor_name):
    """
    Filters invalid rows
    """

    def has_required_fields(d):
        # The value is Truthy for all the required fields.
        missing_field_keys = set(required_fields) - set(d)
        if missing_field_keys:
            raise ValueError("Required keys were missing: {}".format(','.join(missing_field_keys)))
        return all([d[k] for k in required_fields])

    valid_data = filter(has_required_fields, data)
    num_filtered_rows = len(data) - len(valid_data)
    if num_filtered_rows:
        logging.info("Removed {} invalid rows in {}".format(num_filtered_rows, processor_name))

    return valid_data


def get_headers(api_key, processor_name):
    return {
        'x-api-key': api_key,
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Processor-Name': processor_name,
        'Processor-Version': pkg_resources.get_distribution("rhumbix_csv_uploader").version
    }


def post_data(endpoint, data, processor_name):
    url = '{}/{}/'.format(config['api_url'], endpoint)
    result = requests.post(url, headers=get_headers(
        config['api_key'], processor_name), json=data)
    return result


def post_chunked_data(endpoint, data, processor_name=""):
    responses = []
    chunk_size = MAX_POST_BATCH_SIZE
    for idx in range(0, len(data), chunk_size):
        responses.append(post_data(endpoint, data[idx:idx+chunk_size], processor_name))
    return responses
