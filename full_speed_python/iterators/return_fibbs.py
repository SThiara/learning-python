class MyRange:
  def __init__(self, n):
    self.n = n

  def __iter__(self):
    return self

  def next(self):
    if self.n <=1:
      return [0]
    fibArray = [0, 1]
    if self.n == 2:
      return fibArray
    for i in range(3, self.n+1):
      fibArray.append(fibArray[-1] + fibArray[-2])
    return fibArray
  
myrange = MyRange(8)
print(myrange.next())
      