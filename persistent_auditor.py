rejected_entries = 0 

def load_inventory():

    try: 
        with open(inventory.txt, "r") as inventory:
            lines = inventory.read().splitlines()
    except FileNotFoundError:
        return 0, []

    try:
        total_inventory = int(lines[0])
        history = []
        if len(lines) > 1 and lines[1].strip():
            history = [int(item) for item in lines[1].split(",")]
        return total_inventory, history
    except (ValueError, IndexError):
        print("Inventory file not found. Starting from new file")
        return 0, []


def save_inventory(total_inventory, history):
    with open(inventory.txt, "w") as inventory:
        inventory.write(f"{total_inventory}\n")
        inventory.write(",". join(str(amount) for amount in history) + "\n")



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

    inventory, history = load_inventory()
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

    save_inventory(inventory, history)


    generate_report(deliveries_processed, rejected_entries)
    print(f"Total tax accumulated: {total_tax:.2f}")
    print(f"Total Inventory: {inventory}")


main()