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