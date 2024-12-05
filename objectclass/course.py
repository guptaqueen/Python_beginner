class Course:

    def __init__(self,name,rating):
        self.name = name
        self.rating = rating
    
    def average(self):
        numberofRating = len(self.rating)
        average = sum(self.rating)/numberofRating
        print("Average rating For ",self.name, "Is" ,average)

c1 = Course('Java Course',[1,2,3,4,5])
print(c1.name)
print(c1.rating)
c1.average

c2 = Course('Web development',[5,6,7,8])
print(c2.name)
print(c2.rating)
c2.average