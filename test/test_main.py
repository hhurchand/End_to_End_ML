import pytest,unittest
from src.main import read_data

class TestMyFunctions(unittest.TestCase):
    def test_my_functions(self):
        df = read_data("data/processed/train.csv")
        obtained = len(df)
        expected = 4250

        self.assertEqual(obtained,expected)
        