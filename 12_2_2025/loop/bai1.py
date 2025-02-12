res = []
process = 0
while process != 1:
  inp = int(input())
  if inp != 0: res.append(inp)
  else: process = 1
print(sum(res))