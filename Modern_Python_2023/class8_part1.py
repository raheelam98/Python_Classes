print('Dictionary methods, JSON, Jsonify and dataframe\n')

import pandas as pd

from typing import Union, Optional

methods : list[str] = [i for i in dir(dict) if '__' not in i]
print(methods)
# output:- ['clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 
# 'pop', 'popitem', 'setdefault', 'update', 'values']

print('\nclear(), clear data but not object')
Key = Union[int, str]
Value = Union[int, str, list, dict, tuple, set]

data : dict[str,str] = { 'fname'     : 'Akbar',
                          'name'      : 'Ali',
                          'education' : 'MSc',
                        }

print(f'before clear:- {data}')   # before clear : {'fname': 'Akbar', 'name': 'Ali', 'education': 'MSc'}
data.clear()                      # clear all the data but object is there
print(f'after clear:- {data}')    # after clear : {}  

print('\ndel():- del data with object')
Key2 = Union[int, str]
Value2 = Union[int, str, list, dict, tuple, set]

data2 : dict[str,str] = { 'fname'     : 'Akbar',
                          'name'      : 'Ali',
                          'education' : 'MSc',
                        }

print(f'before del:- {data2}')   # before del : {'fname': 'Akbar', 'name': 'Ali', 'education': 'MSc'}
del data2                         # delete data with object
#print(f'after del:- {data2}')    # error :- 'data2' is not defined

print('\npop(key):- delete the pass value of key')
Key = Union[int, str]
Value = Union[int, str, list, dict, tuple, set]

data3 : dict[str,str] = { 'fname'     : 'Akbar',
                          'name'      : 'Ali',
                          'education' : 'MSc',
                        }

print(f'before pop:- {data3}')      # before pop : {'fname': 'Akbar', 'name': 'Ali', 'education': 'MSc'}
#data3.pop()                        # give error, have to pass key
pop_key : str = data3.pop('name')   # delete the pass value
print(f'pop value:- {pop_key}')     # pop value:- Ali
print(f'after pop:- {data3}')       # after pop:- {'fname': 'Akbar', 'education': 'MSc'}

print('\npopitem():-  delete last key with value')
Key4 = Union[int, str]
Value4 = Union[int, str, list, dict, tuple, set]

data4 : dict[str,str] = { 'fname'     : 'Akbar',
                          'name'      : 'Ali',
                          'education' : 'MSc',
                        }

print(f'before popitem:- {data4}')       # before popitem : {'fname': 'Akbar', 'name': 'Ali', 'education': 'MSc'}
pop_item : str = data4.popitem()         # delete the last key with value
print(f'popitem key-value:- {pop_item}') # popitem key-value:- ('education', 'MSc') 
print(f'after popitem:- {data4}')        # after popitem:- {'fname': 'Akbar', 'name': 'Ali'} 

print('\nbook page 97 MUST READ')
print('\nget(key):- key found return value, if key not_found return None')
Key5 = Union[int, str]
Value5 = Union[int, str, list, dict, tuple, set]

data5 : dict[str,str] = { 'fname'     : 'Akbar',
                          'name'      : 'Ali',
                          'education' : 'MSc',
                        }

print(f'1- key found return value:- {data5.get('education')}') # 1- key found return value:- MSc                # 
get_key : str = data5.get('KeyIsNotDefine')                 
print(f'2- key not_found return:- {get_key}')                  # 2- key not_found return:- None              
get_key_mess : str = data5.get('KeyIsNotDefine','NA')
print(f'3- pass message if key not_found:- {get_key_mess}')    # 3-  pass message if key not_found:- NA
print(f'4- get(key) not effected on original dict ??? :- {data5} ') # 4- {'fname': 'Akbar', 'name': 'Ali', 'education': 'MSc'} 

print('\nsetdefault(new_key):- add new key at the end')
Key6 = Union[int, str]
Value6 = Union[int, str, list, dict, tuple, set]

data6 : dict[str,str] = { 'fname'     : 'Akbar',
                          'name'      : 'Ali',
                          'education' : 'MSc',
                        }

add_key_end : str = data6.setdefault('add_key')               #'add_key': None
print(f'setdefault(new_key) add key at the end:- {data6}')
#add_key_mess : str = data6.setdefault('add_key', 'Empty Value')
#print(f'setdefault(new_key) with value mess:- {add_key_mess}')
a : str = data6.setdefault("Pakistan","Empty value")            # 'Pakistan': 'Empty value'
print(a)
print(f'setdefault(new_key) new key added in dict:- {data6}')
# output :- {'fname': 'Akbar', 'name': 'Ali', 'education': 'MSc', 'add_key': None, 'Pakistan': 'Empty value'}


print('\nupdate():- update value and add new data as well ')
Key = Union[int, str]
Value = Union[int, str, list, dict, tuple, set]

data_old : dict[str,str] = { 'fname'     : 'Akbar',
                             'name'      : 'Ali',
                             'education' : 'MSc',
                        }

data_new : dict[str,str] = { 'name'       : 'Mike',     # update name 
                              'id'        :  7,
                              'country'   : 'Pakistan'
                        }


update_data : list[str] = data_old.update(data_new)
#print(f'update data :- {update_data}')       # update data :- None
print(f'updated data :- {data_old}')
# output:- {'fname': 'Akbar', 'name': 'Mike', 'education': 'MSc', 'id': 7, 'country': 'Pakistan'}



print('\nkey are always uniques, if we multple times it take only last key ')
print('Values can be multiple (use tuple, set, dict)')
Key7 = Union[int, str]
Value7 = Union[int, str, list, dict, tuple, set]

data7 : dict[str,str] = { 'fname'     : 'Akbar',
                          'name'      : 'Ali',
                          'education' : 'MSc',
                          'name'      :  'Jamal'   # repeat name key
                        }
print(f' {data7}')
# output:-  {'fname': 'Akbar', 'name': 'Jamal', 'education': 'MSc'}

