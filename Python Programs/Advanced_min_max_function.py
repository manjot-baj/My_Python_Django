# Advanced MAx And Min function
# max/min(list/tuple/string,your function)
students = {
    "harshit": {"Score": 90, "age": 24},
    "mohit": {"Score": 75, "age": 19},
    "rohit": {"Score": 76, "age": 23}
}
print(max(students, key=lambda item: students[item]["Score"]))
print(min(students, key=lambda item: students[item]["Score"]))

students = [
    {"Name": "harshit", "Score": 90, "age": 24},
    {"Name": "mohit", "Score": 75, "age": 19},
    {"Name": "rohit", "Score": 76, "age": 23}
]

print(max(students, key=lambda item: item.get("Score"))["Name"])
print(min(students, key=lambda item: item.get("Score"))["Name"])
