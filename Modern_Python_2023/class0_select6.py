from typing import Dict, Union, Optional
import pprint


# Hashable (immutable- can't change (key))

print('\nHashable:- immutable types (can\'t change):- numbers, strings, tuples')
print('Unashable: mutable(changeable) lists, dictionaries, sets\n')
Key = Union[int, str]
Value = Union[int, str, list, dict, tuple, set]

data : dict[Key,Value] = { 
                         'name'      : 'Ali',
                         'code'      :   8,
                          0          :  'gate_number',
                          'list_1'   : [1,2,3],         # list []
                          'tuple_1'  : (1,2,3),         # tuple ()
                          'set_1'    : {1,2,3},         # set {}
                          'dict_1'   : {'a': 4, 'b':9}, # nested dictionary {}
                           (1,2,3)   : 'tuple_2',
                       } 
 # note (in dict we make key of dictionary ) 

print(data)
# output:-  {'name': 'Ali', 'code': 8, 0: 'gate_number', 'list_1': [1, 2, 3], 'tuple_1': (1, 2, 3), 'set_1': {1, 2, 3}, 'dict_1': {'a': 1, 'b': 2}, (1, 2, 3): 'tuple_2'}

print(f'key, 0 is key not index :- {data[0]}' )  # gate_number
print(f'key, name :- {data['name']}')  # Ali
print(f'key,dict_1 :-  {data['dict_1']}')        # {'a': 4, 'b': 9}
print(f'extract value of b from dict_1 : {data['dict_1']['b']} ')  #  9
 


