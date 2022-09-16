# option + shift + click and drag to write on multiple statements
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
# Todo: 1. Prompt user by asking “What would you like?
is_on = True
profit = 0


def is_resource_suffient(order_ingredients):
    """Returns True when order can be made and False when ingredients are insufficient."""
    for ingredient in order_ingredients:
        if order_ingredients[ingredient] > resources[ingredient]:
            print(f"Sorry there is not enough {ingredient}.")
            return False
        return True


def process_coins():
    """Returns the total calculated from coins inserted."""
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total


def is_transaction_successful(money_recieved, drink_cost):
    """ Returns True if payment is accepted , or false if money is insuffient"""
    if money_recieved < drink_cost:
        print("sorry that's not enough money. Money refunded.")
        return False
    else:
        change = round(money_recieved - drink_cost, 2)
        print(f"Here is your change ${change}")
        global profit
        profit += drink_cost
        return True


def process_remaining_resources(drink_name, order_ingredient):
    """process remaining resources"""
    for ingredient in order_ingredient:
        resources[ingredient] -= order_ingredient[ingredient]
    print(f"Here is your {drink_name} ☕️☕😄️")


while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")

    if choice.lower() == "off":
        is_on = False
    elif choice.lower() == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: {profit}")
    else:
        drink = MENU[choice]
        if is_resource_suffient(drink["ingredients"]):
            payment = process_coins()
            print(f"payment ${payment}")
            if is_transaction_successful(payment, drink["cost"]):
                process_remaining_resources(choice, drink["ingredients"])
