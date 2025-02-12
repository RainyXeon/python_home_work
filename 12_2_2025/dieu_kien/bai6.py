import math
inp = [int(x) for x in input().split(' ')]
d = (inp[1] ** 2) - (4 * inp[0] * inp[2])
if d < 0: exit()
elif d == 0: r = (-inp[1]) / (2*inp[0]); print(r); print(r)
else:
  print((((-inp[1]) + math.sqrt(d)) / (2*inp[0])))
  print((((-inp[1]) - math.sqrt(d)) / (2*inp[0])))