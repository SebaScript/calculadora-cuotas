import unittest
from model import CalcPayment
import exceptions


class TestPayments(unittest.TestCase):

    def test_monthly_payment(self):
        amount = 200000
        interest_rate = 3.1
        number_of_payments = 36
        calc = CalcPayment(amount, interest_rate, number_of_payments)
        result = round(calc.calc_monthly_payment(), 2)
        expected_result = 9297.96
        self.assertEqual(result, expected_result)

    def test_total_interest(self):
        amount = 200000
        interest_rate = 3.1
        number_of_payments = 36
        calc = CalcPayment(amount, interest_rate, number_of_payments)
        result = round(calc.calc_total_interest(),2)
        expected_result = 134726.53
        self.assertEqual(result, expected_result)

    def test_total_interest_2(self):
        amount = 850000
        interest_rate = 3.4
        number_of_payments = 24
        calc = CalcPayment(amount, interest_rate, number_of_payments)
        result = round(calc.calc_total_interest(),2)
        expected_result = 407059.97
        self.assertEqual(result, expected_result)

    def test_interest(self):
        amount = 480000
        interest_rate = 0
        number_of_payments = 48
        calc = CalcPayment(amount, interest_rate, number_of_payments)
        result = round(calc.calc_total_interest(), 2)
        expected_result = 0
        self.assertEqual(result, expected_result)

    def test_usury(self):
        amount = 50000
        interest_rate = 12.4
        number_of_payments = 48
        calc = CalcPayment(amount, interest_rate, number_of_payments)
        self.assertRaises(exceptions.Usury, calc.calc_monthly_payment)

    def test_single_payment(self):
        amount = 90000
        interest_rate = 2.4
        number_of_payments = 1
        calc = CalcPayment(amount, interest_rate, number_of_payments)
        result = round(calc.calc_total_interest(), 2)
        expected_result = 0
        self.assertEqual(result, expected_result)

    def test_zero_amount(self):
        amount = 0
        interest_rate = 2.4
        number_of_payments = 60
        calc = CalcPayment(amount, interest_rate, number_of_payments)
        self.assertRaises(exceptions.ZeroAmount, calc.calc_monthly_payment)

    def test_negative_number_of_payments(self):
        amount = 2
        interest_rate = 3.1
        number_of_payments = -2
        calc = CalcPayment(amount, interest_rate, number_of_payments)
        self.assertRaises(exceptions.NegativeNumberOfFees, calc.calc_monthly_payment)

    def test_amortization(self):
        amount = 200000
        interest_rate = 3.10
        number_of_payments = 36
        calc = CalcPayment(amount, interest_rate, number_of_payments)
        table = calc.amortization()
        result = table[-1]
        self.assertListEqual(result, [36, 0, 279.57, 9018.39])

    def test_amortization_2(self):
        amount = 850000
        interest_rate = 3.40
        number_of_payments = 24
        calc = CalcPayment(amount, interest_rate, number_of_payments)
        table = calc.amortization()
        result = table[-1]
        self.assertListEqual(result, [24, 0, 1722.28, 50655.22])

    def test_amortization_single_payment(self):
        amount = 90000
        interest_rate = 2.40
        number_of_payments = 1
        calc = CalcPayment(amount, interest_rate, number_of_payments)
        table = calc.amortization()
        result = table[-1]
        self.assertListEqual(result, [1, 0, 0, 90000])

    def test_amortization_zero_interest_rate(self):
        amount = 480000
        interest_rate = 0
        number_of_payments = 48
        calc = CalcPayment(amount, interest_rate, number_of_payments)
        table = calc.amortization()
        result = table[-1]
        self.assertListEqual(result, [48, 0, 0, 10000])

    def test_amortization_extra_payment(self):
        amount = 200000
        interest_rate = 3.10
        number_of_payments = 36
        period = 10
        extra_payment = 53000
        calc = CalcPayment(amount, interest_rate, number_of_payments)
        result = calc.calc_extra_payment(extra_payment, period)
        result = result[-1]
        self.assertListEqual(result, [27, 0, 238.20, 7683.92])

    def test_amortization_extra_payment_2(self):
        amount = 850000
        interest_rate = 3.40
        number_of_payments = 24
        period = 5
        extra_payment = 90000
        calc = CalcPayment(amount, interest_rate, number_of_payments)
        result = calc.calc_extra_payment(extra_payment, period)
        result = result[-1]
        self.assertListEqual(result, [23, 0, 1129.65, 33225.06])

    def test_amortization_insufficient_extra_payment(self):
        amount = 850000
        interest_rate = 3.40
        number_of_payments = 24
        period = 10
        extra_payment = 45000
        calc = CalcPayment(amount, interest_rate, number_of_payments)
        self.assertRaises(exceptions.InsufficientPayment, calc.calc_extra_payment, extra_payment, period)

    def test_amortization_greater_extra_payment(self):
        amount = 850000
        interest_rate = 3.40
        number_of_payments = 24
        period = 22
        extra_payment = 180000
        calc = CalcPayment(amount, interest_rate, number_of_payments)
        self.assertRaises(exceptions.GreaterPayment, calc.calc_extra_payment, extra_payment, period)
