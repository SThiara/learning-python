def has_duplicates(list):
  for item in list:
    if list.count(item) > 1:
      return True
  return False

l=[1, 2, 3, 4, 5]  
print(has_duplicates(l))
l=[1, 2, 3, 3, 4]  
print(has_duplicates(l))