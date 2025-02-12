import math
a, b = int(input()), int(input())
print(math.gcd(a, b))
print(abs(a * b) // math.gcd(a, b))