from art import logo
from resources import MENU, resources


def resource_check(resources, operation):
    if resources["water"] >= MENU[operation]["ingredients"]["water"]:
        if  resources["coffee"] >= MENU[operation]["ingredients"]["coffee"]:
            if resources["milk"] >= MENU[operation]["ingredients"]["milk"]:
                return True
            else:
                print("Sorry there is not enough milk.")
                return False
        else:
            print("Sorry there is not enough coffee.")
            return False

    else:
        print("Sorry there is not enough water.")
        return False


def transaction(resources,operation):
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    penny = int(input("How many pennies?: "))
    total = (0.25 * quarters) + (0.10 * dimes) +(0.05 * nickles) + (0.01 * penny)
    change = total - MENU[operation]['cost']
    if change >=0:
        change = "{:.2f}".format(change)
        print(f"Here is ${change} in change.")
        print(f"Here is your {operation}, Enjoy!")
        resource_change(resources,operation)
        return
    else :
        print("Sorry that's not enough money. Money refunded.")
        return


def print_resources(resources):
    milk = resources['milk']
    coffee = resources['coffee']
    money = resources['money']
    water = resources['water']
    print(f"Water : {water}\nMilk : {milk}\nCoffee : {coffee}\nMoney : {money}\n")
    return


def resource_change(resources, operation):
    resources["water"] -= MENU[operation]["ingredients"]["water"]
    resources["coffee"] -= MENU[operation]["ingredients"]["coffee"]
    resources["milk"] -= MENU[operation]["ingredients"]["milk"]
    resources["money"] += MENU[operation]["cost"]
    return


def coffee_machine():
    operation = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if operation == 'espresso':
        if resource_check(resources, operation):
            transaction(resources,operation)
            coffee_machine()
        else:
            coffee_machine()
    elif operation == 'latte':
        if resource_check(resources, operation):
            if resource_check(resources, operation):
                transaction(resources, operation)
                coffee_machine()
        else:
            coffee_machine()
    elif operation == 'cappuccino':
        if resource_check(resources, operation):
            if resource_check(resources, operation):
                transaction(resources, operation)
                coffee_machine()
        else:
            coffee_machine()
    elif operation == 'report':
        print_resources(resources)
        coffee_machine()
    elif operation == 'off':
        return
    return

coffee_machine()
