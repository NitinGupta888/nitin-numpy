import random
import statistics

# Generate marks for 50 students
marks = []

for i in range(50):
    m = random.randint(0, 100)
    marks.append(m)

print("Marks of 50 Students")
print(marks)

# Total, Average, Highest, Lowest
total = sum(marks)
average = total / len(marks)
highest = max(marks)
lowest = min(marks)

print("\nTotal Marks :", total)
print("Average :", average)
print("Highest :", highest)
print("Lowest :", lowest)

# Count Above 75, Below 35, Between 35-75
above75 = 0
below35 = 0
between = 0

for i in marks:
    if i > 75:
        above75 += 1
    elif i < 35:
        below35 += 1
    else:
        between += 1

print("\nAbove 75 :", above75)
print("Below 35 :", below35)
print("Between 35 and 75 :", between)

# Assign Grades
print("\nGrades")

for i in range(len(marks)):
    if marks[i] >= 90:
        grade = "A+"
    elif marks[i] >= 75:
        grade = "A"
    elif marks[i] >= 60:
        grade = "B"
    elif marks[i] >= 35:
        grade = "C"
    else:
        grade = "F"

    print("Student", i + 1, "-", marks[i], "-", grade)

# Top 5 Marks
top5 = sorted(marks, reverse=True)

print("\nTop 5 Marks")
for i in top5[:5]:
    print(i)

# Bottom 5 Marks
bottom5 = sorted(marks)

print("\nBottom 5 Marks")
for i in bottom5[:5]:
    print(i)

# Median and Standard Deviation
median = statistics.median(marks)
std = statistics.stdev(marks)

print("\nMedian :", median)
print("Standard Deviation :", round(std, 2))

# 5 Subject Marks Matrix
print("\n5 Subject Marks Matrix")

students = []

for i in range(50):
    one = []
    for j in range(5):
        one.append(random.randint(30, 100))
    students.append(one)

for i in range(50):
    total = sum(students[i])
    print("Student", i + 1, ":", students[i], "Total =", total)

# Topper in Each Subject
print("\nTopper in Each Subject")

for sub in range(5):
    highest = students[0][sub]
    topper = 1

    for i in range(50):
        if students[i][sub] > highest:
            highest = students[i][sub]
            topper = i + 1

    print("Subject", sub + 1, ": Student", topper, "-", highest)

# Report Card
print("\nReport Cards")

for i in range(50):

    total = sum(students[i])
    average = total / 5
    percentage = average

    if percentage >= 90:
        grade = "A+"
    elif percentage >= 75:
        grade = "A"
    elif percentage >= 60:
        grade = "B"
    elif percentage >= 35:
        grade = "C"
    else:
        grade = "F"

    print("\nStudent", i + 1)
    print("Marks :", students[i])
    print("Total :", total)
    print("Average :", round(average, 2))
    print("Percentage :", round(percentage, 2), "%")
    print("Grade :", grade)