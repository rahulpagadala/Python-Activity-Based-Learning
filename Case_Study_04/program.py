# ==============================================================================
# Case Study 4: Warehouse Inventory Reconciliation
# Student Name: P.RAHUL | Roll Number: 26000659 | Branch: CSE
# College: Dr. RVR NRI Institute of Technology
# ==============================================================================

items    = ["Bolts", "Nuts", "Washers", "Cables", "Switches", "Bulbs"]
system   = [120, 85, 40, 60, 25, 70]    # quantity as per ERP records
physical = [118, 70, 41, 58, 12, 95]    # quantity counted on the shelf

mismatch_count = 0
reorder_count = 0

print("=" * 66)
print(f"{'Item':<12}{'System':>8}{'Physical':>10}{'Diff':>8}   Status")
print("=" * 66)

for i in range(len(items)):
    diff = physical[i] - system[i]
    status = ""

    if abs(diff) > 5:
        status = status + "DISCREPANCY "
        mismatch_count = mismatch_count + 1
    if physical[i] < 20:
        status = status + "REORDER"
        reorder_count = reorder_count + 1
    if status == "":
        status = "OK"

    print(f"{items[i]:<12}{system[i]:>8}{physical[i]:>10}{diff:>+8}   {status}")

print("=" * 66)
print("Items checked        :", len(items))
print("Discrepancies found  :", mismatch_count)
print("Items to reorder     :", reorder_count)
