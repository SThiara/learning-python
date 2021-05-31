class MyRange:
  def __init__(self, n):
    self.n = n

  def __iter__(self):
    return self

  def next(self):
    evenList = []
    while self.n >= 0:
      evenList.append(self.n)
      self.n -= 1
    return evenList
  
myRange = MyRange(8)
print(myRange.next())