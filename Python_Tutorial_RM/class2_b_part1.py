print('data type, mutable and imutable\n')

#Mutable Data Types (can modify mutable object) :-  list, dict (dictionary), set
#Immutable ( can’t modify immutable object. When modify new object will created and with modify value)
#Immutable Data Types :-  int, float, str, tuple, frozen set
# mutable (changeable) list, dict (dictionary), set
# memory location:- print(id(x))

# ======  mutable (changeable) list, dict, set  ======
print('\n mutable (changeable) list, dict, set')

fruit_list : list[str] = ['apple', 'orange']
print(fruit_list)    # output :- ['apple', 'orange']
# memory location:- print(id(x))
print(id(fruit_list))   # output :- 4354312448
fruit_list[0] = 'banana'   # output :- ['banana', 'orange']
print(fruit_list)
print(id(fruit_list))   # output :- 4354312448  
# note memory location don't change

# ====== Immutable (can't change) int, float, str, tuple ======
print(f"\n Immutable (can't change) int, float, str, tuple")

mess = "hello"
print(mess)     # output :- hello
print(id(mess)) # output :- 4410761808
mess = "hi"
print(mess)     # output :- hi
print(id(mess)) # output :- 4407261408  (note memory location is change, new location)
# note :- create new string object when modify the value

# now changing the memory location (give error)
#mess[0] = "whatsup" (TypeError: 'str' object does not support item assignment) 

# ====== F-strings (formatted string literals) ======
# note :- F-strings :- (1) combine different data type (2) multiple lines
print('\n F-strings (formatted string literals)')
name = 'Asim'
age = 30
# print({name} + {age})  # TypeError:we can't combine different data type 
print(f"Hello, My name is {name} I'm {age} years old.")
# multiples lines
print(f"""
      Hello, My name is {name} 
      I'm {age} years old.
      """)