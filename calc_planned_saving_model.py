import calc_planned_saving_exceptions


class CalcPlannedSaving:

    def __init__(self, monthly_amount: float, interest_rate: float, months: int = 0):
        self.monthly_amount: float = monthly_amount
        self.interest_rate: float = interest_rate
        self.interest_percentaje: float = self.interest_rate / 100
        self.months: int = months

    def calc_total_saving(self):
        total_interest: float = 0
        subtotal: float = 0
        for month in range(1, self.months + 1):
            subtotal += round(self.monthly_amount + total_interest, 4)
            total_interest = round(self.interest_percentaje * subtotal, 4)
        return round(subtotal, 4)

    def calc_saving_goal(self, goal: float):
        total_interest: float = 0
        subtotal: float = 0
        count = 0
        while subtotal <= goal:
            count += 1
            subtotal += round(self.monthly_amount + total_interest, 4)
            total_interest = round(self.interest_percentaje * subtotal, 4)
            print(count)
            if subtotal >= goal:
                return count


total_saving = CalcPlannedSaving(9000, 0.7, 36)
saving_goal = CalcPlannedSaving(9000, 0.7)
print(total_saving.calc_total_saving())
print(saving_goal.calc_saving_goal(200000))
