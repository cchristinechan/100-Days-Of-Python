import art

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

# we don't add brackets because we are storing the functions, not triggering them
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

restart = True

while restart:
    print(art.logo)

    # catching invalid value error - keeps asking until input is valid
    while True:
        try:
            num1 = float(input("What is the first number? "))
            break
        except ValueError:
            print("\nInvalid input. Please enter a valid number.")

    continue_calculating = True
    while continue_calculating:
        for symbol in operations:
            print(symbol)
        # catching invalid key error - keeps asking until input is valid
        try:
            operation = input("Pick an operation: ")
            if operation not in operations:
                raise KeyError("Invalid operation")
        except KeyError:
            print("\nInvalid operation. Please enter a valid operation.")
            continue

        # catching invalid value error - keeps asking until input is valid
        while True:
            try:
                num2 = float(input("What is the next number? "))
                break
            except ValueError:
                print("\nInvalid input. Please enter a valid number.")

        result = operations[operation](num1, num2)
        print(f"{num1} {operation} {num2} = {result}")
        use_result_as_num1 = input(f"Type 'y' to continue calculating with {result}, "
                                   f"type 'n' to start a new calculation, "
                                   f"or type 'e' to end: " ).lower()
        if use_result_as_num1 == 'y':
            num1 = result
        elif use_result_as_num1 == 'n':
            continue_calculating = False
            print("\n" * 20)
        elif use_result_as_num1 == 'e':
            continue_calculating = restart = False
