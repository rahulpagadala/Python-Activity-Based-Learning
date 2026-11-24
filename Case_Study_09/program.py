# ==============================================================================
# Case Study 9: Student Marks Matrix Analysis
# Student Name: P.RAHUL | Roll Number: 26000659 | Branch: CSE
# College: Dr. RVR NRI Institute of Technology
# ==============================================================================

students = ["Kiran", "Meena", "Arjun", "Divya"]
subjects = ["Maths", "Physics", "Chemistry", "Python"]
marks = [
    [88, 76, 91, 95],
    [67, 72, 58, 80],
    [45, 52, 38, 60],
    [92, 85, 79, 88],
]

highest = marks[0][0]
lowest = marks[0][0]
best_total = -1
best_student = 0

print(f"{'Student':<10}", end="")
for s in subjects:
    print(f"{s:>10}", end="")
print(f"{'Total':>8}{'Avg':>8}")
print("-" * 66)

# row-wise: totals, averages, highest and lowest cell
for i in range(4):
    total = 0
    for j in range(4):
        total = total + marks[i][j]
        if marks[i][j] > highest:
            highest = marks[i][j]
        if marks[i][j] < lowest:
            lowest = marks[i][j]
    if total > best_total:
        best_total = total
        best_student = i
    print(f"{students[i]:<10}", end="")
    for j in range(4):
        print(f"{marks[i][j]:>10}", end="")
    print(f"{total:>8}{total / 4:>8.2f}")

# column-wise: subject averages
print("-" * 66)
print(f"{'Average':<10}", end="")
best_avg = -1
best_subject = 0
for j in range(4):
    col = 0
    for i in range(4):
        col = col + marks[i][j]
    avg = col / 4
    if avg > best_avg:
        best_avg = avg
        best_subject = j
    print(f"{avg:>10.2f}", end="")
print("\n")

print("Highest mark in class :", highest)
print("Lowest mark in class  :", lowest)
print(f"Top student           : {students[best_student]} ({best_total} marks)")
print(f"Best subject          : {subjects[best_subject]} (class average {best_avg:.2f})")
