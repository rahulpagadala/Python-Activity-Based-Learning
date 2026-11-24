# ==============================================================================
# Case Study 7: Repeated Transaction Detection
# Student Name: P.RAHUL | Roll Number: 26000659 | Branch: CSE
# College: Dr. RVR NRI Institute of Technology
# ==============================================================================

# each transaction = (id, amount, merchant)
transactions = [
    (1001, 499.00, "Swiggy"),
    (1002, 1250.00, "Amazon"),
    (1003, 499.00, "Swiggy"),
    (1004, 250.00, "Uber"),
    (1005, 1250.00, "Amazon"),
    (1006, 499.00, "Swiggy"),
    (1007, 799.00, "Netflix"),
]

pairs = 0
print("Suspicious duplicate pairs:")
for i in range(len(transactions)):
    for j in range(i + 1, len(transactions)):
        id_a, amt_a, mer_a = transactions[i]
        id_b, amt_b, mer_b = transactions[j]
        if amt_a == amt_b and mer_a == mer_b:
            pairs = pairs + 1
            print(f"  Txn {id_a} & Txn {id_b} -> Rs. {amt_a:,.2f} at {mer_a}")

print("\nTransactions scanned :", len(transactions))
print("Duplicate pairs found:", pairs)
