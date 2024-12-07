import re
str  = "Take 1 up one 123 idea 45 idea at  Time"
result = re.search(r'o\w',str )
print(result.group())

result = re.findall(r'o\w\w',str )
print(result)

result = re.match(r'T\w\w',str )
print(result.group())

result = re.sub(r'One','Two',str )
print(result)

result = re.findall(r'O\w{1,2}',str)
print(result)

reult = re.split(r'\d+',str)
print(result)