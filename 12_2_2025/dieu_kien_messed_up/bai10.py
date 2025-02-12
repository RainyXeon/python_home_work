x = None
inp = [int(x) for x in input().split(' ')]
if inp[0] < inp[1]: x = (inp[0] + inp[1]) / 2
if inp[0] == inp[1]: x = inp[0]
if inp[0] > inp[1]: x = (inp[0] ** 2) + (inp[1] ** 2)
print((inp[0]*(x**2)) + (inp[1]*x) + 5)