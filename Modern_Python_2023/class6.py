print('if-else-elif, tuple, zip (chapter 5)\n')
from typing import Union, Optional

# if else are control block 

# 1) if  2) if-else 3) if-elif-else (only one true logic run)
# *)  if (if run when logic is true),   if-else (else run when logic is false),  if-elif-else (only one logic runs)
# if logic:
#   True-block
# else:
#    False-block

# comprehensive if-else :-   True-block if logic else False-block
# map(), filer()
# ======================== #

# comparison operator :-  ==   >=   <=   !=
# logical operator :-   and    or    not
# Union :- can use multiple data-types e.g. Union[int, float, str]
# from typing import Union, Optional
# note :- Optional by default is null
# Errors :-  1) Syntax Errors  (2) Runtime Errors (Exceptions) (3) Logical Errors:
# To protect from Logical Error : percentage >= 0  and percentage <= 50
# float : can take both 88.3 and 88 , we use float in percetage
# int : give error if we put 88.3
# input() return str :- Restrict User Input (type casting) e.g. float(input('percentage'))
# Zip combine elements from two or more iterables (same length) into tuples (list-of-tuples)
#(zip:- generator function, {iteration perform --> list , for-loop} )
# sorted has parameter key, key require function, we give lambda function


 
# ======================== #

# 1)  if (if run when logic is true)
print('if (if run when logic is true)')
if True:
    print('Python! Easy To Learn')

print('Python! beginner-friendly')
print('Python! easy to understand and use')

if False:
    print('Python! Easy To Learn')

print('Python! beginner-friendly')
print('Python! easy to understand and use')



# 2) if-else 
print('\nif-else (if/else run when logic is true)')
if True:
    print('Lost time is never found again')
else:
    print('''Time is limited, so don't waste it ''')

if False:
    print('Lost time is never found again')
else:
    print('''Time is limited, so don't waste it ''')

# comprehensive if-else 
print('\ncomprehensive if-else :- True-block if logic else False-block')
#        True-block                  logic              Flase-block
print('Time is most valuable thing') if True else print('Time waits for no one...')

print('Time is most valuable thing') if False else print('Time waits for no one...')

# 3) if-elif-else (only one true logic run) (multi logic)

print('\nif-elif-else (only one true logic run) (multi logic)')

# chain1 run only one block 
if True:
    print("True_block")
elif False:
    print("elif logic1")
elif False:
    print("elif logic2")
elif True:
    print("elif logic3")
else:
    print("final else block")

# chain2 run only one block 
if False:
    print("True_block")
elif False:
    print("elif logic1")
elif True:
    print("elif logic2")
elif True:
    print("elif logic3")
else:
    print("final else block")


# chain3 run only one block 
if False:
    print("True_block")
elif False:
    print("elif logic1")
elif False:
    print("elif logic2")
elif False:
    print("elif logic3")
else:
    print("final else block")


# Union :- can use multiple data-types e.g. Union[int, float, str]
print('\nUnion :- can use multiple data-types')

# from typing import Union, Optional
# note : Optional by default is null

print('\nCalculate Grade')
percentage : Union[int,float] = int(input('Enter Percentage\t'))
grade : Optional[str] = None
# percentage : int | float  # alternate of union
# grade : Union[str, None] = None

if percentage >= 70:
    grade = 'A'
elif percentage >= 60:
    grade = 'B'
elif percentage >= 50:
    grade = 'C'
elif percentage >= 40:
    grade = 'D'
else:
    grade = 'Fail'

print(f'Percentage is {percentage}, Calculated Grade is {grade} ')
# print :- Percentage is 88, Calculated Grade is A 

# Logical Error : 88 >= 0 condion Ture, when every get true (code come-out from block)
# percentage : int | float  # alternate of union
# grade : Union[str, None] = None

print('\nCalculate Grade (Logical Error)')
percentage : Union[int,float] = int(input('Enter Percentage\t'))
grade : Optional[str] = None

if percentage >= 0:
    grade = 'Fail'
elif percentage >= 50:
    grade = 'C'
elif percentage >= 60:
    grade = 'B'
elif percentage >= 70:
    grade = 'A'
else:
    grade = 'A+'

print(f'Percentage is {percentage}, Calculated Grade is {grade} ')

# print :- Percentage is 88, Calculated Grade is Fail (logical error)

# To protect from Logical Error : percentage >= 0  and percentage <= 50
# float : can take 88.3 and 88 , we use float in percetage
# int : give error if we put 88.3

print('\nResolve (Logical Error)  (variable >= 0)  and (variable < 50) ')
per : Union[int,float] = float(input('Enter Percentage\t'))
grade : Optional[str] = None

if (per >= 0) and (per < 50):
    grade = 'Fail'
elif (per >= 50) and (per < 60):
    grade = 'C'
elif (per >= 60) and (per < 70):
    grade = 'B'
elif (per >= 70) and (per <= 100):
    grade = 'A'

print(f'Percentage is {percentage}, Calculated Grade is {grade} ')

