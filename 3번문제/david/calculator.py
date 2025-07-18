def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Error: Division by zero.")
    return a / b

def calculator():
    a = input("Enter the first number (float): ")
    b = input("Enter the second number (float): ")
    operator = input("Enter an operator (+, -, *, /): ")

    try:
        a = int(float(a))
        b = int(float(b))
    except ValueError:
        print("Invalid input: Please enter valid numbers.")
        return

    try:
        if operator == '+':
            result = add(a, b)
        elif operator == '-':
            result = subtract(a, b)
        elif operator == '*':
            result = multiply(a, b)
        elif operator == '/':
            result = divide(a, b)
        else:
            print("Invalid operator.")
            return

        print(f"Result: &lt;{result}&gt;")

    except ZeroDivisionError as e:
        print(e)

if __name__ == "__main__":
    calculator()
    