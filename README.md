# Simple_Calculator
This repository holds the answer to problem:
Create a Simple App Calculator
1.  The application will ask the user to choose one of the four math operations (Addition, Subtraction, Multiplication and Division)
2.  The application will ask the user for two numbers
3.  Display the result
4. The application will ask if the user wants to try again or not.
5. If yes, repeat Step 1.
6. If no, Display “Thank you!” and the program will exit 
7. Use Python Function and appropriate Exceptions to capture errors during runtime.
## Installation of pyfiglet
  - pyfiglet is a full port of FIGlet (http://www.figlet.org/) into pure python.
pip install pyfiglet
  - To install the pyfiglet module through pip installer from command prompt shell, we first have to open the command prompt terminal of our system and write down the following command in it:
```
pip install pyfiglet
```
## Installation of Termcolor
 - Change Text Color. To add color to our stylish text, we can combine pyfiglet and termcolor to create pretty text. 
 - To change the text color, we use a Python library called termcolor. To install termcolor, use:
 ```
 pip install termcolor
 ```
## Installation of PrettyTable
 - PrettyTable class inside the prettytable library is used to create relational tables in Python. 
 - Install via pip:
 ```
 python -m pip install -U prettytable
 ```
 Let's suppose you have a shiny new PrettyTable:
 ```
from prettytable import PrettyTable
table = PrettyTable()
 ```
and you want to put some data into it. You have a few options.

### Row by row
You can add data one row at a time. To do this you can set the field names first using the field_names attribute, and then add the rows one at a time using the add_row method:
 ```
table.title = '\033[95mSelect operation:'
table.field_names = ['Operation', 'Choice']
table.align['Operation'] = 'l'
table.add_row(['a.) Addition', 1])
table.add_row(['b.) Subtraction', 2])
table.add_row(['c.) Multiplication', 3])
table.add_row(['d.) Division', 4])
print(table)
 ```
