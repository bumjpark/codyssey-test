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

def evaluate_expression():
    expression = input("Enter expression: ")
    tokens = expression.strip().split()

    if len(tokens) != 3:
        print("Invalid expression format. Use: number operator number (e.g., 2 + 3)")
        return

    a_str, operator, b_str = tokens

    try:
        a = float(a_str)
        b = float(b_str)
    except ValueError:
        print("Invalid numbers.")
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

        print(f"Result: {result}")

    except ZeroDivisionError as e:
        print(e)

if __name__ == "__main__":
    evaluate_expression()