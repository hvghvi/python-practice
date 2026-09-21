students = [
    {"name": "Alice", "age": 20, "grades": {"math": 88, "science": 92, "english": 85}, "active": True},
    {"name": "Bob", "age": 19, "grades": {"math": 76, "science": 81, "english": 79}, "active": True},
    {"name": "Charlie", "age": 21, "grades": {"math": 95, "science": 89, "english": 91}, "active": False},
    {"name": "Diana", "age": 20, "grades": {"math": 82, "science": 87, "english": 90}, "active": True},
    {"name": "Ethan", "age": 22, "grades": {"math": 70, "science": 74, "english": 68}, "active": False},
]

#prints everyones math score
for i in range(len(students)):
    print(students[i]["name"], students[i]["grades"]["math"])

print()
#better way? 
for student in students:
    print(student["name"], student["grades"]["math"])

print()
print("2,")
#exercise 2 only active students
for student in students:
    if student["active"]:
        print(student["name"], student["grades"]["math"])


print()
print("3,")
#exercise 3 average of active student grades
for student in students:
    if student["active"]:
        average = sum(student["grades"].values()) / len(student["grades"].values())
        print(f"{student['name']} {average:.2f}") 


print()
print("4")
