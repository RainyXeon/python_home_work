a = int(input())
out = open('./OUT', 'w+', encoding='utf8')
out.write(str(round(a ** (1/2))) + '\n' + str(a ** 2))