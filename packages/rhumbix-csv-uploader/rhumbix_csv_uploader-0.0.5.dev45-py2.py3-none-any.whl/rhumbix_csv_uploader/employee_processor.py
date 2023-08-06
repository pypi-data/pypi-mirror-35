from rhumbix_csv_uploader.processor_utils import read_csv, get_headers, post_chunked_data, update_url_config, filter_values
fieldnames = ["company_supplied_id", "first_name", "last_name", "classification-role",
              "trade", "is_active", "phone", "email"]
required_fields = ["company_supplied_id", "classification-role"]
PROCESSOR_NAME = "employee_processor"


def read_employee_csv(path):
    return read_csv(path, fieldnames)


def prepare_data(data):
    data = filter_values(data, required_fields, PROCESSOR_NAME)
    data = transform_values(data)
    return data


def transform_values(data):
    """
    Transforms the csv values into the Rhumbix API format
    is_active.Active => is_active.True etc.
    """
    for person in data:
        person['is_active'] = person['is_active'] == 'Active'
        person['classification'] = person['classification-role'].split('-')[0]
        person['user_role'] = person['classification-role'].split('-')[1]
        del person['classification-role']

    return data


def process_csv(path, api_key=None, api_url=None):
    update_url_config(api_key, api_url)
    data = read_employee_csv(path)
    data = prepare_data(data)
    return post_chunked_data('employees', data, PROCESSOR_NAME)
