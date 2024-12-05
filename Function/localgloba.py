"""x=123 #global  variable

def display():
    y=678 #local variable
    print(y)

print(x)
display()"""


x=123 #global  variable

def display():
    x=678 #local variable
    print(x)
    print(globals()['x'])

print(x)
# display()

z = display # assign the variable
z()
z()