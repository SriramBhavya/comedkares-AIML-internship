print("Start small. Ship something.")# Simple Billing Program with 18% GST

customer_name = input("Enter Customer Name: ")
num_items = int(input("Enter Number of Items: "))

total = 0.0

print("\nEnter Item Details")
print("-" * 30)

for i in range(1, num_items + 1):
    item_name = input(f"\nEnter Item {i} Name: ")   # String
    quantity = int(input("Enter Quantity: "))       # Integer
    price = float(input("Enter Price per Item: "))  # Float

    amount = quantity * price
    total += amount

    print(f"{item_name} Amount = ₹{amount:.2f}")

gst = total * 0.18
grand_total = total + gst

print("\n" + "=" * 35)
print("            BILL")
print("=" * 35)
print("Customer Name :", customer_name)
print("Subtotal      : ₹", format(total, ".2f"))
print("GST (18%)     : ₹", format(gst, ".2f"))
print("Grand Total   : ₹", format(grand_total, ".2f"))
print("=" * 35)
print("Thank You! Visit Again.")
