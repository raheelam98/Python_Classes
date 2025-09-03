# functions
# https://realpython.com/primer-on-python-decorators/

# First-Class Objects
# In functional programming, you work almost entirely with pure functions 
# that don’t have side effects

def say_hello(name:str) -> None:
    return f"Hello {name}"

def be_awesome(name:str) -> None:
    return f"Yo {name}, awesome"

def greet_person(greeter_func) -> None:
    return greeter_func("Mike")

print(greet_person(say_hello))   # output : Hello Mike
print(greet_person(be_awesome)) # output : Yo Mike, awesome

# note :- say_hello function is named without parentheses. 
# say_hello:- This means that only a reference to the function is passed. The function isn’t executed.
# greet_person() with parentheses, so it will be called as usual.

# ============ Inner Functions ==============
# Inner Functions :-  define functions inside other functions.
# note :-  inner functions within the parent function

def parent1():
    print("Printing from partent()")

    def first_child1():
        print("Printing from first_child()")

    first_child1()

parent1() # output:- Printing from partent()   Printing from first_child()

# first_child() # NameError # inner functions aren’t defined until the parent function is called

# Functions as Return Values 

def parent2(num : int):
    def first_child2():
        return "First child is here"
    
    def seond_child2():
        return "Second child is here"
    
    if num == 1:
        return first_child2
    else:
        return seond_child2
    
print(parent2(2))  
# output :- <function parent2.<locals>.seond_child2 at 0x107b28f40>

# ============ Decorators ==============
# Decorators

def decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

def say_whee():
    print("Whee!")

say_whee = decorator(say_whee)
print(say_whee)

# output :- <function decorator.<locals>.wrapper at 0x107b28fe0>