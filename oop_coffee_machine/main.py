from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

items = Menu()
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()

def coffee_machine():
    operation = input(f"What would you like? {items.get_items()}: ").lower()
    if operation == "report":
        coffee_maker.report()
        money_machine.report()
        coffee_machine()
        return
    if operation == "off":
        return

    drink = items.find_drink(operation)
    if drink != None:
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
                coffee_machine()
            else:
                coffee_machine()
                return
        else:
            coffee_machine()
            return
    else:
        coffee_machine()
        return
    return

coffee_machine()