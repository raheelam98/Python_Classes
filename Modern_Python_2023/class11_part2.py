print("Error Handle 1)syntex (development time) 2)run time error  3)logical error\n")

# 1)syntex error (development time) 2)run time error (solve by tesing)  3)logical error

# Error 1 :- ZeroDivisionError: division by zero (if use zero) user mistake
# Error 2 :- IndexError: list index out of range
# Error 3 :- TypeError: unsupported operand type(s) for +: 'int' and 'str'
# Error 4 :- KeyError: 'father name'  (father name is not key)  crash server
# Error 5 :- FileNotFoundError: 
# Error 6 :-  NameError: name is not defined # print(xyz)
# Handle Run time error :- 
# try:
#     logic
# except (Error_class1, Error_class2):
#     if error accured then run this block 
# else:
#     if error not accured
# finally:
#     always run


print("Runtime error")

num1 : int = int(input("Enter number1 :\t"))
num2 : int = int(input("Enter number1 :\t"))

print(f'Divide {num1/num2}')

# Error1 :- ZeroDivisionError: division by zero (if use zero) user mistake

names : list[str] = ['Ali', 'Akbar', 'Mike']

index1 : int = int(input('Enter index number and get name : '))
#print(f'Name is {names(index1)}')  error [index]
print(f'Name is {names[0]}')
# if user input is 10 : IndexError: list index out of range

# Error 2 :- IndexError: list index out of range (wrong index number) user mistake

data_tuple : tuple[int,int,int] = (1,2,3)
print(f'tuple index are: {data_tuple[0]}, {data_tuple[1]}, {data_tuple[2]} ')
# print(data_tuple[20]) # IndexError: tuple index out of range

# Error 3:- TypeError: unsupported operand type(s) for +: 'int' and 'str'
#2 + "2"  TypeError: unsupported operand type(s) for +: 'int' and 'str'


# Error 4 :- KeyError:(Surver crash) insert wrong value
data_dict : dict[str,str] = {
    'name' : 'Raheela',
    'Education' : 'MSc'
}
print(f'Name is {data_dict['name']} and Education is {data_dict['Education']} ')
# print(data_dict['father name']) KeyError: 'father name'

# Error 5 :- FileNotFoundError: 
# open('fileName1.txt') FileNotFoundError: 

print('\nHandle Run time error')  # time 1: 02

print('\nZeroDivisionError')
# 5/0 ZeroDivisionError: division by zero
print('5/2:- ', 5/2)
try:
    print(f'5/0:-', 5/0 ) # Error 
except (ZeroDivisionError):
    print('ZeroDivisionError')
print("logic4")

print('\nIndexError')
#print(my_list[undefine_index]) # IndexError: list index out of range

my_list : list[int] = [1,2,3]
print(f'list[0]:-  {my_list[0]}')
#print(my_list[10]) # IndexError: list index out of range
try:
    print(f'list[10]:- {my_list[10]}')
except (IndexError):
    print('IndexError: list index out of range')
print(f'list[1]:- {my_list[1]}')

print('\nMultiple error: after getting 1st error goes to except block, logic underneath cannot run ')

my_list : list[int] = [1,2,3]
print(f'list[0]:-  {my_list[1]}')
#print(my_list[10]) # IndexError: list index out of range
try:
    print(f'5/0:-', 5/0 ) # Error 
    print(f'list[10]: {my_list[10]}') # error
    #print(f'{xyz}, NameError: name is not defined')
except (ZeroDivisionError, IndexError, NameError):
     print(f'5/0:- ZeroDivisionError')
     print(f'list[10]:- IndexError: list index out of range')
print(f'list[1]:- {my_list[2]}')

#print(f'{xyz}')  NameError: name 'xyz' is not defined

print('\nRM ================================\n')
# How to Catch Multiple Exceptions in Python
# https://realpython.com/python-catch-multiple-exceptions/

# try:
#     first = float(input("What is your first number? "))
#     second = float(input("What is your second number? "))
#     print(f"{first} divided by {second} is {first / second}")
# except ValueError:
#     print("You must enter a number")
# except ZeroDivisionError:
#     print("You can't divide by zero")
# except (ValueError, ZeroDivisionError) as error:
#     print(f"A {type(error).__name__} has occurred.")


# exception_identification_with_structural_pattern_matching.py

from operator import mul, truediv

def calculate(operator, operand1, operand2):
    return operator(operand1, operand2)

try:
    first = float(input("What is your first number? "))
    second = float(input("What is your second number? "))
    operation = input("Enter either * or /: ")
    if operation == "*":
        answer = calculate(mul, first, second)
    elif operation == "/":
        answer = calculate(truediv, first, second)
    else:
        raise RuntimeError(f"'{operation}' is an unsupported operation")
except (RuntimeError, ValueError, ZeroDivisionError) as error:
    print(f"A {type(error).__name__} has occurred")   # tell the type or error
    match error:
        case RuntimeError():
            print(f"You have entered an invalid symbol: {error}")  # & error
        case ValueError():
            print(f"You have not entered a number: {error}") # ee  error
        case ZeroDivisionError():
            print(f"You can't divide by zero: {error}")   # first/0 error
else:
    print(f"{first} {operation} {second} = {answer}")







