# ==============================================================================
# Case Study 5: Student Performance Trend Analysis
# Student Name: P.RAHUL | Roll Number: 26000659 | Branch: CSE
# College: Dr. RVR NRI Institute of Technology
# ==============================================================================

students = ["Kiran", "Meena", "Arjun", "Divya", "Sai"]
subjects = ["Maths", "Physics", "Chemistry", "Python"]
marks = [
    [88, 76, 91, 95],
    [67, 72, 58, 80],
    [45, 52, 38, 60],
    [30, 35, 28, 42],
    [92, 85, 79, 88],
]

print("=" * 76)
print(f"{'Student':<10}", end="")
for s in subjects:
    print(f"{s:>10}", end="")
print(f"{'Total':>8}{'Avg %':>8}  Grade")
print("=" * 76)

for i in range(len(students)):
    total = 0
    for j in range(len(subjects)):
        total = total + marks[i][j]
    avg = total / len(subjects)

    if avg >= 80:
        grade = "Excellent"
    elif avg >= 60:
        grade = "Good"
    elif avg >= 40:
        grade = "Average"
    else:
        grade = "Poor"

    print(f"{students[i]:<10}", end="")
    for j in range(len(subjects)):
        print(f"{marks[i][j]:>10}", end="")
    print(f"{total:>8}{avg:>8.2f}  {grade}")

print("-" * 76)
print(f"{'Class avg':<10}", end="")
for j in range(len(subjects)):
    col_total = 0
    for i in range(len(students)):
        col_total = col_total + marks[i][j]
    print(f"{col_total / len(students):>10.2f}", end="")
print()
