# ==============================================================================
# Case Study 2: Retail Billing with Multiple Discount Rules
# Student Name: P.RAHUL | Roll Number: 26000659 | Branch: CSE
# College: Dr. RVR NRI Institute of Technology
# ==============================================================================

n = int(input("How many different products? "))

names = []
cats = []
qtys = []
prices = []

for i in range(n):
    print("\nProduct", i + 1)
    names.append(input("  Name: "))
    cats.append(input("  Category (Grocery/Electronics/Luxury): ").strip().lower())
    qtys.append(int(input("  Quantity: ")))
    prices.append(float(input("  Unit price (Rs.): ")))

subtotal = 0.0
print("\n" + "=" * 72)
print(f"{'Item':<14}{'Category':<13}{'Qty':>5}{'Rate':>11}{'Amount':>13}{'Tax':>12}")
print("-" * 72)

# first pass: line amounts and tax on each line (before discount)
line_totals = []
for i in range(n):
    amount = qtys[i] * prices[i]
    line_totals.append(amount)
    subtotal = subtotal + amount

# discount slab, capped at Rs. 2000
if subtotal <= 5000:
    disc_rate = 0
elif subtotal <= 10000:
    disc_rate = 5
else:
    disc_rate = 10
discount = subtotal * disc_rate / 100
if discount > 2000:
    discount = 2000.0

# tax is charged on the discounted value of each line (discount shared in proportion)
total_tax = 0.0
for i in range(n):
    if cats[i] == "electronics":
        tax_rate = 12
    elif cats[i] == "luxury":
        tax_rate = 18
    else:
        tax_rate = 5
    line_discount = discount * line_totals[i] / subtotal
    line_tax = (line_totals[i] - line_discount) * tax_rate / 100
    total_tax = total_tax + line_tax
    print(f"{names[i]:<14}{cats[i].title():<13}{qtys[i]:>5}{prices[i]:>11,.2f}{line_totals[i]:>13,.2f}{line_tax:>12,.2f}")

taxable = subtotal - discount
payable = taxable + total_tax

print("-" * 72)
print(f"{'Subtotal':<50}Rs. {subtotal:>12,.2f}")
print(f"{'Discount (' + str(disc_rate) + '%, max Rs.2000)':<50}Rs. {discount:>12,.2f}")
print(f"{'Taxable amount':<50}Rs. {taxable:>12,.2f}")
print(f"{'Total GST':<50}Rs. {total_tax:>12,.2f}")
print("=" * 72)
print(f"{'AMOUNT PAYABLE':<50}Rs. {payable:>12,.2f}")
print("=" * 72)
