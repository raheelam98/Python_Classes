print("list tuple and list comprehensive, range (chapter 5)")

#for item in items_list:
#    loop_body
# Comprehensive Style :- [loop_body for item in items_list] (: not needed)
# 0R :- [expression for item in iterable if condition]
# Error :- unnecessary indentation (even not single space), function: (single colon)

# for...else, if...else, while...else
# else :- else block will not be executed if the loop is terminated by a break
#  else block is executed when the for/while loop completes its iteration without encountering a break
# else block is executed when the condition in the if statement is False.
# else: part of the block

# perform optations by using tuples
# tuple :- immutable {constant} (can't add, remove and update), support slicing 

# python loop:-  last iterated item can use out-side of loop (book)
# enumerate :- iterate over a sequence and returns tuple with index and the corresponding element.
# string.title() :- first letter of each word is capital
# input():- return string 
# for value in list: (new way)

names : list[str] = ['Bushra', 'Raheela ' 'Mahmood']

for name in names:
    print(name)
# Bushra
# Raheela Mahmood

for name in names:
    print(f"Hi! Welcome on board {name.title()}")
    print("AI Champion\n")    # in the loop

print("Win The Race")     # print only one time becuse out of loop

print('\nExtract select values from list through loop (use slice:- variable_names[start:end:step])')
numbers_list : list[str] = ['One', 'tWo', 'tHree', 'fouR', 'fiVe', 'Six']

for value in numbers_list  [:2]:  
    print('[:2] ', value.upper())   # print:- ONE TWO

#names2 : list[str] = ['one', 'two', 'three', 'four', 'five', 'Six']
for value in numbers_list  [:-2] :
    print('[:-2] ',value.title())       # print:-  One  Two  Three  Four
# note :- title() method of string --> convert the first character of each word in a string to uppercase and the rest of the characters to lowercase

# perform optations by using tuples
print(''' \ntuple :- immutable (can't add, remove and update), support slicing ''' )

data_base : list[tuple[str,str]] = [
                                        ('Akbar', '123'),
                                        ('Lal', '345')
                                    ]

for row in data_base:
    print(row)

# zip
print('\nExtracting value from tuple, one by one and put in separate variable ')
data_base : list[tuple[str,str]] = [
                                        ('Akbar', '123'),
                                        ('Mike', '456')
                                    ]

for row in data_base:
    user, password = row    # extract value from tuple one by one put in separate variable 
    print(user,password)

# for...else, if...else, while...else
print('\nelse block')
names : list[str] = ['Bushra', 'Raheela']

for name in names:
    print(name)             # Bushra  Raheela
else:
    print('Champion of AI\n')  # Champion of AI

# else:  else block will not be executed if the loop is terminated by a break
for name in names:
    print(name)     # Bushra  Raheela
    break
else:
    print('Champion of AI 2\n')   # not run because of break

# python loop:-  last iterated item can use out-side of loop (book)
print('\npython loop:-  last iterated item can use out-side of loop, here carolina')
magicians : list[str] = ['alice', 'david', 'carolina']

for magician in magicians:
    print(f"{magician.title()}, that was a great trick! ")
print(f"I can't wait to see your next trick, {magician.title()}")

# enumerate :- iterate over a sequence and returns tuple with index and the corresponding element.

print('\nenumerate, iterate over a sequence and returns tuple with index and the corresponding element')
print(list(enumerate(magicians)))   # [(0, 'alice'), (1, 'david'), (2, 'carolina')]

print('\nunzip')
for index, name in enumerate(magicians):
    print(index,name)       # 0 alice   1 david   2 carolina

print('\nNumbers with loop')
print('range(start,end,step):- generates a sequence of numbers')
print('range function can\'t run directly (run with list) need iterator e.g list') 
print('range(n):- sinale-value, start=0, end n-1')

#range(0,10)
print('\nrange(end), end n-1, note start default-value 0 ')
print(list(range(10)))  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print('\nrange(start,end), sart from 3 and end 8-1=7 ')
print(list(range(3,8)))  # [3, 4, 5, 6, 7]

print('\nrange(start,end,step), Sequence of 2')
print(list(range(2, 21, 2)))    # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# for loop is doing iteration so we don't need iteration of range
for n in range(2,21,2):
    print(n)

print('\nTable of 2 by using for-loop and range')

for n in range(1,11):
    print(f"{2} x {n} = {n*2}")

# old way
squares : list[int] = []

print('indentation one')
for value in range(1,5):
    square = value ** 2
    squares.append(square)
    print('indentation one ', squares)

print('indentation two')
squares:list[int] = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)
print('indentation two', squares)

print('\nOld Style')
print(list(range(2,5)))   # [2, 3, 4]

for n in range(2,5):
    print(n**2)         # 4   9  16  

# Comprehensive Style :- [loop_body for item in items_list]  (: not needed)
# benefit of list comprehensive
print('\nComprehensive Style :- [loop_body for item in items_list]')

print([n**2 for n in range(2,11)])  # [4, 9, 16, 25, 36, 49, 64, 81, 100]

digit : list[int] = [0,1,2,3,4,5,6,7,8,9]

print(max(digit))   # 9
print(min(digit))   # 0
print(sum(digit))   # 45

# shallow and deep copy (slicing result is deep copy)
# slicing make indiual copy if change in any element doesn't effect on main list ??
my_foods = ['pizza', 'falafel', 'carrot cake'] 
friend_foods = my_foods[:] # deep copy

print('before      ', my_foods)     # ['pizza', 'falafel', 'carrot cake']
print('before      ', friend_foods) # ['pizza', 'falafel', 'carrot cake']

friend_foods[0] = "Tikka"

print('after        ',my_foods)     # ['pizza', 'falafel', 'carrot cake'
print('after update ',friend_foods) # ['Tikka', 'falafel', 'carrot cake']

# tuple :- immutable {constant} (can't add, remove and update), support slicing
print('\ntuple :- immutable {constant} (can\'t add, remove and update), support slicing')

names:tuple[str] = ('A',"B",'C')
print(names[0])
print(names[0:2])

# tuple :- re_assign then change
print('1- tuple can re_assign then change')
names:tuple[str] = ('Pakistan',"B",'C')     # ('Pakistan', 'B', 'C')
print(names)

from typing import Any

data : tuple[Any] = ("A", [1,2,3], True)
print(data)     # ('A', [1, 2, 3], True)

# tuple never update but the object in the tuple (e.g list) can update

print(data[1])      # [1, 2, 3]
data[1].append(20)
print(data)         # ('A', [1, 2, 3, 20], True)

# ======= class questions
my_input = input("abc")
print(type(my_input))
print(my_input)

print(sorted([17,8,3])) 



