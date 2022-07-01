from my_annual_budget import Annual_Budget
from my_biweekly_budget import import BiWeekly

def new_budget():
    out_file = input("What is the name of your new budget?: ")
    if out_file[-4:] != ".txt":
        out_file += ".txt"

   
    print("             ")
    print("""Let's set up some default estimated values for some continuous expenses. You will be able to adjust these or change the specific expenses later""")
   print("             ")
    print("Type '0', if it does not apply")
    print("")


    income = float(input("Expected Annual income: "))
    housing = float(input("Expected monthly housing costs: "))
    groceries = float(input("Expected monthly cost of groceries: "))
    utilities = float(input("Expected monthly cost of utilities: "))
    gas = float(input("Expected monthly cost of gas:"))
    phone = float(input("Expected monthly cost of phone:"))
    loans = float(input("Expected monthly cost of loans:"))
    subscriptions = float(input("Expected monthly cost of subscriptions:"))
    num_months = float(input("Number of months you would like this budget to spread Annual income: "))

    annual_budget = Annual_Budget(income, housing, groceries, utilities, gas, phone, loans,
                                subscriptions,  num_months)
