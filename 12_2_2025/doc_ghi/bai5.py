inp = int(input())
open('./OUT', 'w+', encoding='utf8').write(
  str(((inp + 1) * ((inp - 1) + 1)) / 2)
)