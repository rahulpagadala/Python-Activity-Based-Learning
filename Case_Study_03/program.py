# ==============================================================================
# Case Study 3: Attendance Recovery Computation
# Student Name: P.RAHUL | Roll Number: 26000659 | Branch: CSE
# College: Dr. RVR NRI Institute of Technology
# ==============================================================================

total = int(input("Total classes held so far: "))
attended = int(input("Classes attended so far: "))

if total <= 0 or attended < 0 or attended > total:
    print("Invalid input: total must be > 0 and attended must be between 0 and total.")
else:
    current = attended * 100 / total
    print(f"\nCurrent attendance : {current:.2f}%")

    if current >= 75:
        print("Status             : ELIGIBLE (attendance is 75% or more)")
        print("No recovery classes needed.")
    else:
        print("Status             : SHORTAGE (below 75%)")
        extra = 0
        new_total = total
        new_attended = attended
        # attend one more class at a time until 75% is reached
        while new_attended * 100 / new_total < 75:
            extra = extra + 1
            new_total = new_total + 1
            new_attended = new_attended + 1

        print(f"Classes to attend continuously : {extra}")
        print(f"Attended / Total after that    : {new_attended} / {new_total}")
        print(f"Attendance after recovery      : {new_attended * 100 / new_total:.2f}%")
