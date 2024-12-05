lst = [2,3,4,5]
result = list(map(lambda n:n*2,lst))
print(result)

#reduce function
from functools import reduce

lst = [5,10,15,20]
result=reduce(lambda x,y:x+y,lst)
print(result)

