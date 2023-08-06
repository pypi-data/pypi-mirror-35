import unittest
import sys
import os
import shutil
import requests
from mock import mock
from rhumbix_csv_uploader.csv_processor import main

TEST_LOCATION = 'rhumbix_csv_uploader/test'
TEST_FILES = ['rhumbix_budget.csv', 'rhumbix_cost_code_min.csv', 'rhumbix_employee.csv', 'rhumbix_project.csv']


def prepare_test_csv_folder():
    test_folder = os.path.join(TEST_LOCATION, 'test_csvs')
    if os.path.exists(test_folder):
        shutil.rmtree(test_folder)
    os.makedirs(test_folder)
    for f in TEST_FILES:
        shutil.copy(os.path.join(TEST_LOCATION, 'exampleCSVs', f), test_folder)


class TestCsvProcessor(unittest.TestCase):
    @mock.patch('requests.post')
    def test_main(self, mock_post):
        sys.argv = ['foo', 'rhumbix_csv_uploader/test/test_csvs']  # Either need to pass creds here or in config.json
        # Construct our mock response object, giving it relevant expected
        mock_response = mock.Mock()
        mock_response.status_code = 200
        # Assign our mock response as the result of our patched function
        mock_post.return_value = mock_response

        prepare_test_csv_folder()
        main()
        # `requests.post` was called.
        self.assertEqual(4, mock_post.call_count)
        # Make sure all files were moved to `processed` directory
        self.assertEqual(['processed'], os.listdir(os.path.join(TEST_LOCATION, 'test_csvs')))
        for f in TEST_FILES:
            self.assertTrue(os.path.exists(os.path.join(TEST_LOCATION, 'test_csvs', 'processed', f)))
