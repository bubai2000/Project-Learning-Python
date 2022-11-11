class Student:
    school = 'BCCS'

    def __init__(self, name, roll):
        self.name=name
        self.roll=roll
    def returninfo(self):
        return [self.name, self.roll, self.school]
    def returnschool(cls):
        return cls.school
    def printhello():
        return "Hello"
    @classmethod
    def returnschool2(cls):
        return cls.school

s1=Student("Soumya",1)
print(s1.returninfo())
print(s1.returnschool())
print(s1.school)
print(Student.returnschool(Student))
print(Student.returnschool2())
print(Student.printhello())