print("Python List Comprehension")

# [Python List Comprehension Syntax - greeks](https://www.geeksforgeeks.org/python-list-comprehension/)
# newList = [ expression(element) for element in oldList if condition ] 

# [https://www.w3schools.com/python/python_lists_comprehension.asp](https://www.w3schools.com/python/python_lists_comprehension.asp)
# newlist = [expression for item in iterable if condition == True]

# [Syntax of List Comprehension - programiz](https://www.programiz.com/python-programming/list-comprehension)
# [expression for item in list if condition == True]

num_list1 = [2,3,4]

## old way 
square_numbers = []
for num in num_list1:
    square_numbers.append(num * num)

print("square_number with list", square_numbers)
## output :-  [4, 9, 16]    

squares = []
for x in range(10):
    squares.append(x**2)

print("square with range(10)", squares)    
## output :- [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

print('\nlist comprehension')

num_list2 = [2,3,4]
# list comprehension to create new list
new_list2 = [num ** 2 for num  in num_list2 ]

print("new_list2 ", new_list2)
## output :- new_list2  [4, 6, 8]

# [expression for item in list if condition == True]

square_range_list = [num*2 for num in range(10)]
print("square range 10 ", square_range_list)

## Conditional in List Comprehension

even_number = [ num for num in range (1,10) if num % 2 == 0 ]

print('even_number', even_number)
## output :- even_number [2, 4, 6, 8]


### ========================================================================== ###

## https://www.programiz.com/python-programming/methods/built-in/range
# range() function generates a sequence of numbers
# starts at 0, increments by 1, and stops before the specified number.
# range(start, stop(n-1), step)
# range(stop(n-1)) , range(start, stop(n-1)), range(start, stop(n-1), step)

print("\nPython range() Function :- range(start, stop(n-1), step) ")