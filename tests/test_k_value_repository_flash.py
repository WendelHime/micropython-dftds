import os
import unittest
import tempfile
from dftds.kvalue_repository_flash import KValueRepositoryFlash

class TestKValueRepositoryFlash(unittest.TestCase):

    def setUp(self):
        self.filepath = "/tmp/test.json"
        self.repository = KValueRepositoryFlash(self.filepath)

    def test_read(self):
        try:
            with tempfile.NamedTemporaryFile(delete=False) as tmp:
                self.filepath = tmp.name
                tmp.write(bytes("", "utf-8"))

            self.repository = KValueRepositoryFlash(self.filepath)
            self.repository.read()
        except Exception as e:
            self.assertIsInstance(e, OSError)

    def test_write(self):
        self.repository.write(1.0)
        self.assertTrue(os.path.exists(self.filepath))

    def test_write_read(self):
        expected_k_value = 2.0
        self.repository.write(expected_k_value)
        self.assertTrue(os.path.exists(self.filepath))
        k_value = self.repository.read()
        self.assertEqual(expected_k_value, k_value)

    def tearDown(self):
        if os.path.exists(self.filepath):
            os.remove(self.filepath)
