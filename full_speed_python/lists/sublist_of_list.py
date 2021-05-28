def getSubList():
  l = [1, 4, 9, 10, 23]
  l1 = l[:3]
  l2 = l[3:]
  return [l1, l2]

test = getSubList()
print(test[0])
print(test[1])

[l1, l2] = getSubList()
print(l1)
print(l2)