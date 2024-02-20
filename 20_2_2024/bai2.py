a = input("Nhập 1 chuỗi: ")
b = input("Nhập 1 ký tự: ")
count = 0

for i in a:
    if (i == b):
        count = count + 1

print("Kí tự", b, "xuất hiện", count, "lần")