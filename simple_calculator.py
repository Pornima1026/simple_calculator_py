# =========================================
#         SIMPLE PYTHON CALCULATOR
# =========================================

def show_header():
    print("=" * 40)
    print("       SIMPLE PYTHON CALCULATOR")
    print("=" * 40)


def show_menu():
    print("\nAvailable Operations")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Modulo (%)")


def get_numbers():
    while True:
        try:
            values = input("\nEnter numbers (space separated): ").split()

            if len(values) < 2:
                print("Please enter at least two numbers.")
                continue

            numbers = [float(value) for value in values]
            return numbers

        except ValueError:
            print("Invalid input! Enter only numbers.")


def get_operation():
    valid = ["+", "-", "*", "/", "%"]

    while True:
        operation = input("\nChoose operation (+, -, *, /, %): ")

        if operation in valid:
            return operation

        print("Invalid operation. Try again.")


def calculate(numbers, operation):

    result = numbers[0]

    for number in numbers[1:]:

        if operation == "+":
            result += number

        elif operation == "-":
            result -= number

        elif operation == "*":
            result *= number

        elif operation == "/":
            if number == 0:
                print("\nError: Cannot divide by zero.")
                return None
            result /= number

        elif operation == "%":
            if number == 0:
                print("\nError: Cannot perform modulo by zero.")
                return None
            result %= number

    return result


def display_result(numbers, operation, result):

    expression = f" {operation} ".join(str(num) for num in numbers)

    print("\n" + "-" * 40)
    print("Expression:")
    print(expression)
    print("\nResult:")
    print(result)
    print("-" * 40)


def main():

    show_header()

    while True:

        show_menu()

        numbers = get_numbers()

        operation = get_operation()

        result = calculate(numbers, operation)

        if result is not None:
            display_result(numbers, operation, result)

        again = input("\nDo another calculation? (Y/N): ").strip().lower()

        if again != "y":
            print("\nThank you for using the calculator.")
            break


if __name__ == "__main__":
    main()