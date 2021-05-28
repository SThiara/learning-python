def ListofEvenOdds():
  list1 = [num for num in range(21) if (num % 2 == 0)]
  list2 = [num for num in range(21) if (num not in list1)]
  return [list1, list2]

[list1, list2] = ListofEvenOdds()
print(list1)
print(list2)