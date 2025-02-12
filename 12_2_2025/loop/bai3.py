e = 0
o = 0
process = 0
while process != 1:
  inp = int(input())
  if inp % 2 == 0: e += 1
  else: o += 1
  if e == o: process = 1
print(e)