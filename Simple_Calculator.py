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

