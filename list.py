lst=[10,20,'Manisha',-10]
print(lst)
print(len(lst))
print(lst[2])
print(lst*3)

lst.append(40)
lst.remove('Manisha')
del(lst[1])
print(lst)

# lst.clear()
# print(lst)

print(max(lst))
print(min(lst))

lst.insert(3,99)
print(lst)

lst.sort(reverse=True)
print(lst)