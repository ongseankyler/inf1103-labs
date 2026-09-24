
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


