# Paulean Marguerette F. Parrish
# Bscpe 1-4
# Simple Calculator activity

# Import everything needed for design
from termcolor import colored
from pyfiglet import Figlet
from prettytable import PrettyTable

# Header
print('=' * 54)
f = Figlet(font = "standard")
print(colored(f.renderText('Oh, Hi there!'), 'cyan'))
print('=' * 54)

# Ask the name of the user
name=input("\nWhat's your name? ")
print("\n")
print("         \\|||||/        ")
print("         ( OᴗO )         ")
print("+--ooO------------------+")
print("|                       |")
print("|     Hello " + name + "     |")
print("|                       |")
print("+------------------Ooo--+")
print("         |__||__|        ")
print("          ||  ||         ")
print("         ooO  Ooo        ")

# Ask the user to choose one of the four math operations
table = PrettyTable()

table.title = '\033[95mSelect operation:'
table.field_names = ['Operation', 'Choice']
table.align['Operation'] = 'l'
table.add_row(['a.) Addition', 1])
table.add_row(['b.) Subtraction', 2])
table.add_row(['c.) Multiplication', 3])
table.add_row(['d.) Division', 4])
print(table)

# Take input from the user
def calculate():
    while True:
        try:
            choice = input("\n\033[92mPlease enter your chosen operation (1/2/3/4): ")
            if choice not in ["1", "2", "3", "4"]:
                raise ValueError

            # Ask the user for two numbers
            num1 = float(input("\nEnter the first number: "))
            num2 = float(input("Enter the second number: "))

            # Calculate the given operation and display the result
            if choice == '1':
                result = num1 + num2
                print("\n\033[93mThe result of", num1, "+", num2, "is:", result)
            elif choice == '2':
                result = num1 - num2
                print("\n\033[93mThe result of", num1, "-", num2, "is:", result)
            elif choice == '3':
                result = num1 * num2
                print("\n\033[93mThe result of", num1, "*", num2, "is:", result)
            elif choice == '4':
                if num2 == 0:
                    raise ZeroDivisionError
                else:
                    result = num1 / num2
                    print("\n\033[93mThe result of", num1, "/", num2, "is:", result)
                continue

            # Ask if the user wants to try again or not
            choice = input("\n\033[96mDo you want to try again? 'y' or 'n': ")

            # Raise Value error
            if choice not in ["y", "n"]:
               raise ValueError

            # If yes, repeat Step 1
            if choice == 'y':
                continue

            # If no, Display “Thank you!” and the program will exit
            else:
                r = Figlet(font = "cybermedium")
                print(colored(r.renderText('\nThank you!'), 'red'))
                break
           
        # Use Python Function and appropriate Exceptions to capture errors during runtime
        except ValueError:
            print("\n\033[31mSorry! Invalid input, please enter one of the given choices")
        except ZeroDivisionError:
            print("\n\033[31mSorry! You are dividing by zero")
            
calculate()
            

