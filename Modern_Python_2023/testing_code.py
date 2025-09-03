from typing import Dict, Union, Optional
import pprint

## ===================== class 7#
print(' =====================\n')
# class 7 (Qasim)
Key = Union[int,str] # create custom type
Value = Union[int, str, list, dict, tuple, set]

data : Dict[Key,Value] = {
                        "name":"Ahmed Akbar",
                        "education": "MSc"}
#                 key
print(data.get('API',"NA"))  # output:- NA
print(data.get("name","NA"))  # output:- Ahmed Akbar

print(data["education"]) # output :- MSc
#print(data["API"])       # output :- KeyError: 'API'
print(data.get('API'))   # output :- None

print(' =====================\n')
# https://www.tutorialspoint.com/python/python_dictionary.htm
# tutorials -- keys() method :- returns a list of all the available keys in the dictionary
# dict.keys()
# Keys must be immutable. Which means you can use strings, numbers or tuples as dictionary keys
#  dict[key] :- if a key is not found, raised KeyError 
#  dict.get() :- If you use, key is not found, return None (or custom value, if you specify one)

dict = {'Name':'Zara', 'Age':7}

print( dict.keys())   # output:-  dict_keys(['Name', 'Age'])
print(dict["Name"])   # output:-  Zara
#print(dict["Alice"]) # output:-  KeyError: 'Alice' # call uundefined key
#print(dict[7])  # output:- KeyError: 7

data = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
print(data['Name']) # output:-  Zara
del data['Name'];  # remove entry with key 'Name'
data.clear();      # remove all entries in dict
del data ;         # delete entire dictionary

# change the value of key
dict = {'Name': 'Zara', 'Age': 7, 'Name': 'Manni'}
print( "dict['Name']: ", dict['Name'])

print(' =====================\n')

#  type(), built-in function , which returns the class of the given object
var1 = 100
print(id(var1))   # output :-  4426496832
print(type(var1)) # output :- <class 'int'>
print('type of variable 100 is ' , type(100) )  #  <class 'int'>

list = [ 'abcd', 786 , 2.23, 'john', 70.2 ]
tinylist = [123, 'john']

print (list)            # Prints complete list
print (list[0])         # Prints first element of the list
print (list[1:3])       # Prints elements starting from 2nd till 3rd 
print (list[2:])        # Prints elements starting from 3rd element
print (tinylist * 2)    # Prints list two times
print (list + tinylist) # Prints concatenated lists







