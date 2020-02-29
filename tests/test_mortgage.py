import unittest
import os, sys

# Add lib/ to module lookup path
parent_dir = os.path.join(sys.path[0], '../lib')
sys.path.insert(1, parent_dir) 

from mortgage import *

class MortgageTestCase(unittest.TestCase):
    

    def setUp(self):
        self.mortgage = Mortgage(principal=100_000, apr=0.06)

    def teardown(self):
        pass

    def test_instantiate_mortgage(self):
        self.assertIsInstance(self.mortgage, Mortgage)

    def test_monthly_payment(self):
        self.assertEqual(round(self.mortgage.monthly_payment, 2), 639.81)
        self.assertIsInstance(self.mortgage.monthly_payment, float)
    
    def test_payments(self):
        # Payments is tuple of objects with expected keys
        self.assertIsInstance(self.mortgage.payments, tuple)

        first_payment = self.mortgage.payments[0]
        for prop in ['principal', 'interest', 'balance_start', 'balance_end']:
            self.assertTrue(prop in first_payment.keys()) 
        
        # Ends with 0 principal outstanding        
        self.assertEqual(round(self.mortgage.payments[-1]['balance_end'], 4), 0)

    def test_payments_field(self):
        for prop in ['principal', 'interest', 'balance_start', 'balance_end']:
            self.assertIsInstance(self.mortgage.payments_field(prop), tuple)

if __name__ == '__main__':
    unittest.main()
