import unittest
import calc_planned_saving_exceptions
from calc_planned_saving_model import CalcPlannedSaving


class TestCalcPlannedSaving(unittest.TestCase):
    def test_total_saving(self):
        monthly_amount: float = 9000
        interest_rate: float = 0.70
        months: int = 36
        calc = CalcPlannedSaving(monthly_amount, interest_rate, months)
        expected_result = 367029.0298
        self.assertEqual(expected_result, calc.calc_total_saving())

    def test_total_saving_2(self):
        monthly_amount: float = 36000
        interest_rate: float = 0.80
        months: int = 48
        calc = CalcPlannedSaving(monthly_amount, interest_rate, months)
        expected_result = 2096568.1724
        self.assertEqual(expected_result, calc.calc_total_saving())

    def test_saving_goal(self):
        monthly_amount: float = 9000
        interest_rate: float = 0.70
        goal = 200000
        calc = CalcPlannedSaving(monthly_amount, interest_rate)
        expected_result = 21
        self.assertEqual(expected_result, calc.calc_saving_goal(goal))

    def test_saving_goal_2(self):
        monthly_amount: float = 36000
        interest_rate: float = 0.80
        goal = 1000000
        calc = CalcPlannedSaving(monthly_amount, interest_rate)
        expected_result = 26
        self.assertEqual(expected_result, calc.calc_saving_goal(goal))
