def find_min_max(numbers):
    
    min_num = max_num = numbers[0]

    for num in numbers[1:]:
        if num < min_num:
            min_num = num
        if num > max_num:
            max_num = num
    return min_num, max_num

def main():
    try:
        user_input = input("Enter numbers separated by spaces: ")
        number_strings = user_input.strip().split() 
        numbers =[float(n) for n in number_strings]

        min_val, max_val = find_min_max(numbers)
        print(f"Minimum: {min_val}, Maximum: {max_val}")
    except ValueError:
        print("Invalid input") 
    
if __name__ == "__main__":
    main()