try:
    f=open("myfile","w")
    a,b = [int(x) for x in input("enter the  two number:").split()]
    c=a/b
    f.write("Write %d into file" %c)
    f.close()
    print(c)
except ZeroDivisionError:
    print("Division by zero is not allowed")
    print("Please Enter the non zero number")
finally:
    f.close()
    print("file Closed")
print("Code after the exception")

