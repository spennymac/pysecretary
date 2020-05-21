import os
import unittest

from pysecretary import pysecretary, InvalidPrefixError, UnsupportedPrefixError


class TestPysecretary(unittest.TestCase):
    def test_env_get(self):
        os.environ["PYSECRETARY"] = "test"
        t = pysecretary.get("env://PYSECRETARY")
        self.assertEqual(t, "test")

    def test_env_raise(self):
        os.environ.clear()
        with self.assertRaises(KeyError):
            pysecretary.get("env://PYSECRETARY")

    def test_unsupported_prefix(self):
        with self.assertRaises(UnsupportedPrefixError):
            pysecretary.get("invalid://PYSECRETARY")

    def test_invalid_prefix(self):
        with self.assertRaises(InvalidPrefixError):
            pysecretary.get("PYSECRETARY")

        with self.assertRaises(InvalidPrefixError):
            pysecretary.get("v:/PYSECRETARY")
           
        with self.assertRaises(InvalidPrefixError):
            pysecretary.get("://PYSECRETARY")
