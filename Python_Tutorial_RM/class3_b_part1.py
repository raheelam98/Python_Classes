print('variables')

# naming and using variable (book page 16)
# variable_name :- name must be start with letter or _ (underscore)
# don't use space and key_words

# string is a series of characters (anything inside single/ double quotes) pg-19

#methods_str : str = [i for i in dir(str) if "__" not in i]
#print(methods_str)

message : str = 'we are expert in python'
_message : str = "I am champion in python"

print(message.title()) # change first letter to upper case

mess : str = '   right hello  '
print(mess.rstrip())
