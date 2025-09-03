
print("list, indexing, slicing and list methods/attributes \n")
# Python, dynamically-typed language :- type of the variable is determined only during runtime.
# Python, strongly typed :- 
# immutable :- int, float, str, tuple, frozen set
# mutable objects :-  Lists, dictionaries, and sets
# List comprehension :-  [i for i in dir(list) if "__" not in i]
#  ( if "_ _" not in i. The result is a list containing names without double underscores.)
# List :- dynamic length (any length)
# List (any):-  hetrogenous data types (Multiple type)
# index :-  (#1) postive 0 to n-1 , (#2) negative -1 to length
# slicing :- variable_names[start:end:step]  (extract more than 2 or more elements, default slicing from left to right)
# slicing :-  start : int = include (Default 0),  end : int = n-1, step : int = sequence (Default 1) (step of the slicing)
# Note slicing :- if we don't put any value (its means everything included)
# string is iterative data-type we can perform iteration  str['abcde']
# print() :- no-return function (implicitly returns None) (value don't go to variable)
# id() :- return function (value goes to variable) (store the value)
# call help :-  help(object)  object?   object??   ?object  ??object

# Shallow copy :- change every where e.g. list2 = list1 
# Deep copy :- change only in particular item e.g list2 = list1.copy() 

# list_of_items (good name)

from typing import Any

# default slicing is from left to right :
# variable_names[start:end:step]
# slicing :-  start : int = include (Default 0),  end : int = n-1, step : int = sequance (Default 1) (step of the slicing)
# class4_slice1.py (detail)

# ->                    0        1         2
names : list[str] = ["Qasim","Sir Zia", "Sir Inam", 20, True]
# <-                    -5      -4          -3       -2   -1
print("List :- ", names)

print('\nlist methods/attributes \n')

# print() :- no-return function (implicitly returns None) (value don't go to variable)
return_nothing : str = print("Print message") # Print message
print("print function, return_nothing :- ",return_nothing)  # None

return_nothing2 : str = print(type(names)) # Print Return-nothing
print("type funtion, return_nothing :- ",return_nothing2)  # None

# id() :- return function (value goes to variable)
return_value : str = id(names)
print("id funtion, return_value :- ", return_value)  # 4477433856

# mutable objects (can update) :-  Lists, dictionaries, and sets 

methods_list : str = [i for i in dir(list) if "__" not in i]
print(methods_list)
# ['append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']

# list over-write can declar again
# ->                    0        1         2
names : list[Any] = ["Qasim","Zia", "Imran", 20, True]
# <-                                    -3   -2   -1

print(names[0]) # Qasim
names[0] = "Muhammad Qasim"
print(names)  # ['Muhammad Qasim', 'Zia', 'Imran', 20, True]

# deleted element is not store any where
del names[3] # delete :-  20    note we can't put in variable
print(names)  # ['Muhammad Qasim', 'Zia', 'Imran', True]

remove_lastelement : list[str] = names.pop()
print("pop return-method :- ",remove_lastelement)   # remove :- True  (return-method)
print("pop remove last item :- ",names)  # ['Muhammad Qasim', 'Zia', 'Imran']

add_element_end : list[str] = names.append("Akbar")
print(add_element_end)   # None
print("append add element at end :- ",names) # ['Muhammad Qasim', 'Zia', 'Imran', 'Akbar']

#insert_anywhere : list[str] = names2.insert(2,"Raheela")
names.insert(2,"Raheela")
print("insert on perticular postion :- ", names) # ['Muhammad Qasim', 'Zia', 'Raheela', 'Imran', 'Akbar']

print("\nShallow copy :- change every where e.g. list2 = list1 ")
list1 : list[str] = ['a', 'b', 'c']
list2 = list1  # shallow copy
print(list1)    # ['a', 'b', 'c']
print(list2)    # ['a', 'b', 'c']

list2[0] = 'Pakistan'    # change only b variable but both variable updated
print("auto updated ",list1)  # auto update ['Pakistan', 'b', 'c'] (but element auto added b/c list1 = list2)
print("update element 0",list2)  # update element 0 ['Pakistan', 'b', 'c']

print("\nDeep copy :- change only in particular item e.g list2 = list1.copy()")
list1 : list[str] = ['a', 'b', 'c']
list2 = list1.copy()    # Deep copy
print("list1 before ", list1)  # list1 before  ['a', 'b', 'c']
print("list2 before ", list2)  # list2 before  ['a', 'b', 'c']

list2[0] = 'Pakistan'
print("list1 after ", list1)  # list1 after ['a', 'b', 'c']
print("list2 after update ", list2) # list2 after update  ['Pakistan', 'b', 'c']


original_list : list[str] = ['Ali', 'Akbar']
new_list : list[str] = ['Asma','Rana' ]
original_list.append(new_list)  # 
print('append',original_list)   # append ['Ali', 'Akbar', ['Asma', 'Rana']]
#original_list.extend(new_list)   #  add elements of the list at the end  
#print(original_list)  # ['Ali', 'Akbar', ['Asma', 'Rana'], 'Asma', 'Rana']
# multiple add  (use extend)
original_list : list[str] = ['Ali', 'Akbar']
new_list : list[str] = ['Asma','Rana' ]
original_list.extend(new_list) # add elements at the end one by one 
print('extend',original_list)  # extend ['Ali', 'Akbar', 'Asma', 'Rana']

original_list : list[str] = ['Ali', 'Akbar', 'Mike']
remove_particular_text = original_list.remove('Akbar') # remove by text with value
print('remove',original_list)    # ['Ali', 'Mike']

# search element by text  (return 1st occurrence)
original_list : list[str] = ['Ali', 'Akbar', 'Mike', 'Akbar']
print(original_list.index('Akbar'))  # 1

# reverse/sort:- in-memory (change the real data)
#data_list : list[str] = list["ABCDEF"]  # error passing as string 

data_list : list[str] = list("ABCFDEF")
print('before ', data_list )    # ['A', 'B', 'C', 'F', 'D', 'E', 'F']
data_list.reverse()
print('reverse ', data_list)    #  ['F', 'E', 'D', 'F', 'C', 'B', 'A']

data_list.sort()    # sort:- in-memory (change the real data)
print('sort ', data_list)   # ['A', 'B', 'C', 'D', 'E', 'F', 'F']

data_list : list[str] = list("ABECDEDF")
print('before ', data_list )    # ['A', 'B', 'E', 'C', 'D', 'E', 'D', 'F']
data_list.sort(reverse=True)    # desendeing order
print('sort(reverse=True)',data_list)   # ['F', 'E', 'E', 'D', 'D', 'C', 'B', 'A']

print(len(data_list))   # 8

# multiple add  (use extene)
data_listone : list[str] = ['A', 'B']
data_listtwo : list[str] = ['X', 'Y', 'Z']
data_listone.extend(data_listtwo)   # ['A', 'B', 'X', 'Y', 'Z']
print('add multiple values (extend)',data_listone) # 


# add_elements = data_listone.extend(data_listtwo)  wrong logic
# print('add mutiple values(extend)', add_elements) wrong logic

# multiple delete (use slice)
data_list : list[str] = ['A', 'B', 'C', 'D', 'E']
del data_list[1:3]  # ['A', 'D', 'E']
print('delete multiple values(slice)', data_list)