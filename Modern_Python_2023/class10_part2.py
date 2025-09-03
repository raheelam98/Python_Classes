# unlimited arguments (*) return tuples
# positional argument, position is important
# pass unlimited key words arguments ( ** ) return dictionary

# pass unlimited arguments (single * tuples) (time 1:20) (example 37)

from typing import Tuple, Dict

print('\nunlimited arguments (*) return tuples')
def unlimited_arguments1(*nums):    # single * tuple
    print(nums, type(nums))

# traditional method
    total = 0
    for n in nums:
        total += n
    return total
    
unlimited_arguments1(1,2,3,4,5,6)   # call function
# output :- (1, 2, 3, 4, 5, 6) <class 'tuple'>

# greeting function (unlimited arguments )
print('\npass str with unlimited arguments (...  dynamic length)  ')
def greet(*names: Tuple[str, ...]) -> None:
    ''' Function Greet all person in the  tuple (name)  '''

    for i in names:
        print(f'Hello {i}')

greet("Akbar", "Jamal", "Bushra")   # call function
# output :- Hello Akbar  Hello Jamal  Hello Bushra

# parametric function  # old way
def addnum1(num1:int, num2:int) -> int:
    #num1 + num2  # error
    return num1 + num2
print(f'\ntraditional way : {addnum1(3,4)}')  # call function
# output :- traditional way : 7

# new way, # passing through positional argument
# first value goes in 1st and sendon value goes to 2nd position
print('\npositional argument, position is important ')
def add_two_num(num1:int, num2:int) -> int:
    print(f"num1 value {num1} and num2 value {num2}")
    return num1 + num2
print(f'positional argument {add_two_num(3,4)}')   # call function
# output :- positional argument 7

# key word arguments (get it from name, not need to predefine)
print('\nkey word argument, value get it by name ')
def add_two_num(num1:int, num2:int) -> int:
    print(f'num1 value {num1} and num2 value {num2}')
    return num1 + num2
print(f'key word arguments {add_two_num(num2=3, num1=2)}')  # call function

# pass unlimated key words arguments ( ** ) return dictionary (time 1:30)
# note:- we havn't pass any variable in function
print('\nunlimited keyword arguments (**) return dictionary ')
def unlimited_keyword_arguments(**karguments):    
    print(karguments, type(karguments))

unlimited_keyword_arguments(x=2, c=20, a='letter', name="Mike")   # call function
# output :- {'x': 2, 'c': 20, 'a': 'letter', 'name': 'Mike'} <class 'dict'>

# time 1:32 (43)
print('\nexample:- unlimited arugument / keywords')
print(f'required_variable (a), unlimited_comma_seprated_arguments(*), unlimited_keyword_arguments(**)')

def test_function(a, *unlimited_arguments, **unlimited_keyword):
    print(f''' required_any_variable {a},
          *unlimited_arguments  {unlimited_arguments},
          **unlimited_keyword  {unlimited_keyword}
          ''')
    
test_function(123, 6, 'tester', 1,2,3,4,5, e=3, checker=1, d='keyvalue', name='my_name')

print(f'\nexample: define type')

def test_function(a, b:int, c:str, *unlim_arg : Tuple[int,...] , **unlim_keyword : Dict[str,int]) -> None:
    print(f''' required_any_variable {a}, require_int {b}, require_str {c},
          *unlimited_arguments  {unlim_arg},
          **unlimited_keyword  {unlim_keyword}
          ''')
    
test_function(678, 7, 'test_type', 6,7,8,9,10, e=3, tester=1, d=40)

# typing not require
print('\nexample: typing is not require because * (tuple) , ** (dict)')
def my_function(a:int, b:int, *unlimit_arg:int, **unlimit_keyword: int) -> None:
    print(a,b, unlimit_arg, unlimit_keyword)

my_function(1,2, 7,9,9,9, c=20, d= 30, x=100)
# output :- 1 2 (7, 9, 9, 9) {'c': 20, 'd': 30, 'x': 100}


