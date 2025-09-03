
class Teacher:
    def __init__(self, teacher_id: int, teacher_name: str) -> None:
        self.tech_id: int = teacher_id
        self.tech_name: str = teacher_name
        self.organization_name: str = "PIAIC"

    def speak(self, words: str) -> str:
        message1 = f"{self.tech_name} is speaking {words}"
        print(message1)
        return message1

# Creating an instance of the Teacher class
obj1 = Teacher(1, "Mike")

# Accessing attributes
print(obj1.tech_id)
print(obj1.tech_name)

# Calling the methods
result = obj1.speak("learn AI")
print(result)
