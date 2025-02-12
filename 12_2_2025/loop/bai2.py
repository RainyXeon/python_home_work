res = 1
process = 0
while process != 1:
  inp = int(input())
  if inp != 0: res = res * inp
  else: process = 1
print(res)