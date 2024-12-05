class Student:
    def __init__(self):
        self.__id=123
        self.__name="hari"

    def display(self):
         print(self.__id)
         print(self.__name)

s = Student()
# print(s.__id)
# print(s.__name)
s.display() #or
print(s._Student__id);