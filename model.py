import exceptions


class CalcPayment:

    def __init__(self, amount: float, interest_rate: float, number_of_payments: int):
        self.amount: float = amount
        self.interest_rate: float = interest_rate
        self.number_of_payments: int = number_of_payments
        self.interest_percentage: float = self.interest_rate/100

    def calc_monthly_payment(self) -> float:
        if self.amount == 0:
            raise exceptions.ZeroAmount
        elif self.interest_rate * 12 > 100:
            raise exceptions.Usury
        elif self.number_of_payments <= 0:
            raise exceptions.NegativeNumberOfFees
        elif self.number_of_payments == 1:
            return self.amount
        elif self.interest_rate == 0:
            return self.amount / self.number_of_payments
        else:
            return (self.amount * self.interest_percentage)/(1 - (1 + self.interest_percentage)**(-self.number_of_payments))

    def calc_total_interest(self) -> float:
        payment_value: float = self.calc_monthly_payment()
        total_interest: float = (payment_value * self.number_of_payments) - self.amount
        return total_interest
    
    def amortization(self) -> list:
        payment_value: float = round(self.calc_monthly_payment(), 2)
        balance: float = self.amount
        amortization_table: list = []
        if self.number_of_payments == 1:
            capital_payment = payment_value
            row = [1, 0, 0, capital_payment]
            amortization_table.append(row)
        else:
            for payment in range(1, self.number_of_payments + 1):
                payment_number = payment
                interest: float = round(self.interest_percentage * balance,2)
                capital_payment: float = round(payment_value - self.interest_percentage,2)
                balance: float = round(balance - capital_payment,2)
                if balance < 0 > -0.1:
                    balance = 0
                row: list = [payment_number, balance, interest, capital_payment]
                amortization_table.append(row)
    
        return amortization_table
    
    def calc_extra_payment(self, extra_payment: float, installment_of_extra_payment: int) -> list:
        payment_value: float = round(self.calc_monthly_payment(), 2)
        amortization_table: list = self.amortization()

        if extra_payment < payment_value:
            raise exceptions.InsufficientPayment
    
        balance = amortization_table[installment_of_extra_payment-2][1]
    
        if extra_payment > balance:
            raise exceptions.GreaterPayment
    
        extra_payment_amortization_table: list = []
    
        for installment in amortization_table:
            extra_payment_amortization_table.append(installment)

            if installment[0] == installment_of_extra_payment - 1:
                break
    
        for installment in range(amortization_table[installment_of_extra_payment-1][0], amortization_table[-1][0]):
            payment_number = installment
            interest: float = round(self.interest_percentage * balance, 2)

            if installment_of_extra_payment == amortization_table[installment_of_extra_payment - 1][0]:
                capital_payment: float = round(extra_payment - interest, 2)
            else:
                capital_payment: float = round(payment_value - interest, 2)
            balance = round(balance - capital_payment, 2)

            if balance == 0:
                capital_payment = extra_payment_amortization_table[-1][1]

            if balance <= 0:
                balance = 0

            row: list = [payment_number, balance, interest, capital_payment]
            extra_payment_amortization_table.append(row)

            if balance <= 0:
                break

        if extra_payment_amortization_table[-2][1] < extra_payment_amortization_table[-2][3]:
            extra_payment_amortization_table[-1][3] = extra_payment_amortization_table[-2][1]
        return extra_payment_amortization_table
