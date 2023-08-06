import unittest
from rhumbix_csv_uploader.cost_code_processor import process_csv, read_cost_code_csv, prepare_data
from rhumbix_csv_uploader.test.processor_test_config import api_key, api_url

cost_code_test_csv = "rhumbix_csv_uploader/test/exampleCSVs/rhumbix_cost_code_min.csv"


class TestPrepareData(unittest.TestCase):
    def test_prepare_data(self):
        data = read_cost_code_csv(cost_code_test_csv)
        data = prepare_data(data)
        assert(all([x in data[0].keys()
                    for x in ["job_number", "code"]]))


class TestPostData(unittest.TestCase):
    def test_process_csv(self):
        responses = process_csv(cost_code_test_csv, api_key=api_key, api_url=api_url)
        self.assertTrue(all([x.status_code == 200 for x in responses]))
        bodies = [x.json() for x in responses]
        assert(all([all(x in body for x in ['creates', 'processed', 'updates']) for body in bodies]))
