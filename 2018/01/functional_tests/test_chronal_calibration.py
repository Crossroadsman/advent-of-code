import os
import unittest

#os.chdir(os.path.dirname(os.getcwd()))
#from .chronal_calibration import calibrate
from chronal_calibration.chronal_calibration import calibrate



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
        expected_frequency = 0

        result = calibrate(filename)

        self.assertEqual(
            result,
            expected_frequency
        )

        """She is suspicious that maybe this was just luck, so she tries
        some different frequency files
        """
        filename = 'test_frequencies_2.txt'
        expected_frequency = 10

        result = calibrate(filename)

        self.assertEqual(
            result,
            expected_frequency
        )


        filename = 'test_frequencies_3.txt'
        expected_frequency = 5

        result = calibrate(filename)

        self.assertEqual(
            result,
            expected_frequency
        )


        filename = 'test_frequencies_4.txt'
        expected_frequency = 14

        result = calibrate(filename)

        self.assertEqual(
            result,
            expected_frequency
        )

