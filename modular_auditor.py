rejected_entries = 0 

def get_valid_input():
    
    global rejected_entries
    
    while True:
        entry = input("Enter stock quantity or type 'quit' to finish: ").strip()

        if entry.lower() == "quit":
            return "quit"

        if not entry.lstrip("-").isdigit():
            print("Entry is not a valid whole number")
            rejected_entries += 1
            continue

        quantity = int(entry)

        if quantity < 0:
            print("Quantity negative. Entry rejected")
            rejected_entries += 1
            continue

        return quantity

        
def process_delivery(current_total, new_value):
    
    return current_total + new_value


def calculate_tax(amount):
    
    return amount * 0.1


def generate_report(total_units, failed_attempts):
    
    print("\n--- Final Report ---")
    print(f"Total Deliveries Processed: {total_units}")
    print(f"Number of Failed/Rejected Entries: {failed_attempts}")


def main():
    global rejected_entries

    inventory = 0
    total_tax = 0
    deliveries_processed = 0

    print("Enter stock quantity or type 'quit' to finish")

    while True:
        result = get_valid_input()

        if result == "quit":
            break

        inventory = process_delivery(inventory, result)
        tax = calculate_tax(result)
        total_tax += tax
        deliveries_processed += 1

        print(f"Entry accepted. Current inventory: {inventory} (tax on this delivery: {tax:.2f})")

        if inventory > 500:
            print("Overstock! Inventory exceeds 500 units")
            break

    generate_report(deliveries_processed, rejected_entries)
    print(f"Total tax accumulated: {total_tax:.2f}")
    print(f"Total Inventory: {inventory}")


main()