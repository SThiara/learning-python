def sum_N_Numbers (n):
  if n <= 1:
    return n
  return n + sum_N_Numbers(n-1)

print(sum_N_Numbers(5))