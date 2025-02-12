inp = [int(x) for x in input().split(' ')]
if inp[0] == 0 and inp[1] != 0: print('VO NGHIEM')
elif inp[0] == 0 and inp[1] == 0: print('VO SO NGHIEM')
else: print(round((- inp[1]) / inp[0], 3))