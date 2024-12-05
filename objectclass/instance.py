class product:

    def __init__(self):
        self.name = 'Iphone'
        self.description ='Its Awesome'
        self.price = 700
    
    def __del__(self):
        print("Inside thedestructor")

    def display(self):
        print(self.name)
        print(self.price)
        print(self.description)

p1 = product()
p1.display()
p1 = None

p2 = product()
p2.display()