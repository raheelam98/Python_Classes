# input() return str :- Restrict User Input (type casting) (class 6)
print('\nRestrict User Input (type casting)')

user_input = input('Enter Number\t')   # problem :- take int and string
print(type(user_input))     # <class 'str'>  
print(f'User input is {user_input}' )
# input() :- string-type convert into integer,  int (input())
user_input_num = int(input('Enter Number\t')) # only take int
print(type(user_input_num))   # <class 'int'>
print(f'Input number is {user_input_num} ')

# tuples (class 5)
print('\nExtracting value from tuple, one by one and put in separate variable ')
data_base : list[tuple[str,str]] = [
                                        ('Akbar', '123'),
                                        ('Mike', '456')
                                    ]

# unzip user name and password
for row in data_base:
    user, password = row    # extract value from tuple one by one put in separate variable 
    print(user,password)    # Akbar 123       Mike 456

print('\nCreate System to Validate User Name and Password\n')
input_username : str = input('Enter User Name\t')
input_password : str = input('Enter Password\t')

# run loop to match user name and password for each user
for row in data_base:
    user, password = row
    if input_username == user and input_password == password:
         print(f'Valid User {input_username}')
         break
   # else:   #  else belong to if  (print command :- run twice)
else: #  else belong to for loop (only python support it:- for else)
    print(f'Invalid User or Password, Not Found {input_username}')

# for...else, if...else, while...else
