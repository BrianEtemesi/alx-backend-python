#!/usr/bin/env python3
"""
test module for util
"""
import unittest
from utils import access_nested_map
from parameterized import parameterized


class TestAccessNestedMap(unittest.TestCase):
    """
    unit test class
    """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])

    def test_access_nested_map(self, nested_map, path, value):
        """
        unit test for `access_nested_map` method
        """
        result = access_nested_map(nested_map, path)
        self.assertEqual(result, value)

