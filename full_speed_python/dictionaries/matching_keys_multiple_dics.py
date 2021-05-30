def find_students(address, students):
  matched_students = []
  for studname, studstuff in students.items():
    if studstuff["address"] == address:
      matched_students.append(studname)
  return sorted(matched_students)
  
students = {
    "Peter": {"age": 10, "address": "Lisbon"},
    "Isabel": {"age": 11, "address": "Sesimbra"},
    "Anna": {"age": 9, "address": "Lisbon"},
}
print(find_students("Lisbon", students))

print(students.items())