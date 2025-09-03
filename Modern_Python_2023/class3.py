import numpy as np
import pandas as pd
import ssl

print("Operators, comments and zen of python\n")

# Arithmetic operators work from left to right access power (**)
# Power operator works from right to left
# ari
# for in :- (for item in iterable ) (in - different)
# (Membership Operators) in, not in  :-  user_input in names (check in memory) (in - different)

# Extracting Data from a URL

# Disable SSL certificate verification (not recommended for production)
ssl._create_default_https_context = ssl._create_unverified_context
#ssl.....    is used to disable SSL certificate 

url = "https://www.w3schools.com/python/python_operators.asp"
tables = pd.read_html(url)

# Check if any tables were found
if len(tables) > 0:
    # Access the first table (if there are multiple)
    result_table = tables[0]
    print(result_table)
else:
    print("No tables found on the webpage.")

print("\n1- Python Arithmetic Operators ( + - * / )  \n")
a : int = 7
b : int = 2

print(a + b) # addtition
print(a - b) # subtraction
print(a * b) # multiplication
print(a / b) # division

a : int = 11
b : int = 3

print(a % 3)  # Modulus:-   2
print(2**3)   #  **  Exponentiation :- 8

print("\n12/3= 4.0 converted in float")
print(12/3) # 4.0

print(14/3)  # 4.666666666666667

