from project.loans.base_loan import BaseLoan


class MortgageLoan(BaseLoan):
    def __init__(self):
        super().__init__(3.5, 50000.0)

    def increase_interest_rate(self):
        self.interest_rate += 0.5

# In the mortgage_loan.py file, the class MortgageLoan should be implemented.
# A mortgage loan is a type of loan.
# Each mortgage loan has an interest rate of 3.5 percent and an amount of 50000.0 EUR.
# Methods
# __init__()
#     • In the __init__ method, all the needed attributes must be set.
# increase_interest_rate()
#     • The method increases the interest rate by 0.5 percent.
