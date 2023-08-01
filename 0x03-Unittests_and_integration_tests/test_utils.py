#!/usr/bin/env python3
"""Tests for Generic utilities for github org client.
"""
import unittest
from typing import Tuple, Dict, Mapping, Union
from unittest.mock import Mock, patch
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """Test cases for `access_nested_map`"""

    @parameterized.expand(
        [
            ({"a": 1}, ("a",), 1),
            ({"a": {"b": 2}}, ("a",), {"b": 2}),
            ({"a": {"b": 2}}, ("a", "b"), 2),
        ]
    )
    def test_access_nested_map(
        self, mapping: Mapping, path: Tuple, expected: Union[Dict, int]
    ) -> None:
        """tests the `access_nested_map` function"""
        self.assertEqual(access_nested_map(mapping, path), expected)

    @parameterized.expand(
        [
            ({}, ("a",), KeyError),
            ({"a": 1}, ("a", "b"), KeyError),
        ]
    )
    def test_access_nested_map_exception(
        self, mapping: Mapping, path: Tuple, exception: Exception
    ) -> None:
        """tests that `access_nested_map` raises an exception"""
        with self.assertRaises(exception):
            access_nested_map(mapping, path)


class MockedResponse(Mock):
    """Custom mock Object"""

    def __init__(self, data: Dict) -> None:
        """initializer for custom Mocked object"""
        super().__init__()
        self.data = data

    def json(self) -> Dict:
        """mock json method for `requests.get`"""
        return self.data


class TestGetJson(unittest.TestCase):
    """Testcases for `get_json`"""

    @parameterized.expand(
        [
            ("http://example.com", {"payload": True}),
            ("http://holberton.io", {"payload": False}),
        ]
    )
    @patch("requests.get")
    def test_get_json(self, url: str, payload: Dict, mock_get: Mock) -> None:
        """tests for `get_json` method"""
        mock_get.return_value = MockedResponse(data=payload)
        self.assertEqual(get_json(url), payload)
        mock_get.assert_called_once_with(url)


class TestMemoize(unittest.TestCase):
    """Testcases for `memoize`"""

    def test_memoize(self):
        """tests the memoize function"""

        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        test_obj = TestClass()
        with patch.object(test_obj, "a_method", return_value=42) as mock_a_method:
            a = test_obj.a_property
            a = test_obj.a_property
            mock_a_method.assert_called_once()


if __name__ == "__main__":
    unittest.main()
