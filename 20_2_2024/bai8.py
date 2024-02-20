a = input("Data: ")
b = input("Ki tu can tach: ")

def combine(array):
    res = ""
    for i in array:
        res = res + i
    return res

if (len(b) > 0):
    print(combine(a.split(b)))
else:
    print(combine(a.split()))