def display_menu():
    print("\nMenu:")
    print("1. Add item")
    print("2. Remove item")
    print("3. Update item quantity")
    print("4. Display sorted list")
    print("5. Display total number of items")
    print("6. Exit")

def add_item(grocery_list):
    name = input("Enter item name to add: ").lower().strip()
    quantity = int(input("Enter quantity: ").strip())
    if name in grocery_list:
        grocery_list[name] += quantity
    else:
        grocery_list[name] = quantity
    print(f"{name} added/updated with quantity {grocery_list[name]}")

def remove_item(grocery_list):
    name = input("Enter item name to remove: ").lower().strip()
    if name in grocery_list:
        del grocery_list[name]
        print(f"{name} removed.")
    else:
        print("Item not found.")

def update_item(grocery_list):
    name = input("Enter item name to update: ").lower().strip()
    if name in grocery_list:
        quantity = int(input("Enter new quantity: ").strip())
        grocery_list[name] = quantity
        print(f"{name} updated to {quantity}")
    else:
        print("Item not found.")

def display_sorted_list(grocery_list):
    if not grocery_list:
        print("Grocery list is empty.")
    else:
        print("\nSorted Grocery List:")
        for item in sorted(grocery_list):
            print(f"{item} - {grocery_list[item]}")

def display_total_items(grocery_list):
    total_quantity = sum(grocery_list.values())
    print(f"Total number of items: {total_quantity}")

def main():
    grocery_list = {}
    while True:
        display_menu()
        choice = input("Choose an option (1–6): ").strip()

        if choice == '1':
            add_item(grocery_list)
        elif choice == '2':
            remove_item(grocery_list)
        elif choice == '3':
            update_item(grocery_list)
        elif choice == '4':
            display_sorted_list(grocery_list)
        elif choice == '5':
            display_total_items(grocery_list)
        elif choice == '6':
            print("Exiting Grocery List Manager.")
            break
        else:
            print("Invalid option. Please choose between 1 and 6.")

if __name__ == "__main__":
    main()
