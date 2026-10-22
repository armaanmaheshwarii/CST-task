students = {
    "S1": [85, 95, 70, 60],
    "S2": [79, 68, 72, 94],
    "S3": [90, 94, 50, 39]
}

for name, marks in students.items():
    percentage = sum(marks) / 400 * 100
    print(name, "Percentage =", percentage, "%")