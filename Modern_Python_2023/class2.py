print("class2")

# concatenate strings :- "a" + "b"  (become ab)
# concatenate string and int :- "a" + "7"  (become a7)
# concatenate :- "a" + str(7)   (anything in str convert into strin)
# backslash '\' convert special character to normal;
# backslash '\' :- place \ before character
# backslash '\' :- use to continue the to next line

# placeholders {} : bring the value of given format
# strings are immutable (can't change)
# String boundries:- 'single', "double",  '''triple single quotes ''', """" triple quotes  """
# multiline string """ string text """, ''' string text '''
# str(7) : convert 7 into string
# F-string python :- f "formatted string literals"
# F-string allow you to include expressions inside curly braces {} within a string
# F-string:- (f triple single/double quotes)  f''' '''  OR f""" ""
# f-strings :- is use placeholders {} include expressions   and numerical formatting in Python.
# F-string  :- f"""   Name : {name}  (placeholders)  """
# Jinja style :- f"""   Name : { {name} }  (placeholders)  """  (use with html)
# #variable_name.method()   (note:- some method require arguments)
# Syntax: f-string along with raw strings
# fr'string or {string}' ,  f'{func()}' , f"{dict['key']}"
# Note : we use f-string (it most easy)
# python predefine global function :- print, type, id, dir, len

# print method : convert into string and then display
# display method : display in same format (e.g list, dic) jupyter note book

#mthods and attributes of string
print("\nString methods and attributes")
print("list comprehension")
mystring : list[str] = [i for i in dir(str) if "--" not in i]
print(len(mystring))  # give length
print(mystring)


message1 : str = 'Piaic Student Card\nFather\'s Name\n '
print(message1)

name : str = "Akbar"
fname : str = "Mahmood"
education : str = "MSc in Computing"
roll_number : int = 221

card1 : str = "Piaic Student Card\nName: " + name +\
             "\nFName : " + fname +\
             "\nEduaction : " + education +\
             "\nRoll : " + str(roll_number)

print(card1)

print(''' \n multiline string, """ """, ''' '''  ''')
print(""" multiline string, """ """, ''' ''' \n""")

card2 : str = """
Piaic Student Card
Name : ...
FName : ...
Education : ...
Roll Number : ..
 """

print(card2)

#.format is use to place things in particular place
# it is f string method
a = 7
b = 3
mess : str = "value of a = {} and value of b = {}".format(a,b)
print(mess)

print("\nF-string:- f triple single/double quotes")

card : str = """   \n# without f
PIAIC Student Card
Student Name : {a}
Father's Name: {b}
Roll_number: {c}
Education : {d}
""".format(a=name, b=fname, c=roll_number, d=education)
print(card)

# card4 : str = f"""   # give error because of f
# Piaic Student Card
# Name : {a}  
# FName : {b}
# Education: {c}
# Roll Number: {d}
#  """.format(a=name, b=fname, d=education, d=roll_number)
# print(card4)

#Recommended below two f-string format
print("\nRecommended below two f-string format")

card3 : str = f"""
Piaic Student Card
Name : {name}  placeholders
FName : {fname}
Education : {education}
Roll Number : {roll_number}
Calculate {2+4+9}
 """
print(card3)

student_code : str = """
print("print any code")
a:int = 3 
b:int = 4
print(a+b)
"""
exec(student_code)

message : str = "     coMMand ON pyTHon    "

#variable_name.method()
print(message.capitalize())  # capitalize only 1st letter of sentence

print(message.casefold())   
# casefold:- convert all letters into small (not follow any case)

print(message.lower())
# lower:- convert all letters into small  
# casefold and lower doing same job but throught is different

print(message.title())
#conver first letter of every word into capital

print(message.lstrip()) # removed space from left

print(message.rstrip())  # remove space from right

print(message.split())   # remove space from left and right but not from middle

print(f"Hello, {message.title()}!")

import re

print("\nSentence with space")
scenario : str = "     coMMand    and         control   ON     pyTHon       "
print(scenario)

query1 : str = re.sub(' {5,100}', '', scenario).strip()
print("\nRemove spacing")

# substitute(pattern, replacement, variable-workon )
query1 : str = re.sub(' {5,100}', '', scenario).strip()
print(query1)

print("\nPharse editing")
print("Name:\t\t backslash t give space")   #\t :- give space
print("Name:\b backslash b remove last character")    #\b :- delete just before thing

print("\nRemove portion of url")
nostarch_url:str = 'https://nostarch.com'
my_url : str = nostarch_url.removeprefix('https://')
print(my_url)

# variable naming conventions
# https://peps.python.org/pep-0008/#function-and-variable-names

#print("Name:\t\t Muhammad Qasim")