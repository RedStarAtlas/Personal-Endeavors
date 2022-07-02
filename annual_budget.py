from biweekly_budget import BiWeekly

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
        allowance = (self.income)/self.num_months

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
        
        changes = input("Would you like to keep default gas and phone values of $%s and $%s, respectively? (Y/N): " % (self.gas,self.phone))
        if changes.lower() == "n":
            gas = input("Please enter gas amount: ")
            phone = input("Please enter phone amount: ")
            while not gas gas.isnumeric() or not phone.isnumeric():
                print("Please enter valid integers or decimals")
                gas = float(input("Please enter gas amount: "))
                phone = float(input("Please enter phone amount: "))
        else:
            gas = self.gas
            phone = self.phone
            housing = self.housing
            gas = float(gas)
            phone = float(phone)

        if self.month_list:
            prev_month = self.month_list[-1]

        #TODO: fix parameters here

            month  = BiWeekly(name, housing, allowance, groceries, utilities, gas, phone, 0, 0, prev_month)
        else:
            month = BiWeekly(name, housing, allowance, groceries, utilities, gas, phone)

        self.month_list.append(month)

        print(month.name, "created", "\n")

    def print_months(self):
        print("List of months currently in the system")
        for month in self.month_list:
            print(month.name, end=", ")

    def look_up_month(self):

        print("List of Months: ")
        for i in self.month_list:
            print(i.name)
        selected_month = ''
        while selected_month == '':
                
            month = input("Enter the name of the month you wish to view: ")
            for m in self.month_list:
                if m.name == month:
                    selected_month = m
            if selected_month == '':
                error_response = input("Month not found. Try again? (Y/N): ")
                if error_response.lower() == "n":
                    return -1

        return selected_month

    def edit_annual_income(self):
        income = input("Change in income amount: ")
        if income.isnumeric():
            monthly = int(income)/(10 - len(self.month_list))
            for m in self.month_list:
                m.monthly_allowance += monthly
            print("Transaction completed $" + income)
        else:
            print("Invalid answer, please try again")

    def annual_statement(self):
        print("Annual Statement:", "\n")
        print("Net Annual Income: $" + str(format(self.income, ",.2f")))

        for m in self.month_list:
            m.print_statement()
            print("-----------------")
            print("")

    def edit_default_values(self):

        pick = 0

        while pick != 12:
            print('1: Monthly Housing')
            print('2: Groceries')
            print('3: Utilities')
            print("4: Phone")
            print("5: Gas")
            print("6: loans")
            print("7: subscriptions")
            print("8: savings")
            print("9: investments")
            print("10: Additional Expenses")
            print('11: Expected number of months')
            print('12: Quit to budget menu')
            pick = input("Which default value would you like to change: ")

            while not pick.isnumeric() or int(pick) not in range(1,12):
                pick = input("Please select a valid input from 1 to 12: ")

            if pick == "12":
                break

            num_change = input("Enter amount you are changing the default value to: ")
            while not num_change.isnumeric() or float(num_change) < 0:
                num_change = input("Try again: ")

            pick = int(pick)
            num_change = float(num_change)

            if pick == 1:
                self.housing = num_change
            elif pick == 2:
                self.groceries = num_change
            elif pick == 3:
                self.utilities == num_change
            elif pick == 4:
                self.phone == num_change
            elif pick == 5:
                self.gas == num_change
            elif pick == 6:
                self.loans == num_change
            elif pick == 7:
                self.subscriptions == num_change
            elif pick == 8:
                self.savings == num_change
            elif pick == 9:
                self.investments == num_change
            elif pick == 10:
                self.num_months = num_change
          
            print("Change successful","\n")

    def annual_menu(self):

        pick = 0
        while pick != 6:
            print("Annual Budget Menu:")
            print("1: Create a month")
            print('2: Look at a month')
            print('3: Edit annual income')
            print('4: Look at annual statement')
            print('5: Edit default values for categories or expected number of months')
            print('6: Quit to main menu')
            pick = input("Enter a number: ")

            while not pick.isnumeric() or int(pick) not in range(1,7):
                pick = input("Invalid input, please select a digit between 1 and 6: ")

            pick = int(pick)

            if pick == 1:
                self.create_month()
            elif pick == 2:
                month = self.look_up_month()
                month.month_menu()
            elif pick == 3:
                self.edit_annual_income()
            elif pick == 4:
                self.annual_statement()
            elif pick == 5:
                self.edit_default_values()