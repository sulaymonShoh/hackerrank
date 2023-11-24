# number of students
n = int(input())

# empty list for storing data
students = []

# fetting and storing data in list
for i in range(n):
    # Read stundets name and grade
    name = input()
    grade = float(input())

    # create nasted list and append it to list of stundets
    students.append([name, grade])

# sorting list of stundets based on their grades
students.sort(key=lambda x: x[1])

# Find the lowest gradeby iterating over sorted list and comparing adjacent grades
second_lowest_grade = None
for i in range(1, n):
    if students[i][1] > students[0][1]:
        second_lowest_grade = students[i][1]
        break

# create new list for names of students with second lowest grade
names = []
for student in students:
    if student[1] == second_lowest_grade:
        names.append(student[0])

# print the names of students with SLG
print(*names)
