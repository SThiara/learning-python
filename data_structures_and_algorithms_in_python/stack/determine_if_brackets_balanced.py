from stack import Stack
  
def is_match(p1, p2):
    if p1 == "(" and p2 == ")":
        return True
    if p1 == "{" and p2 == "}":
        return True
    if p1 == "[" and p2 == "]":
        return True
    return False

def is_paren_balanced(paren_string):
    s = Stack()
    is_balanced = True

    for bracket in paren_string:
      if bracket in "([{":
        s.push(bracket)
      else:
        if s.is_empty():
          is_balanced = False
          break
        top = s.pop()
        if not is_match(top, bracket):
          is_balanced = False
          break
    
    return is_balanced

print("String : (((({})))) Balanced or not?")
print(is_paren_balanced("(((({}))))"))

print("String : [][]]] Balanced or not?")
print(is_paren_balanced("[][]]]"))

print("String : [][] Balanced or not?")
print(is_paren_balanced("[][]"))