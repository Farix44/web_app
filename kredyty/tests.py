from django.test import TestCase
import unittest
from .load_json import ConfigData
from kredyty.validators.loan_validation_hour import LoanValidationHour
from kredyty.validators.check_loan_validators import CheckLoanValidators

# Create your tests here.

class TestConfigData(TestCase):

    def test_container(self):
        data = ConfigData()
        self.assertEqual(6, data.get_data()['min_hour'])
        self.assertEqual(10000, data.get_data()['max_amount'])
        self.assertEqual(36, data.get_data()['max_period'])
        self.assertNotEqual(21, data.get_data()['max_hour'])
        self.assertNotEqual(9999, data.get_data()['max_amount'])
        self.assertIn('min_hour', data.json_data)
        self.assertIn('max_period', data.json_data)
        self.assertNotIn('dragon', data.json_data)
        self.assertNotIn('pigeon', data.json_data)

class TestLoanValidationHour(TestCase):

    def test_validate(self):
        self.assertEqual(LoanValidationHour({"hour": 12}).validate(), True)
        self.assertEqual(LoanValidationHour({"hour": 7}).validate(), True)
        self.assertEqual(LoanValidationHour({"hour": 23}).validate(), True)
        self.assertEqual(LoanValidationHour({"hour": 1}).validate(), False)
        self.assertEqual(LoanValidationHour({"hour": 5}).validate(), False)

        self.assertNotEqual(LoanValidationHour({"hour": 8}).validate(), False)
        self.assertNotEqual(LoanValidationHour({"hour": 19}).validate(), False)
        self.assertNotEqual(LoanValidationHour({"hour": 22}).validate(), False)
        self.assertNotEqual(LoanValidationHour({"hour": 5}).validate(), True)
        self.assertNotEqual(LoanValidationHour({"hour": 3}).validate(), True)


if __name__ == '__main__':
    unittest.main()
