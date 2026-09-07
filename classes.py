'''
class anything:
    pass
print(anything)


# creating instances
class student:
    pass
student1 = student()
student2 = student()
student3 = student()

print(student1)
print(student2)
print(student3)
'''

# initializing attributes with init and self
class student:
    def __init__(self, name, course):
        self.name = name
        self.course = course
Student1 = student("Alex", "Python")
Student2 = student("Dominion", "Go")
print(Student1.name)
print(Student1.course)
print(Student2.name)
print(Student2.course)

class Student:
    def __init__(self, name, course):
        self.name = name
        self.course = course


student1 = Student("Alex", "Python")

print(student1.name)

student1.name = "Michael"

print(student1.name)