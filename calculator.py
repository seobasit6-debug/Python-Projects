logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |
| |_________________| |
|  ___ ___ ___  ___   |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|
"""

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

def calculator():
    print(logo)

    num1 = float(input("What's the first number?: "))

    while True:
        for op in operations:
            print(op)

        op_choice = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))

        result = operations[op_choice](num1, num2)
        print(f"{num1} {op_choice} {num2} = {result}")

        next_step = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")

        if next_step == "y":
            num1 = result
        else:
            calculator()
            break

calculator()