s = 'abcbbbccccZZZZIII'
temp =[]
for c in s:
    temp.append(c)
print(temp)
output = ''.join(temp)
print(output)

# count the character
s = 'aaaabbbbbccccczidldklgjgdsl'
d = {}
for c in s:
    if c in d.keys():
        d[c] = d[c]+1
    else:
        d[c] = 1
for k,v in d.items():
    print('{}={} times' .format(k ,v))