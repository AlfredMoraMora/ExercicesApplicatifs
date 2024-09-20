# code a program that prompts the user for a number from 1 to 20 and then it prints all the values smaller to that number until 0
def get_valid_input():
    while True:
        try:
            # Prompt user for input
            n = int(input("Enter a number from 1 to 20: "))
            # Check if the input is within the valid range
            if 1 <= n <= 20:
                return n
            else:
                print("Please enter a number from 1 to 20")
        except ValueError:
            # Handle the case were input is not an integer
            print("Invalid input. Please enter a valid integer from 1 to 20")

def print_numbers_below(val):
    print(f"Numbers below {val}:")
    for num in range(val - 1, -1, -1):
        print(num, end=" ")  # Print the numbers in a single line with a space separator
    print()  # Add a newline after the loop

def print_numbers_above(val):
    print(f"Numbers above {val}:")
    for num in range(val + 1, 21):
        print(num, end=" ")
    print()

def print_numbers_pair(val):
    print(f"Pair numbers below {val}:")
    for num in range(val - 1, -1, -1):
        if num % 2 == 0:
            print(num, end=" ")
    print()

def print_numbers_impair(val):
    print(f"Impair numbers below {val}:")
    for num in range(val - 1, -1, -1):
        if num % 2 != 0:
            print(num, end=" ")
    print()

def main():
    init_val = get_valid_input()
    print_numbers_below(init_val)
    print_numbers_above(init_val)
    print_numbers_pair(init_val)
    print_numbers_impair(init_val)

if __name__ == '__main__':
    main()