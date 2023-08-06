import unittest
from rhumbix_csv_uploader.project_processor import process_csv, read_project_csv, prepare_data
from rhumbix_csv_uploader.test.processor_test_config import api_key, api_url


project_test_csv = "rhumbix_csv_uploader/test/exampleCSVs/rhumbix_project.csv"


class TestPrepareData(unittest.TestCase):
    def test_prepare_data(self):
        data = read_project_csv(project_test_csv)
        data = prepare_data(data)
        assert("is_active" not in data[0])
        assert(data[0]["status"] in ("ACTIVE", "INACTIVE"))

    def test_process_csv(self):
        responses = process_csv(project_test_csv, api_key=api_key, api_url=api_url)
        self.assertTrue(all([x.status_code == 200 for x in responses]))
        bodies = [x.json() for x in responses]
        assert(all([all(x in body for x in ['creates', 'processed', 'updates']) for body in bodies]))
