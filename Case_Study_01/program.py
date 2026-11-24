# ==============================================================================
# Case Study 1: Employee Payroll and Deduction Analysis
# Student Name: P.RAHUL | Roll Number: 26000659 | Branch: CSE
# College: Dr. RVR NRI Institute of Technology
# ==============================================================================

# ---------- Input ----------
name = input("Enter employee name: ")
basic = float(input("Enter basic pay (Rs.): "))
ot_hours = float(input("Enter overtime hours: "))
incentive = float(input("Enter incentive (Rs.): "))

# ---------- Earnings ----------
hra = 0.20 * basic            # House Rent Allowance = 20% of basic
da = 0.10 * basic             # Dearness Allowance  = 10% of basic
overtime = ot_hours * 500     # Rs. 500 per overtime hour
gross = basic + hra + da + overtime + incentive

# ---------- Income tax slab (on gross) ----------
if gross <= 50000:
    tax_rate = 0
elif gross <= 100000:
    tax_rate = 5
elif gross <= 150000:
    tax_rate = 10
else:
    tax_rate = 15
tax = gross * tax_rate / 100

# ---------- Other deductions ----------
pf = 0.12 * basic             # Provident Fund = 12% of basic
fixed = 2000                  # Insurance + professional tax
total_deduction = tax + pf + fixed

# ---------- Net salary ----------
net = gross - total_deduction

# ---------- Output ----------
print()
print("=" * 50)
print("            SALARY STATEMENT")
print("=" * 50)
print(f"Employee Name     : {name}")
print(f"Basic Pay         : Rs. {basic:,.2f}")
print(f"HRA (20%)         : Rs. {hra:,.2f}")
print(f"DA (10%)          : Rs. {da:,.2f}")
print(f"Overtime          : Rs. {overtime:,.2f}")
print(f"Incentive         : Rs. {incentive:,.2f}")
print("-" * 50)
print(f"Gross Salary      : Rs. {gross:,.2f}")
print("-" * 50)
print(f"{'Income Tax (' + str(tax_rate) + '%)':<17} : Rs. {tax:,.2f}")
print(f"Provident Fund    : Rs. {pf:,.2f}")
print(f"Other Deductions  : Rs. {fixed:,.2f}")
print(f"Total Deductions  : Rs. {total_deduction:,.2f}")
print("=" * 50)
print(f"NET SALARY        : Rs. {net:,.2f}")
print("=" * 50)
