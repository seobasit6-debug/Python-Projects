MENU = {
    "espresso": {
        "ingredients": {"water": 50, "milk": 0, "coffee": 18},
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {"water": 200, "milk": 150, "coffee": 24},
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {"water": 250, "milk": 100, "coffee": 24},
        "cost": 3.0,
    },
}

resources = {
    "water": 300,   # ml
    "milk": 200,    # ml
    "coffee": 100,  # g
    "money": 0.0,   # $
}


def print_report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${resources['money']:.2f}")


def check_resources(drink):
    ingredients = MENU[drink]["ingredients"]
    for item in ("water", "milk", "coffee"):
        if ingredients[item] > resources[item]:
            print(f"Sorry, there is not enough {item}.")
            return False
    return True


def process_coins():
    print("Please insert coins.")
    quarters = int(input("How many quarters? "))
    dimes    = int(input("How many dimes? "))
    nickles  = int(input("How many nickles? "))
    pennies  = int(input("How many pennies? "))
    return quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01


def check_transaction(inserted, drink):
    cost = MENU[drink]["cost"]
    if inserted < cost:
        print("Sorry that's not enough money. Money refunded.")
        return False
    change = round(inserted - cost, 2)
    if change > 0:
        print(f"Here is ${change:.2f} in change.")
    resources["money"] += cost
    return True


def make_coffee(drink):
    ingredients = MENU[drink]["ingredients"]
    for item in ("water", "milk", "coffee"):
        resources[item] -= ingredients[item]
    print(f"Here is your {drink}. Enjoy!")


def main():
    machine_on = True
    while machine_on:
        choice = input("What would you like? (espresso/latte/cappuccino): ").strip().lower()

        if choice == "off":
            print("Turning off the coffee machine. Goodbye!")
            machine_on = False

        elif choice == "report":
            print_report()

        elif choice in MENU:
            if check_resources(choice):
                inserted = process_coins()
                if check_transaction(inserted, choice):
                    make_coffee(choice)

        else:
            print("Invalid option. Please choose espresso, latte, or cappuccino.")


if __name__ == "__main__":
    main()