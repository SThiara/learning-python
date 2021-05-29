def findMaximum(list):
  if len(list) == 0:
    return None
  max = list[0]
  for num in list:
    if num > max:
      max = num
  return max

def findMaximumValueIndex(list):
  if len(list) == 0:
    return [None, None]
  index = 0
  max = list[0]
  for i, num in enumerate(list):
      if num > max:
          max = num
          index = i
  return [index, max]

list=[1, 2, 7, 4, 5]
[index, max] = findMaximumValueIndex(list)

print(findMaximum(list))
print("Index:", index)
print("Maximum Value:", max)