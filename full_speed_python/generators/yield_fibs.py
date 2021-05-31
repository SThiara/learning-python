def fibonacci(n):
  myArray = []
  for count in range(n):
    if count <= 1:
      myArray.append(count)
      yield count
    else:
      x = myArray[count-2] + myArray[count-1]
      myArray.append(x)
      yield x
      
for val in fibonacci(8):
  print(val)