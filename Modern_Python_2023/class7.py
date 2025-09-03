print('Dictionary, set, tuple, dictionary comprehensive , (chapter 6)')

# Hashable:- immutable types (can't change):- numbers, strings, tuples, (Hashable is unique - can be a key)
# Stable Hash Value: remain constant during its lifetime.
# Unhashable: mutable(changeable) lists, dictionaries, sets (can't make key)
# list [] / tuple () :- value store base on index (don't know on which index value is store)
# Dictionary is data structure, we can create our database
# Dictionary {} :- key-value (key pair value), key (replacement of index) value (item)
# dict_variable[key] :- extract value  e,g. data["name"] (extract-key)
# dictionary :-  add new key-value, update values e.g.  dict_var['key_name'] = 'value'
# dictionary key:- hashable (immutable types) (can't change)
# dict:- key are always uniques, if we multiple times it take only last key '
# dict:- Values can be multiple (use tuple, set, dict)')
# get():-v ar_dict.get(key_name):- if key-found retrieve the value, key not-found retrun None  (not give error)
# Note : dict we can use any in key but when pass unhasable type give error, value (no-restriction) use any
# set {} :- ordered collection of unique elements (can't apply iteration) (without-index)
# set{} :- apply type-casting and convert into list, after that do iteration
# set return unique value (use where data is duplicated)
# change type of list/set (casting) e.g. type_name(cast_variable)
# list comprehension:- [i for i in dir(dict) if '__' not in i] 
# list comprehension:- if '__' not in i (not listed class methods)
# fromkeys() method creates a new dictionary with the provided keys:- data_dict.fromkeys(list)



from typing import Dict, Union, Optional
import pprint

#list
data : list[str] = ['Mike', 'Lal', 'Akbar']
print(data) # ['Mike', 'Lal', 'Akbar']
print(data[1]) # Lal

#set {} :- ordered collection of unique elements.
print('\nset {} :- collection of unique elements.')
set_data : set = {9,2,9,7,2,7,7,4,1,8,3,2,7,4}
print(f'set: {set_data}')   # set: {1, 2, 3, 4, 7, 8, 9}
print(f'change type of list/set (casting)')
type_casted : list[int] = list(set_data)  # list function apply on set
print(f'set cast into list : {type_casted}') # set cast into list : [1, 2, 3, 4, 7, 8, 9]

# Dictionary
print('\nDictionary {} :- key-value (extract) dict_variable[key]')
data1 : dict[str,str] = { 'fname' : 'Akbar',
                         'name' : 'Ali',
                         'education' : 'MSc'
                       } 

print(data1)         # {'fname': 'Akbar', 'name': 'Ali', 'education': 'MSc'}
#print(data1('name')) # error required []
print(data1['name']) # Ali

# pprint is use to decurate the output (pprint.pprint:-  package.function)
pprint.pprint(data1)  # {'education': 'MSc', 'fname': 'Akbar', 'name': 'Ali'}

# to add multiple data_type for key, use alias of union

# create custom type
print('\nCustom Data Type')
Key = Union[int, str]
Value = Union[int, str, list, dict, tuple, set]

data2 : dict[str,str] = { 'fname' : 'Akbar',
                         'name' : 'Ali',
                         'education' : 'MSc',
                         1001 : 'role_no',
                         0 : 'course_no'     # 0 is key not index number

                       } 

#print(data2['0'])  # error because key '0' is integer  
print(f'0 is key not index : {data2[0]}') # course_no
print(f'custom type : {data2}')
# output:-  {'fname': 'Akbar', 'name': 'Ali', 'education': 'MSc', 1001: 'role_no', 0: 'course_no'}

# Hashable (immutable- can't change (key))

print('\nHashable:- immutable types (can\'t change):- numbers, strings, tuples')
print('Unhashable: mutable(changeable) lists, dictionaries, sets\n')
Key = Union[int, str]
Value = Union[int, str, list, dict, tuple, set]

data3 : dict[str,str] = { 'fname'     : 'Akbar',
                         'name'      : 'Ali',
                         'education' : 'MSc',
                          1001       : 'role_no',
                          0          :  'gate_number',
                          'list_1'   : [1,2,3],         # list []
                          'tuple_1'  : (1,2,3),         # tuple ()
                          'set_1'    : {1,2,3},         # set {}
                          'dict_1'   : {'a': 1, 'b':2}, # nested dictionary {}
                           (1,2,3)   : 'tuple_2',
                           (8,9,3)   : "Pakistan"
                        #  [1,2,3]   : 'list_2'     # error 
                        #  {1,2,3}   : 'set_two'    # run time error
                       } 
 # note (in dict we make key of dictionary ) 

