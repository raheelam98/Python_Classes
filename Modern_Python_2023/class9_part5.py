
# https://www.youtube.com/watch?v=W5KCwG2l3R8&list=PL0vKVrkG4hWrEujmnC7v2mSiaXMV_Tfu0&index=14
# - **While Loops**: Learn to use while loops for repeated execution as long as a condition is true.
# - **For Loops**: Discover the power of for loops for iterating over sequences and other iterable objects.
# - **Control Statements**: Understand how to use `break`, `continue`, and `pass` to control the flow of your loops.
# - **Input Function**: Get hands-on experience with the `input()` function for gathering user input.
# - **Command Line Arguments**: Explore how to use `sys.argv` for handling command line arguments in your scripts.


print("book chapter 7")
print(1 + 7 + 3 + 4)    # 15

print(1 + 7 \
      + 3\
         + 4)

prompt = """If you share your name, we can personalize the messages you see.\
What is your first name? """

#book pg 114
print('input:- pg 114')
name = input(prompt)
print(f"\nHello, {name}!")

#age:str = input("How old are you? ")   # input return string
age:int = int(input("How old are you? "))   # type casting
age >= 18

print('modulo oprator:- pg 116')

# find out even and odd number

data : int = [1,2,3,4,5,6,7,7,8,9,13,44,76]

#if num1 == %2 

numlist : int = [i for i in data]
print('list',numlist)

list1 : list[int] = [i for i in data if i%2==0 ]
print('even number', list1)

list2 : list[int] = [i for i in data if i%2!=0 ]
print('odd number', list2)

# Avoiding Infinite Loops pg- 122
#infinite loop (control c / vs code stop button :- to stop infinite loop )
# current_num : int = 0
# while current_num < 20:
#     if current_num%2 == 0:
#         print(f'odd number {current_num}')
    # else:
    #     print(f'even number {current_num}')

# pg 122
print('\nwhile loop')
current_num : int = 0
while current_num < 5:
    current_num += 1    # increment important (break loop)
    if current_num%2 == 0:
        print(f'even number {current_num}')
    else:
        print(f'odd number {current_num}')

# pg - 122
print('\ncontinue:- skipping the iteration when num%2 == 0')
curr_number = 0
while curr_number < 5:
    curr_number += 1
    if curr_number % 2 == 0:
        continue         
    print(curr_number)

# pg 124
print('\nMoving Items from One List to Another')
# Start with users that need to be verified,
# and an empty list to hold confirmed users.

unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []
# Verify each user until there are no more unconfirmed users.
# Move each verified user into the list of confirmed users. 

while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print(f"Verifying user: {current_user.title()}") 
    confirmed_users.append(current_user)
    
# Display all confirmed users.
print("\nThe following users have been confirmed:") 
for confirmed_user in confirmed_users:
    print(confirmed_user.title())
        
#if list has any value while become true
# checkvalue : str = 'checking'  
# while checkvalue :
#     print(checkvalue)

a = 'pakistan'

while a:
    print("first")
    break

b = 10
while b:
    print('second')
    break

datalist : list[int] = [1,2,3]

while datalist:
    n : int = datalist.pop()
    print(n)
print(datalist)

pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat'] 
print(pets)

while 'cat' in pets:
    pets.remove('cat')
print(pets)

