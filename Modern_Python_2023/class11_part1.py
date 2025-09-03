print('Class 11 :- try-except-else-finally chain, call by reference and call by value')
print('call by reference and call by value\n')
# Mutable (changeable) :-  dict, list, set, class object (change these object effect the memory)
# Mutable (changeable):- pass by reference {can modify after creation,  e.g. append} (reference- 2 names)
# Mutable change in both local and global scop
# Immutable (can’t change) :- integer, float, string, tuples, bool (Boolean) ( can’t modify once created).
# Immutable (can’t change) :-  Any modification result a new object.
# Immutable make copy   ( pass by value or pass by copy) change perform in local scope of variable
# https://github.com/panaverse/learn-modern-python/blob/main/11_class(try-except)/class11.ipynb 

list_a : list[int] = [1,2,3]
list_b = list_a
list_a.append(4)
print('list_b :', list_b) # list_b : [1, 2, 3, 4]

num_a : int = 5
num_b = num_a
num_a += 1
print('num_b: ', num_b) # num_b:  5

# Addressing Changes without Function Calls
x = 10
print(f'Before modification: {x}, address {id(x)}')
x += 1
print(f'After modification: {x}, address {id(x)}')
# output: Before modification:10, address 4368207872
# output: After modification: 11, address 4552859680

print('\nImmutable (can’t change) integer, float, string, tuples')
print('pass by copy - Immutable - no change ')

my_int : int = 5    # mutable
print(f"original variable my_int value {my_int} and address {id(my_int)} ")

def int_fun(num1 : int) -> None:
    print(f"\tValue of start of function {num1} address {id(num1)} same (original) address")
    num1 = 6  #  it will change update object (pass by copy and put in num1)
    print(f"\tnum1 value end of function {num1} address {id(num1)} reassign -> change address")    # change hee

int_fun(my_int)     # pass by value imutable
print(f'original variable value is unchange {my_int} and address {id(my_int)} same (original) address')

#output:- original variable my_int value 5 and address 4419207008 
#output:-         Value of start of function 5 address 4419207008
#output:-         num1 value end of function 6 address 4419207040    (change only when num1 = 6)
#output:- original variable value is unchange 5 and address unchange 4419207008

# time 15
print('\nMutable (changeable) dict, list, set')
print('append list, pass by reference, mutable data_type\n')
my_list : list[int] = [1,2,3]
print(f"original variable my_int value {my_list} and address {id(my_list)} ") 

def list_fun(num1 : list[int]) -> None:
    print(f"\tValue of start of function {num1} address {id(num1)}")
    num1.append(200)    # added on element
    print(f'\tnum1 value is {num1} and address {id(num1)} add element-> same address')

list_fun(my_list)
print(f'original variable value is change {my_list} and address {id(my_list)}')

#output:-        Value of start of function [1, 2, 3] address 4454338624
#output:-        num1 value is [1, 2, 3, 200] and address 4454338624
#output:- original variable value is change [1, 2, 3, 200] and address unchange 4310831168

# time 20
print('\npass by copy of the reference - mutable ')
ori_list : list[int] = [1,2,3]
print(f"original variable my_int value {ori_list} and address {id(ori_list)} ") 

def list_fun(num1 : list[int]) -> None:
    print(f"\tValue of start of function {num1} address {id(num1)}")
    num1: list[int]  = [7]  # reassign list variable -> create new object
    print(f'\tnum1 value is {num1} and address {id(num1)}, reassign -> create 2nd object')
    num1.append(300)        # added on element
    print(f'\tnum1 value is {num1} and address {id(num1)}, add element -> 2nd object  ') 

list_fun(ori_list)  # pass by refference (mutable data type)   # second object
print(f'original variable value unchange {ori_list} and address {id(ori_list)} 1st object')

#output:- original variable my_int value [1, 2, 3] and address 4326883008 
#output:-        Value of start of function [1, 2, 3] address 4326883008
#output:-        num1 value is [7, 300] and address 4326883136 2nd object
#output:- original variable value unchange [1, 2, 3] and address unchange 4326883008 1st object

print('\nmutable')
a : list[int] = [1,2,3,4]
print(f"value of a is {a} & address {id(a)}, original")

def abc(num1:list[int])->None:
    print(f"before:- num1 value is {num1} & address {id(num1)}")
    num1:list[int] = [1,2,3,4] # reassign list variable -> create new object
    print(f"after:-  num1 value is {num1} & address {id(num1)} reassign -> create new object ")
    num1.append(200)# added on element
    print(f"value of num1 is {num1} & address {id(num1)} , add element -> same address")

abc(a)# pass by refference (mutable data type)
print(f"value of a is {a} & address {id(a)}, original")

# time 38
print('\n1)immutable int : same thing with different name has same address')
print('2)immutable int : reassign -> create new object')
x: int = 7  # immutable
b = x
c = 7

print(f'value of x is {x} and address {id(x)}, x: int = 7')
print(f'value of b is {b} and address {id(b)}, b = x')
print(f'value of c is {c} and address {id(c)}, c = 7')

b : int = int(7)
print(f'value of b is {b} and address {id(b)} no change by same casting')

b = 100 # update value of b, create new object and change the value
# old object is remain same the new object save in the memory
print(f'value of b is {b} and address {id(b)}  Reassign -> change address')

print('\nRM ================================\n')

print('Immutable (can’t change) integer, float, string, tuples')
print('pass by copy - Immutable - not change ')

my_int : int = 5    # mutable
print(f"original variable my_int value {my_int} and address {id(my_int)} ")

def int_fun(num1 : int) -> None:
    print(f"\tValue of start of function {num1} address {id(num1)} same (original) address")

    num1 = 6  #  it will change update object (pass by copy and put in num1)
    print(f"\tnum1 value end of function {num1} address {id(num1)} reassign -> create new object (new address)")    
   
    x = num1
    print(f"\tchange variable name 'x' of fun {x} address {id(x)} change name ->  same (original) address")     


int_fun(my_int)     # pass by value imutable
print(f'original variable value is unchange {my_int} and address {id(my_int)} same (original) address')

#output:- original variable my_int value 5 and address 4419207008 
#output:-         Value of start of function 5 address 4419207008
#output:-         num1 value end of function 6 address 4419207040    (change only when num1 = 6)
#output:- original variable value is unchange 5 and address unchange 4419207008

print('\nMutable (changeable) dict, list, set')
print('pass by reference, mutable data_type ')
print('Mutable (changeable) add, delete, (memory address same) ')
my_list : list[int] = [1,2,3]
print(f"original variable my_int value {my_list} and address {id(my_list)} ") 

def list_fun(num1 : list[int]) -> None:
    print(f"\tValue of start of function {num1} address {id(num1)}")
    num1.append(100)    # added on element
    print(f'\tappend:-   num1 value is {num1} and address {id(num1)} add element-> same (original) address')
    x = num1
    print(f"\tchange variable name 'x' of fun {x} address {id(x)} change name ->  same (original) address")     

    num1:list[int] = [1,2,3,4] # reassign list variable -> create new object
    print(f"\n\treassign:- num1 value is {num1} & address {id(num1)} reassign -> create new object (new address) ")
    num1.append(200)# added on element
    print(f"\tappend:-   num1  value is {num1} & address {id(num1)}  add element in new object ")

list_fun(my_list)
print(f'\noriginal variable value is change {my_list} and address {id(my_list)} same (original) address')
