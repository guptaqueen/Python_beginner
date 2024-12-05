class Programmer:

    def setName(self,n):
        self.name = n

    def getName(self,sal):
        self.salary = sal
    
    def setSalary(self,techs):
        self.technology = techs

    def getSalary(self):
        return self.salary
    
    def setTechnologies(self,techs):
        self.Technologies = techs
    
    def getTechnologies(self):
        return self.Technologies


p1 = Programmer()
p1.setName("John")
p1.setSalary(10000)
p1.setTechnologies(["Java","Python","CSS","HTMl"])

print(p1.getName)
print(p1.getSalary)
print(p1.getTechnologies)

