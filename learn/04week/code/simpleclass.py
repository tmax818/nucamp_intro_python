

class Student:
    def __init__(self, name):
        self.name = name


class Class:

    students = []

    def __init__(self, name, student):
        self.name = name
        Class.students.append(student)


stu1 = Student("Josh")
myclass = Class("Python", stu1)
