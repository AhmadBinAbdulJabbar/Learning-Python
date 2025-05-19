import json, csv, os, re

contact_csv = "contacts.csv"
contact_json = "contacts.json"
header = ["name", "phone", "email", "address"]

def contact_rewriter(contacts):
    file_exists = os.path.exists(contact_csv)
    try:
        with open(contact_csv, "w", newline="") as file:
            writer = csv.DictWriter(file, header)
            writer.writeheader()
            writer.writerows(contacts)

            print("Contacts were added successfully! ✅")
    except Exception as e:
        print("Error! Contact was not added! ❌")
        print("Error:", e)

def add_contact(): 
    name = input("Enter Name: ").strip().title()
    phone = input("Enter Phone: ").strip()
    email = input("Enter Email: ").strip()
    address_city = input("Enter Address City: ").strip().capitalize()

    phone_pattern = r"^(0\d{10}|92\d{10}|\+92\d{10})$"
    if not re.fullmatch(phone_pattern, phone):
        print("Invalid phone number! Please enter a valid number with area code (e.g., 03001234567, 0421234567, +923001234567).")
        return

    # email_pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$" # basic
    email_pattern = r"^[a-zA-Z0-9.!#$%&'*+\/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$" # advance 
    if not re.fullmatch(email_pattern, email):
        print("Invalid email address!")
        return

    contact_details ={"name": name, "phone": phone,"email": email, "address": address_city}

    file_exists = os.path.exists(contact_csv)
    try:
        with open(contact_csv, "a", newline="") as file:
            writer = csv.DictWriter(file, header)

            if not file_exists or os.path.getsize(contact_csv) == 0:
                writer.writeheader()

            writer.writerow(contact_details)

            print("Contact added successfully! ✅")
    except Exception as e:
        print("Error! Contact was not added! ❌")
        print("Error:", e)

def get_current_contacts():
    contacts = []
    try:
        with open(contact_csv, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                contacts.append({
                    "name" : row["name"],
                    "phone": row["phone"],
                    "email": row["email"],
                    "address": row["address"]
                })

    except FileNotFoundError:
        print(f"{contact_csv} File does not Exist")

    return contacts

def view_contacts(): 
    print("==== Contact List ====")
    contacts = get_current_contacts()

    for i, contact in enumerate(sorted(contacts, key=lambda contact: contact['name']), start=1):
        print(f"{i}. {contact['name']} | {contact['phone']} | {contact['email']} | {contact['address']}")

    return contacts


def search_contact(): 
    contacts = get_current_contacts()
    
    try:
        search_by = int(input("Search by (1) Name or (2) Phone: "))
    except ValueError:
        print("Invalid input. Please enter 1 or 2.")
        return []

    contact_found = []
    if search_by == 1:
        search_name = input("Enter Name: ").strip().lower()
        contact_found = [c for c in contacts if search_name in c['name'].lower()]
    elif search_by == 2:
        search_phone = input("Enter Phone: ").strip()
        contact_found = [c for c in contacts if search_phone in c['phone']]
    else:
        print("Invalid option.")
        return []

    # print(contact_found)

    if contact_found:
        for i, contact in enumerate(contact_found, start=1):
            print(f"Found: {i}. {contact['name']} | {contact['phone']} | {contact['email']} | {contact['address']}")
    else:
        print(f"Not found!")

    return contact_found

    
def update_contact():
    contacts = get_current_contacts()
    print("Search the contact you want to update.")
    contacts_found = search_contact()
    # print(contacts_found)

    if not contacts_found:
        print("No contacts to update.")
        return

    try:
        update_num = int(input("Enter the number which you want to update. ").strip())
        if update_num < 1 or update_num > len(contacts_found):
            print("Invalid numbers.")
            return
    except Exception as e:
        print("Invalid input.")
        print("Error:", e)
        return
    
    current_details = contacts_found[update_num-1]
    # print(current_details)

    new_name = input("Enter new name (or press Enter to skip): ").strip()
    if new_name == "":
        new_name = current_details['name']

    new_phone = input("Enter new phone (or press Enter to skip): ").strip()
    if new_phone == "":
        new_phone = current_details['phone']

    new_email = input("Enter new email (or press Enter to skip): ").strip()
    if new_email == "":
        new_email = current_details['email']
        
    new_address = input("Enter new address (or press Enter to skip): ").strip()
    if new_address == "":
        new_address = current_details['address']


    phone_pattern = r"^(0\d{10}|92\d{10}|\+92\d{10})$"
    if not re.fullmatch(phone_pattern, new_phone):
        print("Invalid phone number! Please enter a valid number with area code (e.g., 03001234567, 0421234567, +923001234567).")
        return

    email_pattern = r"^[a-zA-Z0-9.!#$%&'*+\/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$" # advance 
    
    if not re.fullmatch(email_pattern, new_email):
        print("Invalid email address!")
        return

    new_contact_details = {"name": new_name, "phone": new_phone, "email": new_email, "address": new_address}

    for i, contact in enumerate(contacts, start=0):
        if contact.get("name").lower() == current_details['name'].lower() and contact.get("phone") == current_details['phone']:
            contacts[i] = new_contact_details

    contact_rewriter(contacts)

    print("Contact updated successfully! ✅")


def delete_contact():
    contacts = get_current_contacts()
    print("Search the contact you want to delete.")
    contacts_found = search_contact()

    if not contacts_found:
        print("No contact to delete.")
        return

    try:
        delete_num = int(input("Enter the number which you want to delete. ").strip())
        if delete_num < 1 or delete_num > len(contacts_found):
            print("Invalid number.")
            return
    except ValueError:
        print("Invalid input.")
        return
    
    delete_contact = contacts_found[delete_num-1]

    if delete_contact in contacts:
        contacts.remove(delete_contact)
        contact_rewriter(contacts)
        print("Contact deleted successfully! ✅")
    else:
        print("Contact not found in the contact list.")

def export_to_json(): 
    contacts = get_current_contacts()
    try:
        with open(contact_json, 'w') as file:
            json.dump(contacts, file, indent=4)
            print(f"Exported {len(contacts)} contacts to contacts.json ✅")
    except Exception as e:
        print("Error! while converting to json ❌")
        print("Error:", e)

def menu():
    while True:
        print("==== Contact Book ====")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Export to JSON")
        print("7. Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            export_to_json()
        elif choice == '7':
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.\n")

if __name__ == "__main__":
    menu()