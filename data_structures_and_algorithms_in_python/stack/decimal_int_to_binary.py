"""
Stack Data Structure.
"""
class Stack():
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)				

    def pop(self):
        return self.items.pop()
    
    def is_empty(self):
        return self.items == []
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        
    def get_stack(self):
        return self.items

def convert_int_to_bin(dec_num):
  if dec_num == 0:
    return 0

  s = Stack()

  decimal = dec_num

  while decimal > 0:
    s.push(decimal % 2)
    decimal = decimal // 2

  binary = str(s.pop())
  while s.is_empty() != True:
    binary += str(s.pop())
  return binary

print(convert_int_to_bin(8))
print(convert_int_to_bin(9))