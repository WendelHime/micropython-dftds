import os
import unittest
from dftds.kvalue_repository_flash import KValueRepositoryFlash

class TestKValueRepositoryFlash(unittest.TestCase):

    def setUp(self):
        self.filepath = "test.json"
        self.repository = KValueRepositoryFlash(self.filepath)

    def test_read(self):
        try:
            with open(self.filepath, 'w') as tmp:
                tmp.write("")
            self.repository.read()
        except Exception as e:
            self.assertIsInstance(e, OSError)

    def test_write(self):
        self.repository.write(1.0)
        self.assertTrue(self.filepath in os.listdir())

    def test_write_read(self):
        expected_k_value = 2.0
        self.repository.write(expected_k_value)
        self.assertTrue(self.filepath in os.listdir())
        k_value = self.repository.read()
        self.assertEqual(expected_k_value, k_value)

    def tearDown(self):
        os.remove(self.filepath)
