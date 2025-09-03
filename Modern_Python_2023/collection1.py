# https://www.youtube.com/watch?v=gOMW_n2-2Mw
# collection = single "varaiable" used to store multiple values
# List = [] ordered and changedable. Duplicates OK
# Set = {} unordered and immutable(can't change), but  Add/Removed OK. NO duplication
# Tuple = () ordered and unchangeable. Duplicate OK . FASTER

fruits : list[str] = ["apple", "orange", "banana", "coconut"]
print(fruits)

#print(dir(fruits))
#print(help(fruits))
# print(len(fruits))
print("single element ",fruits[2])    # single element :- banana
print("three elements", fruits[0:3])  # three elements :- 'apple', 'orange', 'banana'
print(" every 2nd elements",fruits[::2])  # every 2nd element :- 'apple', 'banana'
print("reversie ",fruits[::-1]) # reverse :- ['coconut', 'banana', 'orange', 'apple']
print("apple" in fruits )   # True
fruits.append("mango")
print("add at the end ",fruits)   #['apple', 'orange', 'banana', 'coconut', 'mango']
fruits.remove("apple")      # ['orange', 'banana', 'coconut', 'mango']
print("remove element ",fruits)
fruits.insert(0, "pineapple")   # ['pineapple', 'orange', 'banana', 'coconut', 'mango']
print("add element with index ",fruits)
fruits.sort()
print("sort alphabetically ",fruits)   # ['banana', 'coconut', 'mango', 'orange', 'pineapple']

# iteration
# for fruit in fruits:
#     print(fruit)

a = ("a", "b", "c", "d", "e", "f", "g", "h")
x = slice(3, 5)
print(a[x])

a = ("a", "b", "c", "d", "e", "f", "g", "h")   # see latter
x = slice(0, 8, 3)
print(a[x])