l = int(input())
res = []
for x in input().split(' '):
  x = int(x)
  if x < 0: res.append(x)
print(sum(res) / len(res))