print('Type aliases, zip and sorted')

from typing import Union

# Type aliases (custom type )
print('\nType aliases:- Student Percentage (dynamic)')

#PerType : Union[float,int]  error

PerType = Union[float,int]  # Type aliases
percentages : list[PerType] = [98, 58.8, 65, 40, 75.5]
grades : list[str] = []

for  per in percentages:  # fetch from percentage (list)
    grade : str = ""      # (local variable) when condition is true, fetch grade 

    if (per >= 0) and (per < 50):   #  run :- both conditions are true
        grade = 'Fail'
    elif (per >= 50) and (per < 60):
        grade = 'C'
    elif (per >= 60) and (per < 70):
        grade = 'B'
    elif (per >= 70) and (per <= 100):
        grade = 'A'

    grades.append(grade)    # put grade in grades_list (append add value in empty-list one by one)

print(f'Percentage :{percentages}')  # [98, 58.8, 65, 40, 75.5]
print(f'Grades: {grades}')            # ['A', 'C', 'B', 'Fail', 'A']


# Zip combine elements from two or more iterables (same length) into tuples (list-of-tuples)
#(zip:- generator function, {iteration perform --> list, for-loop} )

print('\nZip combine elements from two or more iterables (same length) into tuples.')

print(zip(percentages,grades))      # <zip object at 0x1009842c0> (generator function)

print('zip is generator function {iteration perform --> list, for-loop}')

print(f'\nPercentage and grades {list(zip(percentages,grades))}\n' )
# output:- [(98, 'A'), (58.8, 'C'), (65, 'B'), (40, 'Fail'), (75.5, 'A')]

print(list(zip(percentages, grades, list(range(len(percentages)))   )))
# output:- [(98, 'A', 0), (58.8, 'C', 1), (65, 'B', 2), (40, 'Fail', 3), (75.5, 'A', 4)]

print(f'\npercentage length {len(percentages)}')       # percentage length 5
print(f'percentage range {range(len(percentages))}') # percentage range range(0, 5)
print(f'percentage list {list(percentages)}')        # percentage list [98, 58.8, 65, 40, 75.5]
 
roll_no : list[int] = list(range(len(percentages)))
print(f'Roll Number : {roll_no}')   # Roll Number : [0, 1, 2, 3, 4]

print(f'\nRoll_no, Percentage, Grade \n {list(zip(roll_no, percentages, grades))}\n')
# output:-  [(0, 98, 'A'), (1, 58.8, 'C'), (2, 65, 'B'), (3, 40, 'Fail'), (4, 75.5, 'A')]

data_base = list(zip(roll_no, percentages, grades))
print(f'DataBase {data_base}')
# output:- DataBase [(0, 98, 'A'), (1, 58.8, 'C'), (2, 65, 'B'), (3, 40, 'Fail'), (4, 75.5, 'A')]

print(f'sorted   {sorted(data_base)}')  # no change
# output:- sorted  [(0, 98, 'A'), (1, 58.8, 'C'), (2, 65, 'B'), (3, 40, 'Fail'), (4, 75.5, 'A')]

# sorted has parameter key, key require function, we give lambda function
# data_base (tuple) index(0)= roll_no, index(1)=persentages, index(2)=grades

print(f'Sorted by index1 {sorted(data_base, key=lambda x:x[1])} ')
# output:- Sorted by index1: [(3, 40, 'Fail'), (1, 58.8, 'C'), (2, 65, 'B'), (4, 75.5, 'A'), (0, 98, 'A')] 

print(f'Sorted (reverse) {sorted(data_base, key=lambda x:x[1], reverse=True )}  ')
# output:- Sorted (reverse) [(0, 98, 'A'), (4, 75.5, 'A'), (2, 65, 'B'), (1, 58.8, 'C'), (3, 40, 'Fail')] 

print(f'Sorted by index2 {sorted(data_base, key=lambda x:x[2])}')
# output:- Sorted by index2 [(0, 98, 'A'), (4, 75.5, 'A'), (2, 65, 'B'), (1, 58.8, 'C'), (3, 40, 'Fail')]


print('')





