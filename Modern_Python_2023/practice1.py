
print('\nUsing get() to Access Values (book-97) MUST Read')
methods : list[str] = [i for i in dir(dict) if '__' not in i]
print(methods)

print('\nin oprator:- search substring (return True/Flase)')
# in keyword is used to test if a value is present in a sequence, such as a list, tuple, string, or set.
print( "SerachGame" in '''Hi do you now where is SerachGame, find out somewhere ''')
print('\nin :- for loops for iteration')
# for loops for iteration:-  for value in sequence

char_list1 : list[str] = ['a','b']
int_list : list[int]  = [1,2]
print(list(zip(char_list1,int_list)))
# output:- [('a', 1), ('b', 2)]
print('\nzip:- loop')
for i,j in zip(char_list1,int_list):
    print(f'Hi! first {i} second {j}')
# output:- Hi! first a second 1   Hi! first b second 2