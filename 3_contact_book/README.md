# Contact Book

A simple terminal-based Python application to manage your contacts. Easily add, view, search, update, delete, and export contacts to JSON or CSV.

## Features

- **Add Contact:** Add a new contact with name, phone, email, and address. Validates phone and email formats.
- **View Contacts:** Display all contacts in a sorted list.
- **Search Contact:** Search for contacts by name or phone number.
- **Update Contact:** Update details of an existing contact.
- **Delete Contact:** Remove a contact from the list.
- **Export to JSON:** Export all contacts to a `contacts.json` file.
- **CSV Storage:** All contacts are stored in `contacts.csv` for persistence.

## How to Use

1. **Run the Application**
   ```bash
   python contact_book.py
   ```

2. **Menu Options**
   - `1. Add Contact`  
     Enter details for a new contact. Phone and email are validated.
   - `2. View Contacts`  
     See all contacts in a sorted list.
   - `3. Search Contact`  
     Search by name or phone number.
   - `4. Update Contact`  
     Find and update an existing contact.
   - `5. Delete Contact`  
     Find and delete a contact.
   - `6. Export to JSON`  
     Export all contacts to `contacts.json`.
   - `7. Exit`  
     Exit the application.

## Data Format

- **CSV:** All contacts are stored in `contacts.csv` with columns: name, phone, email, address.
- **JSON:** Exported contacts are saved in `contacts.json` as a list of dictionaries.

## Requirements

- Python 3.x

## Notes

- Phone numbers must be in the format: `03001234567`, `9203001234567`, or `+923001234567`.
- Email addresses are validated with a regular expression.
- All data is stored locally; deleting the CSV file will remove all contacts.

---

**Happy Contact