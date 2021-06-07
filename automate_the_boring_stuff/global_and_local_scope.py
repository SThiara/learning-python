spam = 42

def eggs():
  global spam
  spam = 24

eggs()

print(spam)