# decorators function ,(1:45) allows a user to add new functionality to an 
# existing object without modifying its structure
# use of decorator fun:- pass url page in decorator convert into html and then display
# recursive function calls itself (e.g image reflection in front and back mirror)
# recursion is infinite so we have to break it

from typing import Callable
from typing import Tuple, Dict 

def my_decorator(fun) -> None:
    def wrapper():
        print('before fun call')
        fun()
        print('after fun call')
    return wrapper

@my_decorator
def checker() -> None:
    print('calling checker fun')
checker()

print('\ndecorator')
#def fun_decorator(func : Callable([],None)) -> Callable[[],None]:
    #def wrapper() -> None:
def fun_decorator(func: Callable[[], None]) -> Callable[[], None]:
    def wrapper():
        print(f'Something happen before function is call')
        func()
        print(f'Something happen after function is call')
    return wrapper

@fun_decorator
def say_hello() -> None:
    print('Hello')

say_hello()

print('\ndecorator fun with int')

def int_decorator(fun : Callable[[int], None]) -> Callable[[int], None]:
    def wrapper(num : int)-> None :
        print("Something is happening before the function is called.")
        fun(num)
        print("Something is happening after the function is called.")
    return wrapper

def int_fun(num:int) -> None:
    print(num)
int_fun(45)

print('\nrecursive function calls itself, have to break it')
def factorial(x : int) -> int:
    '''Recursive funion is use to find factorial of an integer'''

    if x == 1:
        return 1
    else:
        return (x * factorial(x-1))
num = 5
print(f'The foctorial of {num}, is {factorial(num)}')
    
print('\n 5! = 5*4*3*2*1 = 120')  