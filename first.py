class Student:

    def __init__(self, name, major, age, is_on_probation):
        self.name = name
        self.major = major
        self.age = age
        self. is_on_probation = is_on_probation



student_1 = Student("Mike", "history", 27, True)
student_2 = Student("John", "marketing", 25, False)
student_3 = Student("Maks", "marketing", 23, False)


print(student_1.name)
print(student_2.name)   
print(student_3.major)