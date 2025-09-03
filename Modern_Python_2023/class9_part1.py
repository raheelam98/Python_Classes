print('loop, iterative type, input, sys.argv')
# While loop
#    while logic: # True/False
#    loop_body




#                        0 1 2  
data_list : list[int] = [1,2,3]
for n in data_list:
    print(f"list number :{n}")

#                          0 1 2
data_tuple : tuple[int] = (1,2,3)
for n in data_tuple:
    print(f"Tuple number :{n}")

#                 012
data_str : str = "run"
for c in data_str:
    print(f"current character :{c}")

#                           iteration perform on keys
data_dict : dict[str,str] = {'name' : 'Ali', 'course' : 'Python' }
for k in data_dict:
    print(f'dictionary key is {k} values is {data_dict[k]}')

print('\ncan directly perform iteration on set data type')
#           iteration perform on keys (here no index or key)
set1 : set[int] = {1,2,3,1,1,1,1}
for i in set1:
    print(f'set item is {i}')

# output:- set item is 1, set item is 2, set item is 3

print('\napply iteration on set with type casting in list')
set2 : list[set[int]] = {1,2,3,1,1,1,1}
for i in set2:
    print(f'value from list of set: {i}')
# output:-  value from list of set: 1, value from list of set: 2, value from list of set: 1

print('\nzip')
char_list1 : list[str] = ['a','b','c']
char_list2 : list[str] = ['x', 'y', 'z']
int_list : list[int]  = [1,2,3]

print(zip(char_list1,char_list2,int_list)) # <zip object at 0x1067f7800>
# note zip need to iterate through list
# output:- [('a', 'x', 1), ('b', 'y', 2), ('c', 'z', 3)]

print(list(zip(char_list1,char_list2,int_list)))
# output:- [('a', 'x', 1), ('b', 'y', 2), ('c', 'z', 3)]

print('\nzip:- loop')
for i,j,k in zip(char_list1,char_list2,int_list):
    print(f'Hi! first {i} second {j} thrid {k}')

# output:-
# Hi! first a second x thrid 1
# Hi! first b second y thrid 2
# Hi! first c second z thrid 3
    
print('\nwhile loop')
# While loop  (time 50)
#    while logic: # True/False
#    loop_body
    
flag : bool = True
current_number : int = 0

while flag:
    print(f'while loop {current_number}')
    current_number += 1

    if current_number == 2:     # flag false at some point
        break                   # stop the loop
# output:- while loop 0    while loop 1

print('\nDisplay 2 list')
num_list : list[int]  =  [100,200,300]
index : int = 0

while index < len(num_list):
    #print(f"current number is: {index} and the list value is {num_list(index)}")
    print(f"current number is: {index} and the list value is {num_list[index]}")
    index += 1
    #break

# current number is: 0 and the list value is 100
# current number is: 1 and the list value is 200
# current number is: 2 and the list value is 300

#note:- while use index to pass opration (see later)
