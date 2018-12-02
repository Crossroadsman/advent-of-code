import os
import unittest

#os.chdir(os.path.dirname(os.getcwd()))
#from .chronal_calibration import calibrate
from chronal_calibration.chronal_calibration import calibrate



"""
if the sequence is: [1, -2, 3, 1], then, starting from a frequency of 0,
the following changes would occur:
 0  +1  ->  1
 1  -2  -> -1
-1  +3  ->  2
 2  +1  ->  3
"""
class ChronalCalibrationTest(unittest.TestCase):

    def test_chronal_calibration(self):
        
        """alice notices a file called `frequencies.txt` that contains
        a listing of all the frequency changes.

        She passes what she thinks is the filename into the calibrator,
        but there is a typo. The program responds with an error to
        confirm this
        """
        filename = 'misspelled_test_frequencies.txt'

        with self.assertRaises(FileNotFoundError):
            result = calibrate(filename)


        """Then she passes the correct filename into her calibrator and 
        notes the output frequency matches her expectation
        """
        filename = 'test_frequencies.txt'
        expected_frequency = 3

        result = calibrate(filename)

        self.assertEqual(
            result,
            expected_frequency
        )

        """She is suspicious that maybe this was just luck, so she tries
        some different frequency files
        """
        filename = 'test_frequencies_2.txt'
        expected_frequency = 3

        result = calibrate(filename)

        self.assertEqual(
            result,
            expected_frequency
        )


        filename = 'test_frequencies_3.txt'
        expected_frequency = 0

        result = calibrate(filename)

        self.assertEqual(
            result,
            expected_frequency
        )


        filename = 'test_frequencies_4.txt'
        expected_frequency = -6

        result = calibrate(filename)

        self.assertEqual(
            result,
            expected_frequency
        )
