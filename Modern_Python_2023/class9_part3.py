# store values
# 1- input from user:- 1) input function (defualt type = string)  
# 2- input from user:- 2)sys.argv (for console input in abc.py file) defualt type = str

# user_input : str = input('Enter Name:\t')
# print(type(user_input))
# print(f'Welcom to Python class {user_input}')

# time 58
print('\ncreat database by user-input dict (e.g. name) and store ')

data : list[dict[str,str]] = []
flag : bool = True

while flag:
    print('write quit or exit to stop this program')
    name : str = input('Your Name? \t')
    education : str = input('Your Education?\t')

    # put condition (otherwise loop become infinite) use list
    #if name not in ['exit', 'quit', 'stop', 'close'] or education not in ['exit', 'quit', 'stop', 'close']:
    if name and education in ['exit', 'quit', 'stop', 'close']:  #or education in ['exit', 'quit', 'stop', 'close']: 
        flag = False
        break

    # add data through dict (loop run untill quit/exit) put condition 
    data.append({'name':name,
                 'education': education })
    
    print(data)
    


