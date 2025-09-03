print('Class 12 :- Error Handling, File Handling and create own error class')

print("Handle multiple error ")
print("logic1")

l1 : list[int] = [1,2,3]

try:
    print('5/2 : ',5/2)
    print(f'l1[0] : {l1[0]}')
    print(f'l1[10] : {l1[10]}') # Index Error
    print('5/0 : ',5/0)    # Zerro Division Error!
    # print(xyz) # error
    open(f"aa.txt",'wrong file name ')
except (ZeroDivisionError):
    print("Zerro Division Error!")
except IndexError:
    print("Index Error")
except NameError:
    print(f"Name not defined")
except:
    print("Some thing is wrong!")

print("logic4")
print("logic5")

print("\nHandle Any kind of error use Exception Class")

try:
    # print(age)
    print(l1[200])  # list index out of range
except Exception as e:
    print(f"Some thing is wrong!\n{e}")

print('\nGenerate Error')
print('if student age is age<18 or age> 60 cannot enroll for course' )

#  def __init__(self, data)  (initializes a newly created object)
# __init__() function is called automatically every time the class is being used to create a new object.

class StudentCard():
    #def __int__(self, name:str,  age:int ) -> None:  # error init TypeError
    def __init__(self, name:str, age:int) -> None:
        pass
        if age < 18 or age > 60:
            raise StudentAgeError('You are not eligible for this program!')
        self.name = name
        self.age = age

            # self.name = name  # TypeError: StudentCard() takes no arguments
            # self.age = age    # problem of indentation
        
# Custom error class
class StudentAgeError(Exception):
    pass

student1 = StudentCard('Ali', 50) #output:- Ali 50
print(student1.name, student1.age)

# output:- student2 = StudentAgeError('Akbar', 40)
# output:- print(student2.name, student2.age)  # AttributeError: 'StudentAgeError' object has no attribute 'name'

student2 = StudentCard('Sun', 60)  
print(student2.name, student2.age)  #output:- Sun 60

# output:- student3 = StudentCard('A', 61)
# output:- print(student3.name, student3.age) 
# output:-  StudentAgeError: You are not eligible for this program!

