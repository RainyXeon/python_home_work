inp = [int(x) for x in input().split(' ')]
c1 = inp[0] + inp[1] > inp[2]
c2 = inp[0] + inp[2] > inp[1]
c3 = inp[1] + inp[2] > inp[0]
print('CO') if c1 and c2 and c3 else print('KHONG')