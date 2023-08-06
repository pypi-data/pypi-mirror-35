from unittest import TestCase
from pyoption.option import *

class TestOption(TestCase):
    """Test the Option pattern classes and methods"""
    def test_some_return_value(self):
        result = Some(27)

        self.assertEqual(27, result.unwrap())
        self.assertTrue(result.is_some())
        self.assertFalse(result.is_none())

    def test_none_return_value(self):
        result = Some(None)

        self.assertTrue(result.is_none())
        self.assertFalse(result.is_some())

    def test_expect_method_on_some_and_none(self):
        result = Some(True)
        none = Some(None)

        self.assertTrue(result.expect('Error!'))

        try:
            none.expect('Error!')
            self.assertFail()
        except RuntimeError as err:
            self.assertEqual('Error!', str(err))

    def test_unwrap_method_on_some_and_none(self):
        result = Some(True)
        none = Some(None)
        func = lambda : none.unwrap()

        self.assertTrue(result.unwrap())
        self.assertRaises(RuntimeError, func)

    def test_unwrap_or_method(self):
        self.assertEqual(2, Some(2).unwrap_or(3))
        self.assertEqual(2, Some(None).unwrap_or(2))

    def test_unwrap_or_else_method(self):
        k = 10
        func = lambda : k * 2

        self.assertEqual(4, Some(4).unwrap_or_else(func))
        self.assertEqual(20, Some(None).unwrap_or_else(func))