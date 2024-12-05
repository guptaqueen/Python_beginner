''' s = input("Enter the string")
 print(s[::-1])

s =input("Enter the string")
i =len(s)-1
result = ''
while i >= 0:
    result = result+s[i]
    i = i-1
print(result)'''

# s = ''.join(['a','b','c'])
# print(s)

s = input("Enter the string")
print(''.join(reversed(s)))