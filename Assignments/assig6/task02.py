class Person:
    def __init__(self, name, contact_numbers):
        self.name = name
        self.contact_numbers = contact_numbers

class Student(Person):
    def __init__(self, name, contact_numbers, department, semester):
        super().__init__(name, contact_numbers)
        self.department = department
        self.semester = semester

class Teacher(Person):
    def __init__(self, name, contact_numbers, course, office_number):
        super().__init__(name, contact_numbers)
        self.course = course
        self.office_number = office_number

class TA(Student, Teacher):
    def __init__(self, name, contact_numbers, department, semester, course, office_number):
        Person.__init__(self, name, contact_numbers)
        Teacher.__init__(self, name, contact_numbers, course, office_number)
        Student.__init__(self, name, contact_numbers, department, semester)
ta = TA("John Doe", "1234567890", "Computer Science", 2, "Artificial Intelligence", "9876543210")

print(ta.name)
print(ta.contact_numbers)
print(ta.department)
print(ta.semester)
print(ta.course)
print(ta.office_number)