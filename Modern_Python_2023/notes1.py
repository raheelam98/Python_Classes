
# List Comprehension
print("\nList Comprehension")

#Syntax:- newlist = [expression for item in iterable if condition == True]
# List comprehension :- [expression for item in iterable if condition]
# expression: The value you want to include in the new list.
# item: The variable representing each element in the iterable.
# iterable: The sequence of elements (e.g., a list, tuple, string, or range) that you want to iterate over.
# condition: (optional) A condition that filters which elements are included in the new list.

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)

print("\nList Comprehension :- String Methods and Attributes List\n")
str_methods : list[str] = [i for i in dir(str) if "--" not in i]
print(str_methods)

# List Comprehension to print letters
print("\nList Comprehension to print letters\n")
char_list : list[str] = [chr(i) for i in range(65,91)]
print(char_list)


