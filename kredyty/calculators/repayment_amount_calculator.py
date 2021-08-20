
class RepaymentAmountCalculator():
    """Class for calculating repayment_amount."""
    def __init__(self, amount, inerest_rate):
        self.amount = amount
        self.interest_rate = inerest_rate

    def calculate(self):
        """Calculate repayment_amount."""
        return self.amount * self.interest_rate / 100 + self.amount

