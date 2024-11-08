def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2

from art import logo

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}



additional_sum = True
start_afresh = True

while start_afresh:

    print(logo)
    current_user_input = float(input("What's the first number: "))
    additional_sum = True

    while additional_sum:

        print("+\n-\n*\n/")
        operation = input("Pick and operation: ")
        new_input = float(input("What's the next number?: "))

        result = operations[operation](current_user_input, new_input)

        print(f"{current_user_input} {operation} {new_input} = {result}")
        current_user_input = result

        to_continue = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation\n")
        if to_continue == 'n':
            additional_sum = False
            start_afresh = True
            print("\n" * 20)
