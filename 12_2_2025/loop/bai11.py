inp = int(input())
c = 0
for i in range(1, inp + 1):
  if inp % i == 0: c += 1
if c > 2: print('NO')
else: print('YES')