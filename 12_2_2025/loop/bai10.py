inp = int(input())
c = 0
for i in range(1, inp + 1):
  print(' ' * (inp - i) + '*' * (i + c) + ' ' * (inp - i)); c += 1