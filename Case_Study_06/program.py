# ==============================================================================
# Case Study 6: Student Timetable Conflict Detection
# Student Name: P.RAHUL | Roll Number: 26000659 | Branch: CSE
# College: Dr. RVR NRI Institute of Technology
# ==============================================================================

# each course = (name, start hour, end hour) in 24-hour format
courses = [
    ("Maths",        9, 10),
    ("Physics",     10, 12),
    ("Python Lab",  11, 13),
    ("English",     13, 14),
    ("Chemistry",   12, 14),
    ("Workshop",    15, 17),
]

print("Registered courses:")
for c in courses:
    name, start, end = c
    print(f"  {name:<12} {start:02d}:00 - {end:02d}:00")

print("\nConflict check:")
conflicts = 0
for i in range(len(courses)):
    for j in range(i + 1, len(courses)):
        name_a, start_a, end_a = courses[i]
        name_b, start_b, end_b = courses[j]

        if start_a < end_b and start_b < end_a:
            conflicts = conflicts + 1
            o_start = max(start_a, start_b)
            o_end = min(end_a, end_b)
            print(f"  CLASH: {name_a} and {name_b} overlap from {o_start:02d}:00 to {o_end:02d}:00")

if conflicts == 0:
    print("  No conflicts found.")
print("\nTotal conflicts:", conflicts)
