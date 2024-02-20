a = input("Data: ").split()
feq = []
stringData = []

def checker(data):
    counter = 0
    for i in a:
        if (i == data):
            counter = counter + 1
    if (counter > len(feq)):
        if (len(feq) == 0 and len(stringData) == 0):
            feq.append(counter)
            stringData.append(data)
        else:
            feq[0] = counter
            stringData[0] = data

for i in a:
    checker(i)

print("Chuoi con xuat hien nhieu nhat la", stringData[0])
print("Xuat hien", feq[0], "lan")