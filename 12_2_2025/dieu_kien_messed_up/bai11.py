inp = int(input())
if inp < 50: print(inp * 2000)
if inp >= 50 and inp <= 100: print((50 * 2000) + ((inp - 50) * 3500))
if inp > 100: print((50 * 2000) + (50 * 3500) + ((inp - 100) * 5500))