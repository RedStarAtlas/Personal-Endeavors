from zipfile import _PathOpenProtocol


class BiWeekly(object):
    
    def __init__(
        self,
        name,
        housing,
        utilities,
        groceries,
        gas,
        phone,
        loans,
        subscriptions,
        savings,
        investments,
        biweekly_allowance,
        actual_spent = 0,
        add_expense = 0,
        prev_two_weeks = None):

        #if there is any leftover money from the previous two weeks
        if prev_two_weeks == None:
            self.leftover = 0
        else:
            self.leftover = prev_two_weeks.calc_leftover()

        #Necessity Bills
        self.housing = housing
        self.utilities = utilities
        self.groceries = groceries
        self.gas = gas
        self.phone = phone
        self.loans = loans      #yes, if you have loans this needs to be a necessity to pay off
        
        #Miscellaneous Bills and Extra Cash
        self.subscriptions = subscriptions
        self.savings = savings
        self.investments = investments
        self.biweekly_allowance = biweekly_allowance
        self.actual_spent = actual_spent
        self.add_expense = add_expense
        self.name = name
        self. prev_two_weeks = prev_two_weeks

    def add_actual_spent(self):

        x = input("What is the total number actually spent for the last biweekly budget?: ")
        if x.isnumeric() and float(x) >= 0:
            self.actual_spent = float(x)
            print("$" + x, "of actual spent recorded")
        else:
            print("Invalid amount type, please only put the numbers without any signs")
    
    #How much of the Misc expenses were spent
    def additional_expenses(self):
        while not expense.isnumeric():
            expense = input("Please add an expense amount, only the numeric value")

        expense = float(expense)
        self.add_expense += expense

        while another_expense.lower() != "none":
            another_expense = input("Please add another expense, or type 'none' if finished: ")
            while not another_expense.isnumeric() or float(another_expense) < 0 or not another_expense.lower() == "none":
                another_expense = input("Please input a valid number: ")

            another_expense = float(ex)
            self.add_expense += another_expense

    def add_income(self):
        amount = input("Please enter the amount: ")
        while not amount.isnumeric() or float(amount) < 0:
            amount = input("Invalid amount type, please only use digits and decimals. Income cannot be negative. Press 'Q' to quit or enter a valid amount: ")
            if amount.lower() == "q":
                return

            self.biweekly_allowance += float(amount) < 0:
            print(amount, "added to biweekly income")

    def calc_current_leftover(self):
        return self.prev_two_weeks.calc_leftover()

    #calculates the amount of spending income
    def calc_spending_income(self):
        assests = self.biweekly_allowance + self.leftover
        expenses = self.housing + self.utilities + self.groceries + self.add_expense
        return assests - expenses

    #calculates the leftover income to next month
    def calc_leftover(self):
        spending_income = self,calc_spending_income()

        return spending_income - self.actual_spent

        


    