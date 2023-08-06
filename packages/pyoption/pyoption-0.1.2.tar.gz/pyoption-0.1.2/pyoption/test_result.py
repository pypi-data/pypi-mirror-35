from unittest import TestCase
from .result import *

class TestResult(TestCase):
    """Test the Result pattern classes and methods"""
    def test_ok_return_value(self):
        func = lambda x, y : Ok(x / y)
        self.assertEqual(0.5, func(1, 2).unwrap())
        self.assertTrue(func(1, 2).is_ok())

    def test_err_unwrap_raises_error(self):
        func = lambda : Err('Invalid division')
        func2 = lambda : func().unwrap()

        self.assertRaises(RuntimeError, func2)

    def test_err_contains_error(self):
        error = Err('Invalid division')

        self.assertFalse(error.is_ok())
        self.assertTrue(error.is_err())

    def test_override_error_using_expect(self):
        error = Err('Invalid division')

        try:
            error.expect('Error')
            self.assertFail()
        except RuntimeError as err:
            self.assertEqual('Error: Invalid division', str(err))

    def test_expect_for_ok_acts_like_unwrap(self):
        result = Ok(True)
        self.assertTrue(result.expect('If this object is an error'))

    def test_unwrap_err_with_ok_and_err_objects(self):
        result = Ok('Success')
        error = Err('Failure')
        func = lambda : result.unwrap_err('Message')

        self.assertEqual('Failure', error.unwrap_err('Message'))
        self.assertRaises(RuntimeError, func)

    def test_expect_err_with_ok_and_err_objects(self):
        result = Ok('Success')
        error = Err('Failure')

        self.assertEqual('Failure', error.expect_err('Message'))

        try:
            result.expect_err('Hey there')
            self.assertFail()
        except RuntimeError as err:
            self.assertEqual('Hey there: Success', str(err))

    def test_result_shortcut(self):
        result = Result(None, 'Failure')

        self.assertTrue(result.is_err())
        self.assertEqual('Failure', result.unwrap_err(''))

    def test_result_shortcut_with_ok(self):
        result = Result(3.14159, None)

        self.assertTrue(result.is_ok())
        self.assertEqual(3.14159, result.unwrap())
