import os
import unittest

from pysecretary import pysecretary, InvalidPrefixError, UnsupportedPrefixError
from pysecretary.exceptions import NotFoundError


class TestPysecretary(unittest.TestCase):
    def test_env_get(self):
        os.environ["PYSECRETARY"] = "test"
        t = pysecretary.get("env://PYSECRETARY")
        self.assertEqual(t, "test")

    def test_env_raise(self):
        os.environ.clear()
        with self.assertRaises(NotFoundError):
            pysecretary.get("env://PYSECRETARY")

    def test_unsupported_prefix(self):
        with self.assertRaises(UnsupportedPrefixError):
            pysecretary.get("invalid://PYSECRETARY")

    def test_invalid_prefix(self):
        with self.assertRaises(InvalidPrefixError):
            pysecretary.register("", lambda x, y: x)

        with self.assertRaises(InvalidPrefixError):
            pysecretary.get("PYSECRETARY")

        with self.assertRaises(InvalidPrefixError):
            pysecretary.get("v:/PYSECRETARY")

    def test_with_default(self):
        t = pysecretary.get("env://PYSECRETARY", 'default')
        self.assertEqual(t, 'default')

        t = pysecretary.get("PYSECRETARY", 'default')
        self.assertEqual(t, 'default')
