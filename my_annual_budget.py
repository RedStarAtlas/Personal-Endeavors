from my_biweekly_budget import BiWeekly

class Annual_Budget(object):

    def __init__(self, income = 0, housing = 0, groceries = 0, utilities = 0, 
                 gas = 0, phone = 0, loans = 0, subscriptions = 0, savings = 0, 
                 investments = 0, biweekly_allowance = 0, num_month = 1):
                self.income = income
                self.month_list = []
                self.housing = housing
                self.groceries = groceries 
                self.utilities = utilities
                self.gas = gas
                self.phone = phone
                self.loans = loans 
                self.subscriptions = subscriptions
                self.savings = savings
                self.investments =  investments
                self.biweekly_allowance = biweekly_allowance
        
    def create_month(self):

        name = input("Give the month name: ")
        housing = self.housing
        allowance = self.add_tax(self.income)/self.num_months

        changes = input("Would you like to keep default grocery and utility values of $%s and $%s, respectively? (Y/N): " % (self.groceries,self.utilities))
        if changes.lower() == "n":
            groceries = input("Please enter grocery amount: ")
            utilities = input("Please enter utility amount: ")
            while not groceries groceries.isnumeric() or not utilities.isnumeric():
                print("Please enter valid integers or decimals")
                groceries = float(input("Please enter grocery amount: "))
                utilities = float(input("Please enter utility amount: "))
        else:
            groceries = self.groceries
            utilities = self.utilities
            housing = self.housing
            groceries = float(groceries)
            utilities = float(utilities)
        
        if self.month_list:
            prev_month = self.month_list[-1]

        #TODO: fix parameters here

            month  = Month(name, housing, allowance, groceries, utilities, 0, 0, prev_month)
        else:
            month = Month(name, housing, allowance, groceries, utilities)

        self.month_list.append(month)

        print(month.name, "created", "\n")
                
                