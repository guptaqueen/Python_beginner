class Student:
    major = 'CSE'

    def __init__(self,rollno,name):
        self.rollno=rollno
        self.name=name

s1=Student(1,"john")
s2=Student(2,"Hari")
print(s1.major)
print(s2.major)
print(s1.name)
print(s2.rollno)
print(Student.major)