def isSorted(list):
  num_evaluate = list[0]
  for num in list[1:]:
    if num < num_evaluate:
      return False
    num_evaluate = num
  return True

print(isSorted([1,2,3,4,5]))
print(isSorted([1,2,5,4,2]))