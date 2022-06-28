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
        self.name = name
        self. prev_two_weeks = prev_two_weeks

    def add_actual_spent(self):

        x = input("What is the total number actually spent for the last biweekly budget?: ")
        if x.isnumeric() and float(x) >= 0:
            self.actual_spent = float(x)
            print("$" + x, "of actual spent recorded")
        else:
            print("Invalid amount type, please only put the numbers without any signs")

    