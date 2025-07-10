contacts = {letter: {} for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"}
def display_contacts():
    print("\n--- Contacts ---")
    for letter in sorted(contacts.keys()):
        if contacts[letter]:
            print(f"\n{letter}")
            for name, number in sorted(contacts[letter].items()):
                print(f"  {name}: {number}")
    print("\n--- End of Contacts ---")
def add_contact():
    name = input("Enter contact name: ")
    number = input("Enter contact number: ")
    if not name or not number.isdigit():
        print("Invalid input. Please ensure you enter a valid name and number.")
        return
    letter = name[0].upper()
    contacts[letter][name] = number
    print(f"Added contact {name} with number {number}.")
def remove_contact():
    name = input("Enter the contact name to remove: ")
    letter = name[0].upper()
    if letter in contacts and name in contacts[letter]:
        contacts[letter].pop(name)
        print(f"Removed contact {name}.")
    else:
        print("Contact not found.")
def update_contact():
    name = input("Enter the contact name to update: ")
    letter = name[0].upper()
    if letter in contacts and name in contacts[letter]:
        new_number = input("Enter new contact number: ")
        if not new_number.isdigit():
            print("Invalid number. Please enter digits only.")
            return
        contacts[letter][name] = new_number
        print(f"Updated contact {name} with new number {new_number}.")
    else:
        print("Contact not found.")
def search_contact():
    search_term = input("Enter name or part of the name to search: ")
    found = False
    print("\n--- Search Results ---")
    for letter in sorted(contacts.keys()):
        for name, number in contacts[letter].items():
            if search_term in name:
                print(f"{name}: {number}")
                found = True
    if not found:
        print("No contacts found.")
def main():
    while True:
        print(
            "\n1. Display Contacts\n2. Add New Contact\n3. Remove Contact\n4. Update Contact\n5. Search Contact\n6. Exit")
        choice = input("Select an option (1-6): ")
        if choice == '1':
            display_contacts()
        elif choice == '2':
            add_contact()
        elif choice == '3':
            remove_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            search_contact()
        elif choice == '6':
            print("Exiting the contact management system.")
            break
        else:
            print("Invalid choice. Please select a valid option.")
main()