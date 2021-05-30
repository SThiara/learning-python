""" def oldestStudent(ages):
  name = None
  age = 0
  for key, value in ages.items():
    if value > age:
      age = value
      name = key
  return name """

def oldestStudent(ages):
  
  value = list(ages.values())
  key = list(ages.keys())
  return key[value.index(max(value))]

ages = {
     "Peter": 10,
     "Isabel": 11,
     "Anna": 9,
     "Thomas": 10,
     "Bob": 10,
     "Joseph": 11,
     "Maria": 12,
     "Gabriel": 10,
  }
print(oldestStudent(ages))