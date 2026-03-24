#single inheritance
#person class
class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_detail(self):
        return f"Myname is {self.name} and my age is {self.age} years old"
            
#Employee class
class Employee(person):
    pass
p = person("ravi", 25)
e = Employee("Siva",31)
print(e.show_detail())
