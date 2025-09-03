# Python class has 2 main things :- (1) attributes (2) methods
# class attributes :- properties of class (e.g skin colour, hair color)
# class attributes (connect with individual object) :-  self.attribute_name = value
# class methods :- action perform (e.g walk, sleep)
# class varaibles (static):- are same for all objects of entire class (school lunch break time)
# define class_varaible :- class_var_name : datatype = value
# call class_varaible :-  class_name.class_varaible_name  OR object_name.class_varaible_name



class Person():
    counter : int = 0  # define class varaible :- class_var_name : datatype = value
    class_var : str = "Message for All Students"  # class varaible

    # constractor :-  __init__(self, arg1 : datatype, arg2 : datatype) -> return_datatype:
    def __init__(self, person_id : int, person_name : str ) -> None:   # constractor / methond / function
        # class attributes (connect with individual object) :- self.attribute_name = value
        self.p_id : int = person_id      # class attributes
        self.p_name : str = person_name
        self.inform : str = "Classes are available online"
        self.counter += 1    # counter 

        # self: refers to the instance of the class itself
        # 'self' is automatically filled in when you call the method on an instance of the class.
        # 'self' is first_argument in method, use to connect individual object of the class 
        # we can use either  self or this (use anything like xyz, but we use standard self or this)
        # an instance refers to a specific realization of a class
        
    #method1 :- def method_name(self, arg1: data_type) -> return_dataType:
    def status(self, languages : str) -> None:
        message_var1 = print(f""" {self.p_name} has command on {languages}
                            """)

    # method2
    def job(self, current_job : str) -> None:
        message_var2 = print(f""" {self.p_name} works as a {current_job} ...!
                              """)
        
    # method3
    def detail(self) -> None:
        general_mess : str =  f""" {Person.class_var}  Generative AI  {self.inform}
                             """
        print(general_mess)

# creating an instance of the Person class 
# intialize object->calling constructor __init__() method only this time
# obj1 = object OR class instance
 
obj1 : Person = Person(1,"Akbar")

# print(obj1.person_id)    ---> note:- give error,  use "p_id"
# AttributeError: 'Person' object has no attribute 'person_id'

print(obj1.p_id)   #output:- 1
print(obj1.p_name) #output:- Akbar

# Calling method1
obj1.status("Python")  # output:- Akbar has command on Python

# Calling method2
obj1.job("Developer")  # output:- Akbar works as a Developer ...!

# Calling method3
obj1.detail()   # output:- Message for All Students  Generative AI Classes are available online

# Memory allocation 
print(id(obj1))     # output :-  4558876944  (note:- value change every time when run program)

obj2 : Person = Person(2, "Aslam")
print(id(obj2))     # output :-  4571920336
# print(type(obj2))

# class varaibles :- are same for all objects
print(Person.counter)   # call class_varaible:- class_name.class_varaible_name  
print(obj1.counter)     # call class_varaible:- object_name.class_varaible_name
print(obj2.counter)
print(Person.counter, obj1.counter)
print(Person.counter, obj2.counter )

# class varaibles :- are same for all objects
print(Person.class_var)
print(obj1.class_var)
print(obj2.class_var)

# __dic__
print(obj1.__dict__)   # give all the argument




        
    

    