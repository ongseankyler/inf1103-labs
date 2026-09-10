inventory = 0
rejected_entries = 0 

print("Enter stock quantity or type 'quit' to finish")

while True:
    entry = input("Enter stock quantity: ").strip()

    if entry.lower() == "quit":
        break

    if not entry.isdigit():
        print("Entry is not a valid whole number")
        rejected_entries = rejected_entries + 1
        continue

    quantity = int(entry)

    if quantity < 0 :
        print("Quantity negative. Entry rejected")
        rejected_entries = rejected_entries + 1
        continue

    inventory = inventory + quantity
    print(f"Entry accepted current inventory: {inventory}")

    if inventory > 500:
        print("Overstock! Inventory exceeds 500 units")
        break

print(f"Total units processed: {inventory}")
print(f"Total units rejected/failed: {rejected_entries}")




