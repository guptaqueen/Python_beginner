def decor(fun):
    def inner():
        result = fun()
        return result*2
    return inner

@decor
def num():
    return 5

# resultfun = decor(num)
# print(resultfun())
print(num())

    