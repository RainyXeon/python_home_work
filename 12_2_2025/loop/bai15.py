import random
sec_key = random.randrange(1, 100)

while True:
  user = int(input('So can tim la bao nhieu ? '))
  if user == sec_key: print('Chuc mung ! Ban da tim ra duoc so bi mat !!!'); break
  if user > sec_key: print('Be hon !')
  if user < sec_key: print('Lon hon !')