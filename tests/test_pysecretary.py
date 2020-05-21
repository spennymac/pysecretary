import os
import unittest

from pysecretary import pysecretary


class TestPysecretary(unittest.TestCase):
    def test_env_get(self):
        os.environ["PYSECRETARY"] = "test"
        t = pysecretary.get("env://PYSECRETARY")
        self.assertEqual(t, "test")

    def test_env_raise(self):
        os.environ.clear()
        with self.assertRaises(KeyError):
            pysecretary.get("env://PYSECRETARY")
