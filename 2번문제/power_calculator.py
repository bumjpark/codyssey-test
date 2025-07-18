def calculate_power():
    try:
        number = float(input("Enter a number: "))
    except ValueError:
        print("Invalid number input.")
        return

    try:
        exponent = int(input("Enter the exponent: "))
    except ValueError:
        print("Invalid exponent input")
        return
    
    result = 1

    if exponent == 0:
        result = 1
    elif exponent > 0:
        for _ in range(exponent):
            result *= number
    else:
        for _ in range(-exponent):
            result /= number
    print(f"result: {result}")

if __name__ == "__main__":
    calculate_power()