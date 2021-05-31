def reverse(n):
  for value in range(n, -1, -1):
    yield value

for i in reverse(8):
  print(i)