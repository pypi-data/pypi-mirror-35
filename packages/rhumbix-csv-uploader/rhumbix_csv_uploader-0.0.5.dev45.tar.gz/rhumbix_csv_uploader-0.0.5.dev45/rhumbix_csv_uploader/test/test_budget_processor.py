import unittest
from rhumbix_csv_uploader.budget_processor import process_csv, read_budget_csv, prepare_data
from rhumbix_csv_uploader.test.processor_test_config import api_key, api_url

budget_test_csv = "rhumbix_csv_uploader/test/exampleCSVs/rhumbix_budget.csv"


class TestPrepareData(unittest.TestCase):
    def test_prepare_data(self):
        data = read_budget_csv(budget_test_csv)
        data = prepare_data(data)
        assert(all([x in data[0].keys()
                    for x in ["cost_code", "job_number", "quantities", "hours"]]))
        for d in data:
            assert(all([isinstance(v, float) for k, v in d.items() if k in ["quantities", "hours"]]))


class TestPostData(unittest.TestCase):
    def test_process_csv(self):
        responses = process_csv(budget_test_csv, api_key=api_key, api_url=api_url)
        self.assertTrue(all([x.status_code == 200 for x in responses]))
        bodies = [x.json() for x in responses]
        assert(all([all(x in body for x in ['creates', 'processed', 'updates']) for body in bodies]))
