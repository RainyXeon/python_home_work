import random
inp = int(input())
total = 0
count = 0

while total <= 2017:
  total += random.randrange(1, inp)
  count += 1

print(total / count)