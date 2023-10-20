p = 29
ints = [14, 6, 11]
quad = []
resA = []
for i in range(1, p):
  a = i
  b = p - i
  if a ** 2 % p == b ** 2 % p:
    if a ** 2 % p in ints:
      resA.append(a)
      quad.append(a ** 2 % p)

print(min(resA))