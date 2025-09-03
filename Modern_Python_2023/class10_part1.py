# https://stackoverflow.com/questions/33833881/is-it-possible-to-type-hint-a-lambda-function
# functions, lambda, decorators, recursive, generator, *arg and **args
# functon declaration:- def function_name(param1:type, param2:type,...)->Return_type:   
#     function_body                                                        
# call function:- function_name(arg1,arg2)
# =======================================
# lambda function (1) one line function (2) without name (3)only use in this line
# lambda param1,param2 : function_body
# use for micro work, use memory only for short period 
# lambda type :-  from typing import Callable  (use cllable for type of lamda fun)
# lambdafun : Callable[[int,int],int] = lambda x,y: x+y
# =======================================
# print in non-return function
# check fun is returnable or non_return 
# assign in variable and then print
# method:- variable_name.method()
# ======================================
# https://stackoverflow.com/questions/74774919/proper-typing-for-a-interesting-yield-function
# Generator Function:-  1) iterate on element one by one (time 57)
# Generator Function:-  2) stop after each iteration
# Generator Function:-  3) remember old iteration value (last iterate value)
# Generator Function:-  4) next iterate - go forward from last iterate value
# def function_name():
#    yield statement 
#  generator expression:- expression for item in iterable)
# Aim :- lot of data, iterate one element then perform opration accordingly, it cale less space in memory

# ======================================

from typing import Callable

checkfun1 : str = print('print non_return_function')

checkfun2 : str = print(len('len return_function'))

# default function:- function without arguments
def defultfun() -> None:
    print("Master in Python")
    print("Call anywhere anytime")
defultfun()

# parametric function
def addnum1(num1:int, num2:int) -> int:
    #num1 + num2  # error
    return num1 + num2
print(addnum1(3,4))

# parametric function with default value 'here 6)
def addnum2(num1:int, num2:int = 6) -> int:
    #num1 + num2
    #num = num1 + num2 #  error : none
    return num1 + num2
print(f'fun default value {addnum2(3,4)}')
print(f'fun with default value {addnum2(4)}')

#lambda function :- lambda param1,param2 : function_body
# lambda num1 : int, num2 : int : num1 + num2   error
addnum : int = lambda num1, num2 : num1 + num2
print(f'lambda fun {addnum(2,3)}')  # lambda fun 5

lambdafun : Callable[[int,int],int] = lambda x,y: x+y
print(f'lambda fun with type {lambdafun(5,2)}')  # lambda fun with type 7

# Generator Function
def my_range(start:int, end:int, step: int=1):
    for i in range(start,end+1,step):
        yield i # Generator function

get_range = my_range(1,6)
print(f'detail  {get_range}')       #  <generator object my_range at 0x10c5295d0>
print(f'generator {list(get_range)}') #  [1, 2, 3, 4, 5, 6]

a = my_range(1,6)
print(next(a))      # 1
print(next(a))      # 2
print('Pakistan')   # Pakistan
print(next(a))      # 3
print(type(a))      # <class 'generator'>

# generator type 
from collections.abc import Iterator

MyDictT = dict[str, object] 

def yield_fun() -> Iterator[MyDictT]:
    a: MyDictT = {}
    b: MyDictT = {}
    yield a
    yield b
print(f' {MyDictT}')  # dict[str, object]
print(f'type {type(MyDictT)}')  # type <class 'types.GenericAlias'>

def type_range1(start:int, end:int, step: int=1) -> Iterator[int]:
    for i in range(start, end+1, step):
        yield i # Generator function

Iterator_variable = type_range1(3,8)

print(next(Iterator_variable))  # 3
print(next(Iterator_variable))  # 4
print(type(Iterator_variable))  # <class 'generator'>

for i in Iterator_variable:
    print(i)

print(dir(Iterator_variable)) # 5, 6, 7, 8

# generator function break large data in small pices like queue(time 1:20)

data : list[int] = filter(lambda x:x%2 == 0, range(1,30) )
print(next(data)) # 2
print(next(data)) # 4






