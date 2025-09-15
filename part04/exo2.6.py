n: int = 14
for i in range(2, n//2 + 1):
  a: str = ''
  for k in reversed(range(n)):
    if(k%i) == 0 and k != 0:
      a += ' ' + str(k) # print(a, end=" ")
  print(a)