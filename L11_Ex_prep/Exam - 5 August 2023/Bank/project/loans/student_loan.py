from project.loans.base_loan import BaseLoan


class StudentLoan(BaseLoan):
    def __init__(self):
        super().__init__(1.5, 2000)

    def increase_interest_rate(self):
        self.interest_rate += 0.2

# In the student_loan.py file, the class StudentLoan should be implemented.
# A student loan is a type of loan. Each student loan has an interest rate of 1.5 percent
# and an amount of 2000.0 EUR.
# Methods
# __init__()
#     • In the __init__ method, all the needed attributes must be set.
# increase_interest_rate()
#     • The method increases the interest rate by 0.2 percent.
