inp = int(input())
for i in [[10000000, 10], [5000000, 8], [2000000, 7], [1000000, 5], [500000, 2]]:
  if inp > i[0]:
    print(inp - ((inp / 100) * i[1]))
    break