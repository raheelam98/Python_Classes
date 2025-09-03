#decorators modify the behavior of a function/method without touching its code
# when
# why

# ============ Decorators ==============

# def decorator_fun(func):
#     def wrapper():
#         print("before")
#         func()
#         print("after")
#     return wrapper

# @decorator_fun
# def say_whee():
#     print("decorator function say whee!")

# f1 = decorator_fun(say_whee)
# print(f1)

# Create a decorator
def sample_decorator(func):
    # define the inner function 
    def example_function(number):
        print("Before Fun Call:", func.__name__)
        
        # call original function
        results = func(number)
        print("Cube: ", results)
     
        print("After Fun Call:", func.__name__)
    # Return inner function
    return example_function

def cube(num):
    return num**3

# decorate the function
decorated_func = sample_decorator(cube)

# call the decorated function
decorated_func(2)

# ==========
print("\nexample 2")
def sample_decorator2(func):
    def example_function(number):
        print("Before Funciton Call:", func.__name__)
        results = func(number)
        print(results)
        print("After Funciton Call:", func.__name__)
    return example_function

@sample_decorator2
def cube(num):
    return num**3

cube(3)

