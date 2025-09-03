# Comprehensions
# https://www.geeksforgeeks.org/comprehensions-in-python/ 
# Comprehensions in Python
#  4 types of comprehension:
# * List Comprehensions
# * Dictionary Comprehensions
# * Set Comprehensions
# * Generator Comprehensions

# List Comprehensions
# List Comprehensions provide an elegant way to create new lists.
# Syntax: output_list = [output_exp for var  in input_list if (var satisfies this condition)]

input_list1 = [1, 2, 3, 4, 4, 5, 6, 7, 7]
list_using_comp = [var for var in input_list1 if var % 2 == 0]
print("Output List using list comprehensions:", list_using_comp)

# Dictionary Comprehensions
# Extending the idea of list comprehensions, we can also create a dictionary using dictionary comprehensions.
# output_dict = {key:value for (key, value) in iterable if (key, value satisfy this condition)}

input_list2 = [1,2,3,4,5,6,7]
dict_using_comp = {var:var ** 3 for var in input_list2 if var % 2 != 0}
print("Output Dictionary using dictionary comprehensions:",dict_using_comp)

# Set Comprehensions
# Set comprehensions are pretty similar to list comprehensions. The only difference between them is that set comprehensions use curly brackets { }

input_list3 = [1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 7]
set_using_comp = {var for var in input_list3 if var % 2 == 0}
print("Output Set using set comprehensions:",  set_using_comp)

# Generator Comprehensions
# Generator Comprehensions are very similar to list comprehensions. One difference between them is that generator comprehensions use circular brackets whereas list comprehensions use square brackets. The major difference between them is that generators don’t allocate memory for the whole list. Instead, they generate each value one by one which is why they are memory efficient.

input_list4 = [1, 2, 3, 4, 4, 5, 6, 7, 7]

output_gen = (var for var in input_list4 if var % 2 == 0)
print("Output values using generator comprehensions:", end = ' ')
for var in output_gen:
    print(var, end = ' ')
