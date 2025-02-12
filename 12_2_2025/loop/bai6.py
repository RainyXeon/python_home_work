inp = int(input())
arr = []
for i in range(1, inp + 1):
  if inp % i == 0: arr.append(str(i))
print(' '.join(arr))
