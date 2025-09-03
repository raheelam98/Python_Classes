print('\nFile Handling')  # time 30
# https://www.geeksforgeeks.org/reading-writing-text-files-python/

data_file = open("./abc.txt")
print(data_file)
# output:- <_io.TextIOWrapper name='./abc.txt' mode='r' encoding='UTF-8'>

print('\nmethods of abc.txt ')
file_methonds : list[str] = [i for i in dir(data_file) if "__" not in i]
print(file_methonds)

print('\nopen abc.txt ')
print(open("./abc.txt"))
# output:- <_io.TextIOWrapper name='./abc.txt' mode='r' encoding='UTF-8'>

print('\ntype of abc.txt ')
print(type(data_file))
# output:- <class '_io.TextIOWrapper'>

# note:- search type of class in chatGPT
# data_file = open("./abc")
# convert python code with python static type

from typing import TextIO

# note:- we require object to return the data of file then use open()
# note:- when ever we open() for connectivity must use close() for discontion
data_file.TextIO = open("./abc.txt")   # connectivity with abc.txt file
print(data_file.read())
print(data_file.close())   # close the connectivity with abc.txt file
# output:-  line 1
# output:-  line 2
# output:-  line 3

print("\nuse with to create local variable ")
# rule: when ever create file it is static (double check)
# with :- create local variable (when lot of code and user forget to close() the file)
# local variable automatically finish when ever we come out from block

with open("./abc.txt") as file_variable:  # type: TextIO
    print(type(file_variable))   # output :- <class '_io.TextIOWrapper'>
    print(file_variable.read())  # read all the lines

print("local varible vanish: when ever come out from block")

# read() :- read file in one go, 
# readlines() read line by line (in form of iteration, so we use logic )
# readline()[] :- use slicing[] to read specific line

print("\nreadlines(),return list and read lines in form of iteration ")
with open("./abc.txt") as file_variable:  # type: TextIO
    print(type(file_variable))   # output :- <class '_io.TextIOWrapper'>
    print(file_variable.readlines())   # readlines() -> return list 
# output :- ['line 1\n', 'line 2\n', 'line 3\n']

print("\nreadline()[slicing], to read specific lines ")
with open("./abc.txt") as file_variable:  # type: TextIO
    print('read line by line : readline()')
    print(file_variable.readline())  # output:- line 1
    print(file_variable.readline())  # output:- line 2
    print('read portion readline()[:3]')
    print(file_variable.readline()[:3]) # output:- lin
# note :- readline() function end with backslash n
# note:- to remove the space use print function end 

print("\nremove space between lines ")
with open("./abc.txt") as file_variable:  # type: TextIO
    print('read line by line : readline()')
    print(file_variable.readline(), end="")  # output:- line 1
    print(file_variable.readline(), end="")  # output:- line 2
 
print("\nmode :- r(Read-only)  w(Write-only)  a(Append-only)  (note:- default mode of file is r)")
# modes:-  r – Read-only mode.      w – Write-only mode.   a – Append-only mode. 
# modes:-  r+ – Read + Write mode.  w+ – Write + Read mode.
# modes:-  a+ – Append + Read mode.
    
print("default mode of file is r ")
with open("./abc.txt", 'r') as file_variable:  # type: TextIO
    print(file_variable.readline())  # output:- line 1
   # print.write('write on file ')  # AttributeError: object has no attribute 'write'
        
print("w – Write-only mode. (overrite ) (cannot read)")
with open("./abc1.txt", 'w') as file:  # type: TextIO
    file.write("Python is easy to learn") 
    #print(file_variable.readline())  # error:-  not readable   (file name different)

print("\nr+ – Read + Write mode (write at end) ")
with open("./abc2.txt", '+r') as file:  # type: TextIO
    print('before')
    print(file.read(), end="")
    file.write("\tWe are strong in Python ")  # after writting text, cursor become at end
    print('After: empty (read() :- cursor become at the end position after writting text) ')
    print(file.read())
# note :- cursor position is at the end, empty because after that nothing is written

    # time 1:02
    #print(file_variable.readline()) # ValueError: I/O operation on closed file.
    print('\nseek(0) cursor(index 0) place the cursor back at the beginning of the file')
    with open("./abc3.txt", 'r+') as file:  # type: TextIO
        print('Before')
        print(file.read(), end="")    # output:- Python class 3
        file.write("\tWe love our country!")
        file.seek(0)
        print('\nAfter :- file.seek(0) ') # output:- Python class 3  We love our country!
        print(file.read())
    

# Now change modes
print('Now change modes')

print('r :- ')
# with open("./abc6.txt", 'r') as file:  # FileNotFoundError: 
#     print(file.read()) 

print('w :- overwrite in file, if file is not there create new file ')  
with open("./abc4.txt", "w") as file:
    print(file.write('write if empty, other wise overwrite'))
# if file exist then it overwrite the text
# if file not exist then it will create new file

print('\na – Append-only mode')    
with open("./abc5.txt", 'a') as file:  # type: TextIO
    print(file.write("\tPakistan"))  

# if file exist then it write the text
# if file not exist then it will create new file
    
with open("./abc5.txt", 'a') as file:  # type: TextIO
    print(file.write("\tline3")) 

# if file not exist then it will create new file
# add content at end
    
print('\nx – mode :- if file not exist then it will create new file') 
print('x – mode :- if file is exist give error') 

# with open("./abc5.txt", 'x') as file:  # type: TextIO
#     # print(file.read())
#     file.write("line3") 

print('rb+ :- read and open in binary')
with open("./abc6.txt", 'rb+') as file:  # type: TextIO
    print(file.read())
    # file.write("line3") 


# convert exiting file into binary 
    
# https://stackoverflow.com/questions/6648493/how-to-open-a-file-for-both-reading-and-writing




        

