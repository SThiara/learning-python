def reverse(list):
  new_list = []
  for item in list:
    new_list.insert(0, item)
  return new_list

list=[1, 2, 3, 4, 5]
print(reverse(list))