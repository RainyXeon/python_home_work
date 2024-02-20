a = input("Data: ").split()
currIndex = 0

for i in a:
    if (len(a[currIndex]) < len(i)):
        currIndex = a.index(i)
    elif (len(a[currIndex]) == len(i)):
        if (a[currIndex] < i):
            currIndex = a.index(i)
        else: pass
    else: pass
    
    
print("Chuoi con dai nhat la", a[currIndex])