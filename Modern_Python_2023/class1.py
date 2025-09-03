
print("class1")
#everything in python is object (???)
#pythong is dynamic language 
#Python, variables are dynamically typed, which means you can assign values of different types to a variable
# mypy, a static type [ give TypeError]
# String
#str is object in python 

name1 = "Python Old Style" #old style we can change the type
print(name1)             # print variable :- Python Class
print(type(name1))       # type of variable :- <class 'str'> 
print(id(name1))         # physical address :- 4430070896

print(dir(name1))        # give methods of variable 

print([i for i in dir(name1) if "__" not in i]) # methods and attribute

name1 = 123   #old style we can change the type (not good)
print(name1)

fname : str = "Python New Way"  # restrict-datatype:-  var : datatype = value
print(fname)

fname = 123  #  type-error :- fname: string can't change type (restrict-datatype)
# mypy your_python_file.py (shows all errors we generate)

#datatypes
rollnumber = 123
print(rollnumber) # print

percentage : float = 7.0
print(percentage) # print

result : bool = True
print(result) # print

myList : list[str] = ['a','b','c']
print('list[str] ', myList) # print

#tuple :- immutable (unchanging)
mytuple : tuple[str,int,float] = ('pakistan',7,2.0)
print('tuple(immutable) ', mytuple) # print

mytuple2 : tuple[str,int,float] = ('pakistan',7,"aaa")  
print(mytuple2) # print

transport : any = "Pakistan"
print(transport) # print


# after installing mypy, restrict type but not give error       
lname : str = "my string"
lname = 123

# display() is not working

