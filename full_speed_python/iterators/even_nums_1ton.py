class MyRange:
  def __init__(self, n):
    self.n = n

  def __iter__(self):
    return self

  def next(self):
    evenList = []
    for i in range(1, self.n+1):
      if i % 2 is 0:
        evenList.append(i)
    return evenList
    
myrange = MyRange(8)
print (myrange.next())