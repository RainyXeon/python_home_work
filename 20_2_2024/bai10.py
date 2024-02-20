a = input("Nhap chuoi: ")
b = input("Chuoi con: ")
count = 0

for i in a.split():
    if (i == b):
        count = count + 1

print("Xau", b, "xuat hien", count, "trong xau", a)