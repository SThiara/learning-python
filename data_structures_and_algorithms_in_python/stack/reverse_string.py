from stack import Stack

def reverse_string(stack, input_str):
  for char in input_str:
    stack.push(char)
  rev_str = ""
  while not stack.is_empty():
    rev_str += stack.pop()

  return rev_str

stack = Stack()
input_str = "!evitacudE ot emocleW"
print(reverse_string(stack, input_str))