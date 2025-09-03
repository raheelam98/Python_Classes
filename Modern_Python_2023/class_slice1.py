
#class 4
#slicing :- variable_names[start:end:step]  (extract more than 2 or more elements, default slicing from left to right)
# slicing :-  start : int = include (Default 0),  end : int = n-1, step : int = sequence (Default 1) (step of the slicing)
# Note slicing :- if we don't put any value (its means everything included)
# default slicing is from left to right :

# class 4
from typing import Any

print('\nslicing:- variable_names[start:end:step]')
print('start : int = include (Default 0),  end : int = n-1, step : int = sequence (Default 1) (step of the slicing)\n')

# ->        0          1       2
names = ["Qasim","Sir Zia","Sir Inam"] # length-1 
# <-        -3       -2        -1

print(names[0]) # Qasim
print(names[-3]) # Qasim
print(names[-2]) # Sir Zia
print(f'Founder of PIAIC {names[-2].upper()}\n')

# ->                    0        1         2
names : list[str] = ["Qasim","Sir Zia", "Sir Inam", 20, True]
# <-                    -5      -4          -3       -2   -1
print("List :- ", names)
print(names[-2])  # 20
print(type(names)) # <class 'list'>
print(type(names[-2])) # <class 'int'>

# string is iterative data-type we can perform iteration  str['abcde']
characters1 : list[str] = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
print(characters1)

#                          0    1    2    3    4     5    6    7   8     9   10                                                                       25(Z)
characters : list[str] = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
#                         -26    -25  -24                                                                                                          -2   -1   

# default slicing is from left to right :
# variable_names[start:end:step]
# slicing :-  start : int = include (Default 0),  end : int = n-1, step : int = sequance (Default 1) (step of the slicing)

print("print whole list [::] \n",characters[::])                      # left to right :-  print ['A', 'B', 'C', ...... , 'W', 'X', 'Y', 'Z']
print("print whole list in reverse order [::-1]\n",characters[::-1])   # right to left :-  print ['Z', 'Y', 'X', 'W', .... , 'C', 'B', 'A']
print("print whole list after 1 elements [::2]\n",characters[::2])    # print  ['A', 'C', 'E', ...., 'U', 'W', 'Y']

print('\nslice :-  extract selected values\n')

#                          0    1    2    3    4     5    6    7   8     9   10                                                                       25(Z)
characters : list[str] = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
#                         -26  -25  -24  -23   -22                                                                                                 -2   -1   


print('[0:3]     ',characters[0:3])      #  (0= include(start) : (end)index 3-1 = 2)           print ['A', 'B', 'C']
print('[:3]      ',characters[:3])       # ((default)0= include(start) : (end)index 3-1 = 2)   print ['A', 'B', 'C']
print('[-26:-23] ',characters[-26:-23])  # (-26=include(start) : (end)index -23-1= -24)        print ['A', 'B', 'C']
print('[0:3:1]   ',characters[0:3:1])    # (0= include(start) : (end)index 3-1 = 2)            print ['A', 'B', 'C']
print('[0:3:1]   ',characters[0:3:1])    # (0= include(start) : (end)index 3-1 = 2)            print ['A', 'B', 'C']

print('[0:10:3]  ',characters[0:10:3])    # (0=include(start) : (end)index 10-1 = 9)              print ['A', 'D', 'G', 'J']
print('[1:10:3]  ',characters[1:10:3])    # (1=include(start) : (end)index 10-1 = 9)              print ['B', 'E', 'H']
print('[::6]     ',characters[::6])       # (0=include(start) : (end)index = not give(all list))  print ['A', 'G', 'M', 'S', 'Y']

print('\nslice :-  extract selected values from A to H\n')
#                          0    1    2    3    4   5     6    7
characters3 : list[str] = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
#                          -8    -7   -6   -5   -4   -3   -2   -1  

# iteration slicing ->  (1) step -> positive (default left to right) (2)step <- negative (right to left)
print('[1:-3]      ',characters3[1:-3])     #  (1=include(start) : (end)index -3-1 = -4)   print ['B', 'C', 'D', 'E']
print('[-2:-5:-1]  ',characters3[-2:-5:-1]) #  (end)index -5-1 = -6) ??????
# [-2:-5:-1] :-  (-2=include(start) : (end)index -5-1 = -6)   print ['G', 'F', 'E'] (sequence is - ve)
print('[-2:-5]     ',characters3[-2:-5])    
# [-2:-5]:- (-2=include(start) : (end)index -3-1 = -4)  print [] (sequence is + ve)start from -2 never get -5 (when move from left to right)
print('Note [] :-  sequence start from -2 never get -5 (when move from left to right)')

# slice with loop (class 5)
#slicing :- variable_names[start:end:step]
print('\nExtract selected values(class 5)\n')

print('Extract select values from list through loop (use slice:- variable_names[start:end:step])')
numbers_list : list[str] = ['one', 'two', 'three', 'four', 'five', 'Six']

print('extract first two values')
for name in numbers_list [:2]:  # print:- one tow
    print('[:2] ',name)

print('\nextract values from -2')
for name in numbers_list [:-2] :
    print('[:-2] ',name)   