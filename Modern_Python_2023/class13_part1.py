print("class 13 : OOP (class, method, attributes, class variable, inheritance, super")

# OOP (Object Oriented Programming)
# 1) Class method :-  first argument must be additional variable (self, this, or anything else)
# 3) Class variable :- (this value use for all objects)  ClassName.class_variable
# 4) constructor :-  def __init__(self, arg1: dataType, arg2: dataType) -> return_datatype
# Note (constructor):- method is use to initialize attributes on the instance
# 2) Class attribute :-  (connect with individual object) self.attribute_name = value
# self: Refers to the instance of the class itself
# class ClassName():
#     class_variable1 : type = Value
# Syntax of class :-   class ClassName():    pass
# call a method :- myobject.method(arg1, arg2)

# class Teacher():
#     def __init__(self, teacher_id:int, teacher_name:str) -> None:    # constractor
#         self.tech_id : int = teacher_id   #self.attribute_name = value
#         self.tech_name : str = teacher_name
#         self.organization_name : str = "PIAIC"

#         def speak(self, words : str) -> str:    # method
#             message1 = f"{self.tech_name} speaks {words}"
#             print(message1)
#             return message1
    
        # def teaching(self, subject : str) -> None:   # method
        #     print(f"{self.tech_name} is teaching {subject}")

class Teacher1():
    def __init__(self, teacher_id: int, teacher_name: str) -> None: # constractor
        self.tech_id: int = teacher_id  #self.attribute_name = value
        self.tech_name: str = teacher_name
        self.organization_name: str = "PIAIC"

    def speak(self, words: str) -> str:      # method 1
        message1 = f"{self.tech_name} speaks {words}"
        print(message1)
        return message1
    
    def teaching(self, subject : str) -> None:   # method 2
        message2 = f"{self.tech_name} is teaching {subject}"
        print(message2)
        return message2
    
#intialize object-> (calling constructor)  __init__() method only this time
# obj1 is object or teacher class instance

# Creating an instance of the Teacher class
obj1 = Teacher1(1, "Mike")

# Accessing attributes
print(obj1.tech_id)     # 1
print(obj1.tech_name)   # Mike

# Calling methods
result1 = obj1.speak("about AI")     # output : Mike is speaking learn AI

result2 = obj1.teaching("Python")

#  ----------- **** ------------

# Class variable
# this value use for all objects
# ClassName.class_variable
# object_name.class_variable
# class ClassName():
#     class_variable1 : type = Value

class Teacher2():
     counter : int = 0 # class variable1
     help_line_number : str = "0312-123456" # class varaible2

    # def __init__(self, teacher_id:int, teacher_name:str) -> None:
    #     self.id: int = teacher_id
    #     self.name: str = teacher_name
    #     self.organization_name: str = "PIAIC"
    #     Teacher2.counter += 1

     def __init__(self, teacher_id: int, teacher_name: str) -> None:
        self.teach_id: int = teacher_id
        self.teach_name: str = teacher_name
        self.organization_name: str = "PIAIC"
        Teacher2.counter += 1
            
                       
    # def details(self) -> None:
    #     information : str = f""" 
    #     Teacher name is {self.name}
    #     our help line number is {Teacher2.help_line_number}
    #     """
    #     print(information)
    
     def details(self) -> None:
        information: str = f""" 
        Teacher name is {self.teach_name}
        our help line number is {Teacher2.help_line_number}
        """
        print(information)

# Creating an instance of the Teacher class
obj2 : Teacher2 = Teacher2(1, "Asma")
obj3 : Teacher2 = Teacher2(2, "Khan")

print(Teacher2.counter, obj2.counter)
print(Teacher2.counter, obj3.counter)

print(id(obj2)) 

print(obj2.counter)
print(obj3.counter)
print(Teacher2.counter)

print(obj2.help_line_number)
print(obj3.help_line_number)
print(Teacher2.help_line_number)

obj2.details()








