from typing import Union, Optional, Any, Dict
import pandas as pd
import pprint
import json
import numpy as np


print('Dictionary methods, JSON, Jsonify and dataframe (book chapter 6)\n')
print('Dictioary convert into structure data')
print('\nData Fram')

student_data : dict[str,list[Any]] = { 'roll_number' : [1,2,3],
                                        'name'       : ['Ali', 'Henry', 'Akbar'],
                                        'education' : ['Bsc', 'MSc', 'PhD']
                                      }

df : pd.DataFrame = pd.DataFrame(student_data)
print(df)

print('\n dict')
Key = Union[int, str]
Value = Union[int, str, list, dict, tuple, set]

data : dict[str,str] = { 'fname'     : 'Akbar',
                          'name'      : 'Ali',
                          'education' : 'MSc',
                          'name'      :  'Jamal'   # repeat name key
                        }
print(f'dict:- {data}')
# output:-  {'fname': 'Akbar', 'name': 'Jamal', 'education': 'MSc'}

print(type(data))       # <class 'dict'>

print('\nConvert into JSON')

json_data =  json.dumps(data, indent=4)
print(json_data)

# output 
# Convert into JSON
# {
#     "fname": "Akbar",
#     "name": "Jamal",
#     "education": "MSc"
# }

print(type(json_data))  # <class 'str'>


print('\nConvert dict into JSON')
data_dict = {"name": "John", "age": 30, "city": "New York"}
json_object = json.dumps(data_dict)

print(data_dict)    # {'name': 'John', 'age': 30, 'city': 'New York'}
print(json_object)  # {"name": "John", "age": 30, "city": "New York"}

print(type(data_dict))  # <class 'dict'>
print(type(json_object)) # <class 'str'>

# json.dumps() :- fun convert the dictionary to a JSON object and 
# store it in the json_object variable

print('\nNested Dictionary error solution')

from typing import Union, TypedDict, Tuple, Set, List
import pprint

cdeDataType = TypedDict(
    'cdeDataType',
    {
        "a": int,
        "b": int
    }
)

myDataType = TypedDict(
    'myDataType', {
        "fname": str,
        "name": str,
        "education": str,
        "abc": List[int],
        'xyz': Set[int],
        'efg': Tuple,
        'cde': cdeDataType
    }
)

# Key = Union[int, str]  # create custom type
# Value = Union[int, str, list, tuple, set]

data: myDataType = {
    "fname": "Muhammad Aslam",
    "name": "Muhammad Qasim",
    "education": "MSDS",
    "abc": [1, 2, 3],
    'xyz': {1, 2, 3},
    'efg': (1, 2, 3),
    'cde': {"a": 1, "b": 2}
}

print(data['cde']['b'])