# //  Float division
print("\n//  Float division :- give round figure")
print(14//3)   # 4

#Python Assignment Operators
print("\n2- Python Assignment Operators (=  =+ -= *= /=)")
# Check if any tables were found
if len(tables) > 0:
    # Access the first table (if there are multiple)
    result_table = tables[1]
    print(result_table)
else:
    print("No tables found on the webpage.")

num : int = 4
print(num)  # 4

num += 3
print(num) # 7

num -= 2
print(num) # 5

num *= 4
print(num) # 20

num /= 2
print(num)  # 10.0

# Python Comparison Operators  (== != > < >= <=)
print("\n3- Python Comparison Operators (== != > < >= <=) (Return TRUE or FALSE)")

# Check if any tables were found
if len(tables) > 0:
    # Access the first table (if there are multiple)
    result_table = tables[2]
    print(result_table)
else:
    print("No tables found on the webpage.")

# Python Comparison Operators  (== != > < >= <=)
print("\nnum1 = 4, num2 = 5")
num1 : int = 4
num2 : int = 5

print( num1 == num2)    # Flase
print ( num1 != num2 )  # True
# != :- when num2 is not allow to login

print( num1 > num2)     # Flase
print( num1 < num2)     # True
print( num1 >= num2)    # False
print( num1 <= num2)    # True

print("num3 = 5, num4 = 5")
num3 : int = 5
num4 : int = 5

print( num3 == num4 )  # True
print( num3 != num4)   # False
print( num3 > num4)    # False
print( num3 < num4 )   # False
print( num3 >= num4)   # True
print( num3 <= num4 )  # True

print("num6 = 5, num7 = 5")
num5 : int = 8
num6 : int = 3

print( num5 == num6 )   # False
print( num5 != num6 )   # True
print( num5 > num6 )    # True
print( num5 < num6 )    # False
print( num5 >= num6 )   # True
print( num5 <= num6 )   # False

print(''' 
ASCII Code  (Unicode)
A = 65  B = 66  Z = 90                    
a = 97  b = 98  z = 122
0=48    1=49    9=57
''')

# ord() :- get the Unicode code point of a character
val1 : str = ord('A')   # 65  
print(val1)

# chr() :-  get  a character from a Unicode code point
val2 : str = chr(65)    # A
print(val2)

a : str = 'A'
b : str = 'B'

print( b >= a )     # True
print( b <= a)      # False

print( a >= b )     # False
print( a <= b)      # True

# Python Logical Operators  (and or not)
print("\n4- Python Logical Operators (and - or - not)")

# Check if any tables 3 were found
if len(tables) > 0:
    # Access the first table (if there are multiple)
    result_table = tables[3]
    print(result_table)
else:
    print("No tables found on the webpage.")

# Python Logical Operators  (and or not)  # and لازمی # or = optional
print("\nand (necessary) لازمی ,,  or = optional  ")
print("\nAND (Logical Operators) Return TRUE if all Comparisons are TURE otherwise Flase")

compare_and : str = True and True and True and True     # True
print(compare_and)

compare_and1 : str = True and True and True and False     # False
print(compare_and1)

print("\nOR (Logical Operators) Return TRUE if any one is TURE otherwise Flase")
compare_or : str = False or False or False or False  # Flase
print(compare_or)

compare_or1 : str = False or False or False or True  # Ture
print(compare_or1)

print("\n NOT (Logical Operators) not :-  Reverse the result")

compare_not : str = not True    # False
print(compare_not)

compare_not1 : str = not False    # True
print(compare_not1)

name : str = "Ali"
print(not name == "Ali")    # Flase (not:- reverse the answer)
print( name == "Ali")       # True (original the answer)

print( name == "Akbar")     # Flase (name is change)
print(not name == "Akbar")  # True 

# Python Identity Operators
print("\n5- Python Identity Operators (is,  is not {compare object})")
print('''
      Identity operators (`is` , `is not`) are used to 
      compare the memory locations of two objects. 
      ''')
# Check if any tables were found
if len(tables) > 0:
    # Access the first table (if there are multiple)
    result_table = tables[4]
    print(result_table)
else:
    print("No tables found on the webpage.")

# concept of deep and shallow 
# name are different but physical address on backend (memory) is same
x : str = 'abc'  
y : str = 'abc'

print(id(x))    # 4442898464 (memory address on backend)
print(id(y))    # 4442898464 (memory address on backend)

print( x == y )    # True  (check on value level)
print( x is y)     # Ture  (check on memory level)
print( x is not y) # False (check on memory level)

# name are different and physical address on backend is different
i : str = 'abc'
j : str = 'xyz'
print(id(i))    # 4527304736 (memory address on backend)
print(id(j))    # 4531511600 (memory address on backend)

print( i == j )     # False  (check on value level)
print( i is j )     # False  (check on memory level)
print( i is not j ) # True  (check on memory level)

# Python Membership Operators
print("\n6- Python Membership Operators (in,  not in ) (important)")
print('''
      Membership Operators:- test whether a value or variable is found
      in a sequence (such as a string, list, or tuple).
      ''')
# Check if any tables were found
if len(tables) > 0:
    # Access the first table (if there are multiple)
    result_table = tables[5]
    print('result_table', result_table)
else:
    print("No tables found on the webpage.")

# List Comprehension to print letters
char_list : list[str] = [chr(i) for i in range(65,91)]
print('char_list', char_list)   # get letter-list from A to Z

# old method 
print("\nOld way : check D is present in the list")
names1: list[str] = [chr(i) for i in range(65,91)]

for i in range(len(names1)):
    print(i, names1[i])
    if names1[i] == "D":  
        print("True")   # True
        break

# New Method
print("\nnew way : check D is present in the list")
names2: list[str] = [chr(i) for i in range(65,91)]
names2 = "D" in names2   
print('names2', names2)   # True

names3: list[str] = [chr(i) for i in range(65,91)]
names3 = "Pakistan" in names3 
print('names3', names3)   # False

names4: list[str] = [chr(i) for i in range(65,91)]
names4 = "D" not in names4   
print('names4', names4)   # Flase

print("\n'Zia', 'Qasim', 'Akbar' ")
names : list[str] = ['Zia', 'Qasim', 'Akbar']
uinput : str = input("Enter your name\t")

print("Only list people are allow")
print("Entered name is :- 'in' list return true otherwise flase")
names_in = uinput in names
print(names_in)

print("Block all the people in the list")
print("Entered name is :- 'not in' list return true otherwise flase")
names_notin = uinput not in names
print('names_notin', names_notin)

# Operator Precedence
print("\nOperator Precedence")
print("PEMDAS :- (solving order:- () , ** , * , / , + ,  -  )")

universe_age: int  = 14_000_000_000
print(universe_age)  # 14000000000

# unzip
print("\nunzip")
#0  1    2     0        1   2
a , b  , c  = 'qasim', 7, 3.0   # automatically become typle

print(a)    # qasim
print(b)    # 7 
print(c)    # 3.0

print("old difficult way")
data = ('qasim', 7, 3.0)
print(data[0], data[1], data[2])  # qasim 7 3.0

print("easy new way")
data = ('qasim', 7, 3.0)
print(*data)   # qasim 7 3.0

print("2 * 3, it performs multiplication\t", 2*3)  # 6
print('"a" * 3, it performs string repetition\t' , "a"*3)  # aaa

# Walrus Operator ( := )
# where you want to both use a value in an expression and assign it to a variable for later use.
print('\n Verify the input')
a : int = 10
if( a < (b := a+5 )):
    print(b)
else:
    print('else is working a<b')

if( a > (b := a+5 )):
    print(b)
else:
    print('else is working a>b')

# import this   # The Zen of Python



