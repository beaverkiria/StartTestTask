from django.test import TestCase
import LoginValidator


class LoginValidatorTestCases(TestCase):
    def test_one_symbol_valid_login(self):
        self.assertTrue(LoginValidator.is_login_valid('a'), 'One symbol test with valid login \'a\'')

    def test_one_symbol_invalid_login1(self):
        self.assertFalse(LoginValidator.is_login_valid('1'), 'One symbol test with invalid login \'1\'')

    def test_one_symbol_invalid_login2(self):
        self.assertFalse(LoginValidator.is_login_valid('+'), 'One symbol test with invalid login \'+\'')

    def test_empty_login(self):
        self.assertFalse(LoginValidator.is_login_valid(''), "Empty login test")

    def test_maximum_length(self):
        self.assertTrue(LoginValidator.is_login_valid('a' + ('1' * 5) + ('.' * 5) + ('-' * 5) + ('b' * 3) + '3'), 'Maximum length valid login')

    def test_overflow(self):
        self.assertFalse(LoginValidator.is_login_valid('a' * 21), 'Overflow test')

    def test_value_error(self):
        with self.assertRaises(ValueError):
            LoginValidator.is_login_valid(123)