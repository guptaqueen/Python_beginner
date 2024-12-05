dict={1:"Ram",2:"Hari"}
print(type(dict))
print(dict.items())

k=dict.keys()
for i in k:print(i)

v=dict.values()
for i in v:
    print(i)

    print(dict[2])

del dict[1]
print(dict)