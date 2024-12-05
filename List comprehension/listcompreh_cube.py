# lst=[]
# for i in range(1,11):
#      lst.append(i**3)
# print(lst)

lst = []
lst = [x**3 for x in range(1,11)]
print(lst)

#even number
# lst = []
# lst = [x for x in range(2,21,2)]
# print(lst)

lst=[x for x in range(1,21) if x%2==0]
print(lst)

#product of two number
a=[1,2,3,4,5]
b=[6,7,8,9,10]

z=[]

'''for i in range(len(a)):
    z.append(a[i]*b[i])
print(z)'''

z=[a[i]*b[i] for i in range(len(a))]
print(z)