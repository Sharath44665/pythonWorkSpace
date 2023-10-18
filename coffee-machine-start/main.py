import coffee_maker
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

machinePower = "on"
isResourceExist = "y"
coffeeMaker = CoffeeMaker()
coffeeMoney = MoneyMachine()

while machinePower == "on":
    coffeeType = input("What would you like? (espresso/latte/cappuccino/): ")

    if coffeeType == "e" or coffeeType == "espresso":
        coffeeType = "espresso"
    elif coffeeType == "l" or coffeeType == "latte":
        coffeeType = "latte"
    elif coffeeType == "c" or coffeeType == "cappuccino":
        coffeeType = "cappuccino"

    order = Menu()
    menuItem = order.find_drink(coffeeType)
    # print(menuItem.name) # gives name
    # print(menuItem.ingredients) # gives dictionary of that item

    # check for existing resources
    # coffeeMaker.report()
    if coffeeMaker.is_resource_sufficient(menuItem):
        # userMoney = float(input("enter amount for your purchase: $ "))

        if coffeeMoney.make_payment(menuItem.cost):
            coffeeMaker.make_coffee(menuItem)

        coffeeReport = input("Do you want to see the coffee machine report? yes or no: ")
        if coffeeReport == "yes" or coffeeReport == "y":
            coffeeMaker.report()

        moneyReport = input("Do you want to see machine money report? yes or no: ")
        if moneyReport == "y" or moneyReport == "yes":
            coffeeMoney.report()

    machinePower = input("Do you want to power off the Coffee Machine? yes or no: ").lower()

    if machinePower == "y" or machinePower == "yes":
        machinePower = "off"
    else:
        machinePower = "on"
    print("""
    _____________________________
    """)
