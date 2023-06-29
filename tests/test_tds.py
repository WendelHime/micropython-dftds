import unittest
from dftds.tds import calculate_ec

class TestECCalc(unittest.TestCase):

    def test_ec_calc(self):
        response = calculate_ec(5.01, 1.0)
        self.assertAlmostEqual(14651.1775, response, places=2)
