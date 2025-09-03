# time 1: 10
#controls:-  (1) break, (2) continue (skip in particular path), (3)pass
print('\ncontrols:-  (1) break, (2) continue (skip in particular path), (3)pass')

for i in range(1,5):
    print(f'Table  2 x {i} = {i*2}')

# use of break:- first test single value than apply on database
print('\nbreak:- i == 2')
for i in range(0,5):  # range(0, n-1)
    print(f'range is {i}')
    if i == 2:  # output :- range is 0  range is 1  range is 2
        break

print('\nbreak')
for i in range(1,5):
    print(f'2 x {1} = {1*2}')   # output:- 2 x 1 = 2
    break

print('\ncontinue:-  i == 3')
for i in range(1,5):
    if i == 3:
        continue  # Skipping the iteration when i is 3
    print(i)  # output:- 1  2 4
        
print('\npass:-')
for i in range(1,100):
    pass
print(i)  # output 99

print('\npass:-function take int and return int')
#def fun(int a, int b) -> int:
def fun(num1:int, num2:int) -> int:
    pass

if True:
    pass

print("pakistan")
print("Second")
# output:- pakistan  Second

# if True:
#     name : str = input("Your name?")
#     print(name)

if False:
    name : str = input("Your name?")
    print(name)

