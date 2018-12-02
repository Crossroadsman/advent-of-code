import unittest

from chronal_calibration.chronal_calibration import (
    calibrate,
    file_to_list,
    strs_to_ints
)


class CalibrateTest(unittest.TestCase):

    def test_valid_input_returns_correct_output(self):
        valid_input_data = [
            ('test_frequencies.txt', 3),
            ('test_frequencies_2.txt', 3),
            ('test_frequencies_3.txt', 0),
            ('test_frequencies_4.txt', -6),
        ]

        for datum in valid_input_data:
            result = calibrate(datum[0])
            self.assertEqual(
                result,
                datum[1]
            )


class FileToListTest(unittest.TestCase):

    def test_valid_filename_produces_valid_list(self):
        valid_filename = 'test_frequencies.txt'
        expected_list = ['1', '-2', '3', '1']

        result = file_to_list(valid_filename)

        self.assertEqual(
            result,
            expected_list
        )

    def test_invalid_filename_raises_FileNotFoundError(self):
        invalid_filename = 'nonsense_name.txt'

        with self.assertRaises(FileNotFoundError):
            calibrate(invalid_filename)

class StrsToIntsTest(unittest.TestCase):
 
    def test_invalid_input_raises_ValueError(self):
        invalid_input_data = ['hello', 'world']

        with self.assertRaises(ValueError):
            strs_to_ints(invalid_input_data)

    def test_valid_input_produces_correct_list(self):
        valid_input_data = ['1', '-2', '3', '1']
        expected_list = [1, -2, 3, 1]

        result = strs_to_ints(valid_input_data)

        self.assertEqual(
            result,
            expected_list
        )

