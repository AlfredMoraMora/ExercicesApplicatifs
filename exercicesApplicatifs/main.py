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

# This function offers a way of printing all the numbers on a single line by
# creating a list to which the numbers will be added to and then printing that list
def print_decr_loop(val):
    numbers = []  # Create an empty list
    print(f"\nSmaller numbers than {val}")
    while val != 0:
        val -= 1
        numbers.append(val) # Append each number to the list
    print(" ".join(map(str, numbers))) # Print the list as a space-separated string

# A more straightforward way to print numbers on a single line is to use the 'end' parameter in the
# print() function. This avoids the need for a list and prints each value on the same line.
def print_croi_loop(val):
    print(f"\nBigger numbers than {val}")
    while val != 20:
        val += 1
        print(val, end=" ") # Print on the same line, separated by spaces
    print() # Add a newline after the loop

def print_pair_loop(val):
    print(f"\nPair numbers bellow {val}")
    while val !=0:
        val -= 1
        if val % 2 == 0:
            print(val, end=" ")
    print() # Add a newline after the loop

def print_imp_loop(val):
    print(f"\nImpair numbers bellow {val}")
    while val != 0:
        val -= 1
        if val % 2 != 0:
            print(val, end=" ")
    print()

def main():

    init_val = get_valid_input()
    print_decr_loop(init_val)
    print_croi_loop(init_val)
    print_pair_loop(init_val)
    print_imp_loop(init_val)

if __name__ == '__main__':
    main()

