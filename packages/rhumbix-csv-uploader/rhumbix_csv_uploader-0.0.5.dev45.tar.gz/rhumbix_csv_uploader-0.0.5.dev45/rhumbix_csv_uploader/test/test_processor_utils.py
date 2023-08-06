from rhumbix_csv_uploader.processor_utils import post_chunked_data, MAX_POST_BATCH_SIZE, filter_values
import mock
import unittest
import math


class TestProcessorUtils(unittest.TestCase):
    @mock.patch('rhumbix_csv_uploader.processor_utils.post_data')
    def test_post_chunked_data_paging(self, mock_post):
        # Make sure that `post_chunked_data` doesn't exceed the limit, but also sends all data.
        data_lengths = [0, 1, 2, 50, 100, 300, 400, 600, 1000, 10000]
        for l in data_lengths:
            post_chunked_data('foo', list(range(l)), 'test')
            data_posted = []
            for call in mock_post.call_args_list:
                args, _ = call
                data_arg = args[1]
                self.assertTrue(len(data_arg) <= MAX_POST_BATCH_SIZE)
                data_posted += data_arg
            self.assertEqual(list(range(l)), data_posted)
            self.assertTrue(mock_post.call_count == math.ceil(float(l) / MAX_POST_BATCH_SIZE))
            mock_post.reset_mock()

    def test_filter_values(self):
        test_data = [
            {'first_name': 'Joe', 'last_name': 'Montana', 'age': '60'},
            {'first_name': 'Brett', 'last_name': 'Farve', 'age': ''}
        ]
        expected = [test_data[0]]
        result = filter_values(test_data, ['first_name', 'age'], 'foo')
        self.assertEqual(expected, result)
