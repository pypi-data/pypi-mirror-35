import unittest
from rhumbix_csv_uploader.employee_processor import process_csv, read_employee_csv, prepare_data
from rhumbix_csv_uploader.test.processor_test_config import api_key, api_url


employee_test_csv = "rhumbix_csv_uploader/test/exampleCSVs/rhumbix_employee.csv"


class TestPrepareData(unittest.TestCase):
    def test_prepare_data(self):
        data = read_employee_csv(employee_test_csv)
        data = prepare_data(data)
        assert(data[0]["is_active"])
        assert(all(role in ["ADMIN", "FOREMAN", "PM", "WORKER", "OFFICE_STAFF"]
                   for role in [d["user_role"] for d in data]))


class TestPostData(unittest.TestCase):
    def test_process_csv(self):
        responses = process_csv(employee_test_csv, api_key=api_key, api_url=api_url)
        self.assertTrue(all([x.status_code == 200 for x in responses]))
        bodies = [x.json() for x in responses]
        assert(all([all(x in body for x in ['creates', 'processed', 'updates']) for body in bodies]))
