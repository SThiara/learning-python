def divBy(num):
  try:
    return 50 / num
  except ZeroDivisionError:
    return "Error: Attempted to divide by zero"

print(divBy(5))
print(divBy(0))
print(divBy(50))