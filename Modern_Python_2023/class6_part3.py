print('Book - chapter 5 \n')

#  car = 'handa' (assign value),  car == 'bmw' (compare value)
#  python is case sensative:- audi and Audi are different
# in (for-loop) = extract element from iterated types e.g.  for item_var in item_list:  
# in (without loop) check membership True/Flase e.g. 'item_name' in item_list

print('book p-72')
cars : list[str] = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:        # # in = extract element from iterated types 
    if car == 'bmw':    # if the current value of car is 'bmw' -> upper()
        print(car.upper()) 
    else:
        print(car.title())  # other than 'bmw' -> title()

# output:-  Audi  BMW  Subaru  Toyota

for car in cars:
    print(car)

print('comprehensive')
# print(car.upper()) if car == 'bmw' else print(car.title()) # Toyota
# error:- print(car.upper()) for car in cars if car == 'bmw' else  print(car.title())

print(f'comprehensive with loop {[i for i in cars]} ') 

# comprehensive if-else :-   True-block if logic else False-block
print(f'comprehensive with condition {[i.upper() if i=='bmw' else i.title() for i in cars]}')
# output:- comprehensive with condition ['Audi', 'BMW', 'Subaru', 'Toyota']

print('\ncondition with !=')
cars : list[str] = ['audi', 'bmw',"Mehran", 'subaru', 'toyota']

for car in cars:
    if car != 'Mehran':
        print(car.upper())
    else:
        print(car.lower())

print('\nin (for-loop) = extract element from iterated types')
cars_detail : list[str] =  [i.upper() if i != 'Mehran' else i.lower() for i in cars]
print(f'in with for-loop  {cars_detail}')

print('\nin (without loop) check membership True/Flase')
cars : list[str] = ['audi', 'bmw',"Mehran", 'subaru', 'toyota']
find_car1 : str = 'changan' in cars
print(f'in  {find_car1}')   # False
find_car2 : str = 'audi' in cars
print(f'in {find_car2}')    # True

print('\nbook p-74')
answer = 40
if answer != 42:
    print("40  is not the correct answer. Please try again!")

answer = 42
if answer != 42:
    print("42 can't run because of condition. Please try again!")

answer = 43
if answer != 42:
    print("43 is not the correct answer. Please try again!")

print('\nbanned_users to login p-76')

banned_users : list[str] = ['andrew', 'carolina', 'david']
user : str = 'marie'

print(user not in banned_users) # True

if user not in banned_users:
    print(f"{user.title()}, you can post a response if you wish.")

print('\nif chain, check each different condition, only true print p-82')

requested_toppings = ['mushrooms', 'extra cheese']

if 'mushrooms' in requested_toppings: print("Adding mushrooms.")

if 'pepperoni' in requested_toppings: print("Adding pepperoni.")

if 'extra cheese' in requested_toppings: print("Adding extra cheese.")
print("\nFinished making your pizza!")

print('\nbook p-86')

requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("Sorry, we are out of green peppers right now.")
    else:
        print(f"Adding {requested_topping}.") 
        print("\nFinished making your pizza!")

print('\nbook p-86 if we request the topping then code run')

requested_toppings = []    
if requested_toppings:
    for requested_topping in requested_toppings: 
        print(f"Adding {requested_topping}.")
        print("\nFinished making your pizza!")
    else:
        print("Are you sure you want a plain pizza?")

print('\nbook p-87 : multiple list')

available_toppings : list[str] = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']

requested_toppings = ['mushrooms', 'french fries', 'extra cheese']   # user input

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}.") 
    else:
        print(f"Sorry, we don't have {requested_topping}.")  
print("\nFinished making your pizza!")

user_input : str =  input("Enter ',' seprated value for topping\t").split(",")
print(user_input)

user_name : str = input("Enter user id: \t")
user_passwrod : str = input("Enter password:\t")


if user_name == 'admin' and user_passwrod == 'admin':
    print("sent otp on you registered number")
    otp : str = input("Please inter otp")
    if otp == '123':
        print("Welcom PIAIC")
else:
    print("Invalid user or password")
