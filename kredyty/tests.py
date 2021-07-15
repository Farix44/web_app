from django.test import TestCase
import unittest
from .models import Loans
from .load_json import ConfigData
from .loan_validation import LoanValidation

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

class TestLoanValidation(TestCase):

    def test_validate(self):
        self.assertEqual(LoanValidation({"hour": 12}).validate(), True)
        self.assertEqual(LoanValidation({"hour": 7}).validate(), True)
        self.assertEqual(LoanValidation({"hour": 23}).validate(), True)
        self.assertEqual(LoanValidation({"hour": 1}).validate(), False)
        self.assertEqual(LoanValidation({"hour": 5}).validate(), False)

        self.assertNotEqual(LoanValidation({"hour": 8}).validate(), False)
        self.assertNotEqual(LoanValidation({"hour": 19}).validate(), False)
        self.assertNotEqual(LoanValidation({"hour": 22}).validate(), False)
        self.assertNotEqual(LoanValidation({"hour": 5}).validate(), True)
        self.assertNotEqual(LoanValidation({"hour": 3}).validate(), True)




if __name__ == '__main__':
    unittest.main()
