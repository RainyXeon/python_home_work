import math
l = [int(i) for i in input().split(' ')]
p = sum(l) / 2
out = open('./OUT', 'w+', encoding='utf8')
out.write(str(round(math.sqrt(p*(p-l[0])*(p-l[1])*(p-l[2])), 3)))