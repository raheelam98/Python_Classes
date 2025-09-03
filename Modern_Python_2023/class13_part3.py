# Super().__init__(arg_parent) :- call parent initializer 
# super() = Function used to give access to the methods of a parent class.
#super() :-  Returns a temporary object of a parent class when used

class Employee():
    def __init__(self, emp_name: str) -> None:
        self.e_name : str = emp_name
        self.education : str = ""
        self.department : str = ""

class Designers(Employee):
    def __init__(self, designer_title : str, emp_name: str) -> None:
        super().__init__(emp_name) # include all artibutes of Employee class 
        self.des_title : str = designer_title

class Developers(Employee):
    def __init__(self, developer_title : str, emp_name: str) -> None:
        super().__init__(emp_name) # include all artibutes of Employee class 
        self.dev_title : str = developer_title
        self.dev_skills : list[str] = ["Python", "JS"]

obj_employee : Employee = Employee("Akbar")
obj1_designer : Designers = Designers("Animated Artis", "Raheel")
obj2_developer : Developers = Developers("AI Engineer", "Rashid")


print(obj_employee.e_name)
print(obj1_designer.des_title)
print(obj2_developer.dev_title)
print(obj2_developer.dev_skills)