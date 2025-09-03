# Implicit type conversion, known as coercion, occurs automatically when different data types are used together in operations.
#  type casting, such as int(), float(), str(), and bool()
# Explicit type casting is done using the mentioned function
#  int("5") converts the string "5" to the integer 5.

print('type casting in Python :')
print('explicitly converting a value from one data type to another\n')

a = 100
print('a = 100 :-  ',a, type(a), id(a))
# output : a = 100 :-   100 <class 'int'> 4384553792

b = str(a)
print('b=str(a) :- ',b, type(b), id(b))
# output : b=str(a) :-  100 <class 'str'> 4357486992

num_float = 14.5
print('num_float :- ', num_float, type(num_float))
# output : num_float :-  14.5 <class 'float'>

num_int = int(num_float)
print('num_int :- ', num_int, type(num_int))
# output : num_int :-  14 <class 'int'>

# integer value of boolean
# note:-  1 = true, 0 =false
print('\ninteger value of boolean')

p1 =1
print(p1 , type(p1))  # output:  1 <class 'int'>

p2 = False
print(p2 , type(p2))  # output:  False <class 'bool'>

q1 = int(True)
print(q1, type(q1))  # output: 1 <class 'int'>

q2 = int(False)
print(q2, type(q2))  # output:  0 <class 'int'>

r1 = bool(1)
print(r1, type(r1)) # output: True <class 'bool'>

r2 = bool(0)
print(r2, type(r2)) # output: False <class 'bool'>




