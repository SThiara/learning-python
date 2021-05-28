def findOccurence(s):
  a = s.find("b")
  b = s.find("ccc")
  return [a, b]

str = "aaabbccc"
print(findOccurence(str))