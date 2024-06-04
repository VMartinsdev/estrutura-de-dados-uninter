
def fatorial_iterativo(n):
  n = 5
  fat = 1
  if n <0:
    return None
  elif n == 0 or n == 1:
    return fat
  else:
      for i in range(1, n+1):
          fat *= i
      return fat

print(fatorial_iterativo(5))

# Série Fibonacci
n = 5
fat = 1
f1 = 1
f2 = 1
for i in range(1, n+1):
   f3 = i+f1
for u in range(1, n+1)
     f4 = f3+f2
print(f3)
