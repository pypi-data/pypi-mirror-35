import unittest
from unittest.mock import patch

from Source.pricing_data_reader import PricingDataReader as datamanipulator


class PricingDataReaderTest(unittest.TestCase):
    mock_data_good = ["Rosco", "Dude", 99]
    mock_data_bad = []

    def test_do_manipulation(self):
        with patch.object(datamanipulator, "readData", return_value=PricingDataReaderTest.mock_data_good) as mocked_get, \
                patch.object(datamanipulator, "save_data", return_value=True) as mocked_save:
            result = datamanipulator.readRawdata()
            self.assertTrue(result)

        with patch.object(datamanipulator, "readData", return_value=PricingDataReaderTest.mock_data_bad) as mocked_get, \
                patch.object(datamanipulator, "savedata") as mocked_save:
            with self.assertRaises(ValueError):
                result = datamanipulator.readRawdata()
                self.assertTrue(result)