print(data3)
# output:- {'fname': 'Akbar', 'name': 'Ali', 'education': 'MSc',1001: 'role_no',
#  0: 'gate_number','list_1': [1, 2, 3], 'tuple_1': (1, 2, 3),'set_1': {1, 2, 3}, 
# 'dict_1': {'a': 1, 'b': 2},(1, 2, 3): 'tuple_2', (8, 9, 3): 'Pakistan'}

print(f'key, 0 is key not index :- {data3[0]}' )  # gate_number
print(f'key, education :- {data3['education']}')  # MSc
print(f'key,dict_1 :-  {data3['dict_1']}')        # {'a': 1, 'b': 2}
#print(f'extract value of b from dict_1 : {data[dict_1['b']]} ') # error
print(f'extract value of b from dict_1 : {data3['dict_1']['b']} ')  #  2
print(f'extract value from dict_1 : {data3['dict_1']} ') # {'a': 1, 'b': 2} 


print('\ndictionary method and attributes')
print([i for i in dir(dict) if '__' not in i])
# output:- ['clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 
# 'pop', 'popitem', 'setdefault', 'update', 'values']

# create new dictionary, add and update values
print('\ncreate empty dictionary then add key-value by using assign operator (=)')
Key = Union[int, str]
Value = Union[int, str, list, dict, tuple, set]

data4 : dict[Key,Value] = {}     # empty dictionary
data4['school'] = 'Educator'
data4['area']    = 'Karachi'
print(f'Add key-value : {data}')  # Add data : {'school': 'Educator', 'area': 'Karachi'}

print('\nupdate dictionary by using assign operator (=)')
Key = Union[int, str]
Value = Union[int, str, list, dict, tuple, set]

data5 : dict[str,str] = { 'fname'     : 'Akbar',
                          'name'      : 'Ali',
                          'education' : 'MSc',
                        }

data5['name'] = 'Omer'     # update 
data5['education'] = 'PhD' # update
print(f'updated values: {data5}')
# output:- updated values: {'fname': 'Akbar', 'name': 'Omer', 'education': 'PhD'}

print(f'\nRetrieve Keys')
for retrive_keys in data5:
    print(retrive_keys) # fname  name   education

print(f'\nRetrieve Keys')
for k in data5.keys():
    print(k)

print(f'\nRetrieve Values')
for v in data5.values():
    print(v)

print(f'\nRetrieve Keys & Values')
for k,v in data5.items():
    print(k,v)      # return tuples

print('\nRetrive Data Method')
print(f'keys() fetch keys:- {data5.keys()}')       # dict_keys(['fname', 'name', 'education'])
print(f'values() fetch values:- {data5.values()}') # dict_values(['Akbar', 'Omer', 'PhD'])
print(f'items() fetch item:- {data5.items()}')     # dict_items([('fname', 'Akbar'), ('name', 'Omer'), ('education', 'PhD')]) 

print('\nvar_dict.get(key_name):- if key-found retrieve the value, if not-found retrun None ')

print(f'get() key found:- {data5.get('name')}')          # Omer
print(f'get() key not-found:- {data5.get('findkey')}')   # None
print(f'get() key not-found, message:- {data5.get("KeyIsNotDefine", 'NA')}') # NA

print('\ncomprehensive list')
print({k:v for v,k in data5.items()}) 

print({k:v for k,v in data5.items()}) # Shuffle 

# shuffle
a : int = 8
b : int = 3

a,b = b,a

print(f'Shuffle (a=8, b=3) : {a,b}')

# create list and dictionary

# Key = Union[int, str]
# Value = Union[int, str, list, dict, tuple, set]

# keys :  list[str] = ['id', 'name', 'fname', 'course']

# data_dict : dict[Key,Value] = {}
# print(f'empty dict : {data_dict}')  # empty dict : {}

# #data_dict = data_dict.fromkeys() error
# data_dict = data_dict.fromkeys(keys) # inline
# print(data_dict)    # output:- {'id': None, 'name': None, 'fname': None, 'course': None}

# fromkeys() method creates a new dictionary with the provided keys,

## =====================
print('## =====================\n\n')






