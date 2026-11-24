# ==============================================================================
# Case Study 10: Smart Canteen Order and Stock Management
# Student Name: P.RAHUL | Roll Number: 26000659 | Branch: CSE
# College: Dr. RVR NRI Institute of Technology
# ==============================================================================

# menu = [name, price, stock]  (stock changes as orders are placed)
menu = [
    ["Veg Biryani", 80, 10],
    ["Masala Dosa", 50, 12],
    ["Samosa", 15, 20],
    ["Tea", 10, 30],
    ["Coffee", 20, 25],
    ["Sandwich", 40, 6],
]

print("=" * 48)
print("               CANTEEN MENU")
print("=" * 48)
print(f"{'No.':<5}{'Item':<16}{'Price':>8}{'Stock':>10}")
for i in range(len(menu)):
    print(f"{i + 1:<5}{menu[i][0]:<16}{menu[i][1]:>8}{menu[i][2]:>10}")

n = int(input("\nHow many different items do you want to order? "))

order_names = []
order_qty = []
order_rate = []
subtotal = 0

for k in range(n):
    choice = int(input(f"Item {k + 1} - enter item number (1-{len(menu)}): "))
    qty = int(input("  Quantity: "))

    if choice < 1 or choice > len(menu):
        print("  Invalid item number, skipped.")
    elif qty <= 0:
        print("  Quantity must be positive, skipped.")
    elif qty > menu[choice - 1][2]:
        print(f"  Sorry, only {menu[choice - 1][2]} {menu[choice - 1][0]} left. Not added.")
    else:
        menu[choice - 1][2] = menu[choice - 1][2] - qty     # update stock
        order_names.append(menu[choice - 1][0])
        order_qty.append(qty)
        order_rate.append(menu[choice - 1][1])
        subtotal = subtotal + qty * menu[choice - 1][1]
        print("  Added to order.")

print("\n" + "=" * 48)
print("                  YOUR BILL")
print("=" * 48)
for i in range(len(order_names)):
    print(f"{order_names[i]:<16}{order_qty[i]:>4} x {order_rate[i]:<6}{order_qty[i] * order_rate[i]:>12.2f}")
print("-" * 48)

if subtotal > 200:
    discount = subtotal * 0.10
else:
    discount = 0
print(f"{'Subtotal':<30}{subtotal:>12.2f}")
print(f"{'Discount':<30}{discount:>12.2f}")
print(f"{'PAYABLE':<30}{subtotal - discount:>12.2f}")
print("=" * 48)

print("\nLow stock alert (less than 5 left):")
alert = False
for i in range(len(menu)):
    if menu[i][2] < 5:
        print(f"  {menu[i][0]} - only {menu[i][2]} left")
        alert = True
if not alert:
    print("  All items sufficiently stocked.")
