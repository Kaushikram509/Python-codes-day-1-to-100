#Types of attributes
#1> Class attributes
class Student:  
    school_name = "Sreenidhi"  #class attribute
    def __init__(self, name, age): #--------------> Initialization constructor
        self.name = name   #instance attribute
        self.age= age      #instance  attribute
    def details(self):          #method
        return f"My name is {self.name} and I am a {self.age} years old"
#object Creation
s1 = Student("Ravi", 14)
s2 = Student("Babu", 13)
print(s1.name)
print(s1.name)
print(s1.details())
print(s1.school_name)
