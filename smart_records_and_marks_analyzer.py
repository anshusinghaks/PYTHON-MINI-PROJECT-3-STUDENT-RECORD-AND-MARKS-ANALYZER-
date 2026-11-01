subjects = ("Python", "Maths", "DBMS")

students = {}

n = int(input("Enter number of students: "))

for i in range(n):

    sid = input("\nEnter Student ID: ")

    if sid in students:
        print("ID already exists")
        continue

    name = input("Enter Name: ")

    marks = []

    for sub in subjects:
        m = int(input("Enter " + sub + " marks: "))

        while m < 0 or m > 100:
            print("Enter marks between 0 and 100")
            m = int(input("Enter marks again: "))

        marks.append(m)

    students[sid] = [name, marks]


print("\n----- STUDENT REPORT -----")

for sid in students:

    name = students[sid][0]
    marks = students[sid][1]

    total = sum(marks)
    avg = total / 3

    if avg >= 75:
        result = "Distinction"
    elif avg >= 40:
        result = "Pass"
    else:
        result = "Fail"

    print("\nID:", sid)
    print("Name:", name)
    print("Marks:", marks)
    print("Total:", total)
    print("Average:", avg)
    print("Result:", result)

sid = input("\nEnter ID to search: ")

if sid in students:
    print("Student Found:", students[sid])
else:
    print("Student Not Found")

student_ids = list(students.keys())

print("First two IDs:", student_ids[:2])


sid = input("\nEnter ID to update marks: ")

if sid in students:

    print("0-Python, 1-Maths, 2-DBMS")

    pos = int(input("Enter subject position: "))
    new_mark = int(input("Enter new marks: "))

    if pos >= 0 and pos < 3 and 0 <= new_mark <= 100:
        students[sid][1][pos] = new_mark
        print("Marks Updated")
    else:
        print("Invalid position or marks")

else:
    print("Student Not Found")


passed = set()

for sid in students:

    for i in range(3):

        if students[sid][1][i] >= 40:
            passed.add(subjects[i])

print("Passed Subjects:", passed)


averages = []

for sid in students:

    avg = sum(students[sid][1]) / 3
    averages.append(avg)

if len(averages) > 0:

    print("\n----- CLASS SUMMARY -----")
    print("Total Students:", len(students))
    print("Class Average:", sum(averages) / len(averages))
    print("Highest Average:", max(averages))
    print("Lowest Average:", min(averages))