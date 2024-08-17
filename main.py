from item import Item


def main():
    item_manager = Item()
    item_manager.create_table()

    while True:
        print("\nMenu:")
        print("1. Create Item")
        print("2. Read Items")
        print("3. Update Item")
        print("4. Delete Item")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter name: ")
            quantity = int(input("Enter quantity: "))
            price = float(input("Enter price: "))
            item_manager.create_item(name, quantity, price)
            print("Item created successfully.")

        elif choice == '2':
            items = item_manager.get_items()
            print("Items:")
            for itm in items:
                print(itm)

        elif choice == '3':
            item_id = int(input("Enter item ID to update: "))
            name = input("Enter new name: ")
            quantity = int(input("Enter new quantity: "))
            price = float(input("Enter new price: "))
            item_manager.update_item(item_id, name, quantity, price)
            print("Item updated successfully.")

        elif choice == '4':
            item_id = int(input("Enter item ID to delete: "))
            item_manager.delete_item(item_id)
            print("Item deleted successfully.")

        elif choice == '5':
            print("Exiting...")
            item_manager.close()
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
