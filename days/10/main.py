import art

print(art.logo)

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
    "/": divide
}

def do_calculation():
    should_accumulate = True

    n1 = float(input("What's the first number?: "))

    for symbol in operations:
        print(symbol)

    while should_accumulate:
        operation = input("Pick an operation: ")
        n2 = float(input("What's the next number?: "))
        final_result = operations[operation](n1, n2)
        print(f"{n1} {operation} {n2} = {final_result}")
        answer = input(f"Type 'y' to continue calculating with {final_result}, or type 'n' to start a new calculation: ")
        if answer == "y":
            n1 = final_result
        else:
         should_accumulate = False
         print("\n" * 20)
         do_calculation()

do_calculation()