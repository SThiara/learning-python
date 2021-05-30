def calculateAvg(ages):
  values = ages.values()
  return sum(values)/len(values)

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
print(calculateAvg(ages))