import random
a, b = int(input()), int(input())
res = []
c = 0

while c < 1000:
  c += 1
  if len(res) == 4: break
  rand = random.randrange(a, b)
  count = 0
  for i in range(1, rand + 1):
    if rand % i == 0: count += 1
  if count == 2:
    res.append(rand)

if len(res) == 4: print(res)
else:
  print(res)
  print(-1)