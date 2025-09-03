# OOP :- Inheritance, Encapsulation, Polymorphism, Abstraction
# Inheritance :- parent child relation (chid inherit from parent like voice)
# Inheritance :- class ChileClass(ParentClass):   pass  (child get the the properties from parent)
#class ChildClass(ParentClass):
#    def __init__(self, arg1, arg2, ...):
#        super().__init__(arg1, arg2, ...)

class Parents():
    def __init__(self) -> None:
        self.eye_color : str = "Brown"
        self.hair_color : str = "Black"

    def speak(self, words:str) -> None:
        print(f"Parents talk about : {words}")

    def look(self, object_names: str) -> None:
        print(f"Parents are seeing : {object_names}")

class Child1(Parents):
    pass

# parent object
print("---- parent object ----")
obj1_parent : Parents = Parents()
print(obj1_parent.eye_color)
print(obj1_parent.hair_color)

obj1_parent.speak("their ancestor")
obj1_parent.look("family heritage")


# child1 object
print("---- first child object ----")
obj2_child1 : Child1 = Child1()
obj2_child1.speak("first child behaviour")
obj2_child1.look("first child's development")

print(obj2_child1.eye_color)
print(obj2_child1.hair_color)

# child2 object
print("---- second child object ----")
class Child2(Parents):
    def learning(self, subjects : str) -> None:
        print(f"2nd Child Method : Second child is learning {subjects}")

obj3_child2 : Child2 = Child2()
obj3_child2.speak("second child achievements")
obj3_child2.look("second child certificates")
obj3_child2.learning("Python")

print(obj3_child2.eye_color)
print(obj3_child2.hair_color)
