contacts_dict = {}

def add_contact():
    contact_name = input("Enter the contact's name: ")
    contact_phone = input("Enter the contact's phone number: ")
    contact_email = input("Enter the contact's email: ")
    contact_address = input("Enter the contact's address: ")

    contacts_dict[contact_name] = {"Phone": contact_phone, "Email": contact_email, "Address": contact_address}
    print(f"{contact_name} has been added to your contacts.")

def view_contacts():
    if not contacts_dict:
        print("Your contacts list is empty.")
    else:
        print("Contact List:")
        for name, details in contacts_dict.items():
            print(f"Name: {name}")
            print(f"Phone: {details['Phone']}")
            print(f"Email: {details['Email']}")
            print(f"Address: {details['Address']}")
            print("-" * 20)

def search_contact():
    search_term = input("Enter the name or phone number to search: ").lower()
    found = False

    for name, details in contacts_dict.items():
        if search_term in name.lower() or search_term in details["Phone"]:
            print_contact_details(name, details)
            found = True

    if not found:
        print("Contact not found.")

def update_contact():
    contact_name = input("Enter the name of the contact to update: ")
    if contact_name in contacts_dict:
        print(f"Current details for {contact_name}:")
        print_contact_details(contact_name, contacts_dict[contact_name])

        contacts_dict[contact_name]["Phone"] = input("Enter new phone number (press Enter to keep it unchanged): ") or contacts_dict[contact_name]["Phone"]
        contacts_dict[contact_name]["Email"] = input("Enter new email (press Enter to keep it unchanged): ") or contacts_dict[contact_name]["Email"]
        contacts_dict[contact_name]["Address"] = input("Enter new address (press Enter to keep it unchanged): ") or contacts_dict[contact_name]["Address"]

        print(f"{contact_name}'s contact details have been updated.")
    else:
        print("Contact not found.")

def delete_contact():
    contact_name = input("Enter the name of the contact to delete: ")
    if contact_name in contacts_dict:
        del contacts_dict[contact_name]
        print(f"{contact_name} has been deleted from your contacts.")
    else:
        print("Contact not found.")

def print_contact_details(name, details):
    print(f"Name: {name}")
    print(f"Phone: {details['Phone']}")
    print(f"Email: {details['Email']}")
    print(f"Address: {details['Address']}")
    print("-" * 20)

while True:
    print("\nContact Management System")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Select an option (1/2/3/4/5/6): ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        search_contact()
    elif choice == "4":
        update_contact()
    elif choice == "5":
        delete_contact()
    elif choice == "6":
        break
    else:
        print("Invalid choice. Please choose a valid option.")
