# ==============================================================================
# Case Study 8: Nested Loop Calendar Generator
# Student Name: P.RAHUL | Roll Number: 26000659 | Branch: CSE
# College: Dr. RVR NRI Institute of Technology
# ==============================================================================

month = int(input("Enter month (1-12): "))
year = int(input("Enter year: "))

month_names = ["", "January", "February", "March", "April", "May", "June",
               "July", "August", "September", "October", "November", "December"]
days_in = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# leap year check
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    days_in[2] = 29

# day of week of the 1st (0 = Sunday ... 6 = Saturday) - Sakamoto's method
t = [0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4]
y = year
if month < 3:
    y = y - 1
first = (y + y // 4 - y // 100 + y // 400 + t[month - 1] + 1) % 7
offset = (first + 6) % 7          # convert so that Monday = 0

print()
print(f"{month_names[month]} {year}".center(28))
print("Mo  Tu  We  Th  Fr  Sa  Su")

day = 1
for week in range(6):
    line = ""
    for col in range(7):
        cell = week * 7 + col
        if cell < offset or day > days_in[month]:
            line = line + "    "
        else:
            line = line + f"{day:<4}"
            day = day + 1
    if line.strip() != "":
        print(line.rstrip())
