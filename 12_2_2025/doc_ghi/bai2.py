a = int(input())
open('./OUT', 'w+', encoding='utf8').write(
  str(2 * 3.14 * (a / 2)) + '\n' + str(3.14 * ((a / 2) ** 2))
)