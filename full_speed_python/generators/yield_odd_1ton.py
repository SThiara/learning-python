def odd(n):
  for num in range(1, n+1):
    print(num)
    if num % 2 != 0:
      yield num

for number in odd(8):
  print(number)