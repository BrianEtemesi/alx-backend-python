#!/usr/bin/env python3
"""
test module for util
"""
import unittest
from utils import access_nested_map, get_json, memoize
from parameterized import parameterized
from unittest.mock import patch


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

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """
        tests that the fuction raises error when passed wrong inputs
        """
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """
    unit test class for get_json method
    """

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch('utils.requests.get')
    def test_get_json(self, test_url, test_payload, mock_get):
        """
        mock response
        """
        mock_response = unittest.mock.Mock()
        mock_response.json.return_value = test_payload

        mock_get.return_value = mock_response
        self.assertEqual(get_json(test_url), test_payload)


class TestMemoize(unittest.TestCase):
    """
    unit test class for utils.memoize decorator
    """

    def test_memoize(self):
        """
        test memoize
        """
        class TestClass:

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        # use @patch to mock a_method of TestClass
        with patch.object(TestClass, 'a_method') as mock_a_method:
            
            # set the return value for the mocked method
            mock_a_method.return_value = 42

            # create an instance of TestClass
            obj = TestClass()

            # call a_property twice
            result1 = obj.a_property
            result2 = obj.a_property

            # assert that the results are correct
            self.assertEqual(result1, 42)
            self.assertEqual(result2, 42)

            # assert that the mocked a_method is called only once
            mock_a_method.assert_called_once()
