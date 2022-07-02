class BiWeekly(object):
    
    def __init__(self, name, housing, utilities, groceries, actual_spent = 0, add_expense = 0, prev_two_weeks = None):

        #if there is any leftover money from the previous two weeks
        if prev_two_weeks == None:
            self.leftover = 0
        else:
            self.leftover = prev_two_weeks.calc_leftover()

        #Necessity Bills
        self.housing = housing
        self.utilities = utilities
        self.groceries = groceries
##        self.gas = gas
##        self.phone = phone
##        self.loans = loans      #yes, if you have loans this needs to be a necessity to pay off
      
        #Miscellaneous Bills and Extra Cash
##       self.subscriptions = subscriptions
##        self.savings = savings
##        self.investments = investments
##        self.biweekly_allowance = biweekly_allowance
        self.actual_spent = actual_spent
        self.add_expense = add_expense
        self.name = name
        self.prev_two_weeks = prev_two_weeks

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

    def edit_expenses(self):
        where = 0
        while where != "0":
            print("Where would you like to change expenses?")
            print("1: Housing")
            print("2: Utilities")
            print("3: Groceries")
            print("4: Phone")
            print("5: Gas")
            print("6: loans")
            print("7: subscriptions")
            print("8: savings")
            print("9: investments")
            print("10: Additional Expenses")
            print("11: Quit to monthly menu")
            where = input("Enter a number: ")

            num_change = input("What would you like to edit expense amount to: ", "\n")
            num_change = float(num_change)

            if int(where) in range(1,10):
                if where == "1":
                    self.housing = num_change
                elif where == "2":
                    self.utilities = num_change
                elif where == "3":
                    self.groceries == num_change
                elif where == "4":
                    self.phone == num_change
                elif where == "5":
                    self.gas == num_change
                elif where == "6":
                    self.loans == num_change
                elif where == "7":
                    self.subscriptions == num_change
                elif where == "8":
                    self.savings == num_change
                elif where == "9":
                    self.investments == num_change
                elif where == "10":
                    self.additional_expenses(num_change)
                else:
                    print("Sorry, invalid option. Please choose 1-10")

    def(biweekly_menu)(self):
        pick = 0
        while pick != 8:
            print('-----------------------------')
            print('')
            print('1: Look at your BiWeekly Statement')
            print('2: Add your actual amount spent for this pay period')
            print('3: Calculate leftover money to the next pay period')
            print('4: Add additional, unaccounted for expenses')
            print('5: Add extra income to this pay period')
            print('6: Change expense amounts for one or more of the categories')
            print('7: Calculate free spending money')
            print('8: Quit to annual budget menu')
            pick = input("Select an option: ")
            print("")
            if pick.isnumeric() and int(pick) in range(1,9):
                pick = int(pick)

                if pick == 1:
                    self.print_statement()
                elif pick == 2:
                    self.add_actual_spending()
                elif pick == 3:
                    self.calc_leftover()
                    print("Next pay period's spillover: " + str(format(self.calc_leftover(), ",.2f")), "\n")
                elif pick == 4:
                    self.additional_expenses()
                elif pick == 5:
                    self.add_income()
                elif pick == 6:
                    self.edit_expenses()
                elif pick == 7:
                    sp_income = self.calc_spending_income()
                    print("Spending Money for this pay period: $", str(format(sp_income, ",.2f")))

            else:
                print("Invalid pick, please try again")

    #prints the income, earnings, and expenses
    def print_statement(self):
        print(self.name + "'s " + "BiWeekly Statement:", "\n")
        print("Starting Balance")
        print("-----------------------------")
        print("BiWeekly Allowance: $" + str(format(self.biweekly_allowance, ",.2f")))
        print("Last pay period's leftover: $" + str(format(self.leftover, ",.2f")))
        print("------------------------")
        assets = self.biweekly_allowance + self.leftover
        print("Total assets: $" + str(format(assets, ",.2f")), "\n")

        print("Expenses: ")
        print("Housing: $" + str(format(self.housing, ",.2f")))
        print("Groceries: $" + str(format(self.groceries, ",.2f")))
        print("Utilities: $" + str(format(self.utilities, ",.2f")))
        print("Gas: $" + str(format(self.gas, ",.2f")))
        print("Phone: $" + str(format(self.phone, ",.2f")))
        print("Loans: $" + str(format(self.loans, ",.2f")))
        print("Subscriptions: $" + str(format(self.subscriptions, ",.2f")))
        print("Savings: $" + str(format(self.savings, ",.2f")))
        print("Investments: $" + str(format(self.investments, ",.2f")))
        print("BiWeekly Allowance: $" + str(format(self.biweekly_allowance, ",.2f")))
        print("Additional Spending: $"+ str(format(self.add_expense, ",.2f")))

        expenses = self.housing + self.groceries + self.utilities + 
                   self.gas + self.phone + self.loans + self.subscriptions + self.savings 
                   self.investments + self.biweekly_allowance + self.add_expense

        print("------------------------")
        print("Total Expenses: $" + str(format(expenses, ".2f")), "\n")
        print("Spending Money: $"+str(format(self.calc_spending_income(), ".2f")))
        if self.actual_spending != 0:
            print("Actual amount spent: $" + str(self.actual_spending))
            print("Next pay period's leftover: $" + str(format(self.calc_leftover(), ".2f")))

        print("End of BiWeekly Statement", "\n")

def main():
    x= Month("September",12,32,43,32)

    spending  = x.calc_spending_income()
    print(str(spending))
    print(type(spending))

    print(x.actual_spending)
    print(type(x.actual_spending))

    