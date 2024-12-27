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

def process_coins():
    """Returns the total amount of coins in dollars that the user has inserted."""
    print("Please insert coins.")
    total = int(input("How many quarters? ")) * 0.25
    total += int(input("How many dimes? ")) * 0.1
    total += int(input("How many nickels? ")) * 0.05
    total += int(input("How many pennies? ")) * 0.01
    return total


def process_transaction(total_inserted_coins, the_drink):
    """Returns the required change for the transaction and updates profits."""
    global profit
    cost = the_drink["cost"]
    if cost < total_inserted_coins:
        profit += cost
        change = round(total_inserted_coins - cost, 2)
        return change
    else:
        return -1


def sufficient_supply_levels(order_ingredients):
    """Returns whether there are sufficient ingredients to make the order."""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def make_coffee(the_drink_ingredients):
    """Reduces the supply count by the ingredients needed for the order."""
    for item in the_drink_ingredients:
        resources[item] -= the_drink_ingredients[item]


profit = 0
machine_on = True

while machine_on:
    order = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if order == 'off':
        machine_on = False
    elif order == 'report':
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[order]
        if sufficient_supply_levels(drink["ingredients"]):
            total_paid = process_coins()
            total_change = process_transaction(total_paid, drink)
            if total_change == -1:
                print("Sorry that's not enough money. Money refunded.")
            else:
                make_coffee(drink["ingredients"])
                print(f"Here is ${total_change} in change.")
                print(f"Here is your {order} ☕. Enjoy!")
