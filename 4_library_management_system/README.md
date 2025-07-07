# Library Management System

A terminal-based Python application to manage books, members, borrowing, returning, and book reviews in a library. This project demonstrates object-oriented programming concepts such as encapsulation and abstraction.

## Features

- **Add Book:** Add new books with title, author, ISBN, and optional category.
- **Register Member:** Register new library members with a unique member ID.
- **Issue Book:** Issue available books to members (with borrowing limits).
- **Return Book:** Return borrowed books and calculate fines for late returns.
- **Remove Book/Member:** Remove books (if not issued) and members (if no books borrowed).
- **List Available/Issued Books:** View all available or currently issued books.
- **Search Book:** Search for books by title, author, or ISBN.
- **Book Reviews:** View and add reviews and ratings for books.
- **Statistics:** View total books, available/issued books, and total members.
- **Automated Testing:** Includes a `test()` function to verify all core features.

## How to Use

1. **Run the Application**
   ```bash
   python main.py
   ```

2. **Menu Options**
   - `1. Add Book`
   - `2. Register Member`
   - `3. Issue Book`
   - `4. Return Book`
   - `5. List Available Books`
   - `6. List Issued Books`
   - `7. Remove Book`
   - `8. Remove Member`
   - `9. Search Book`
   - `10. Add/Show Book Reviews`
   - `0. Exit`

3. **Testing**
   - To run automated tests, uncomment `test()` and comment out `main_menu()` in the `if __name__ == "__main__":` block.

## Example

```
=== Library Management System ===
1. Add Book
2. Register Member
3. Issue Book
...
Select an option: 1
Book title: Python 101
Author: John Doe
ISBN: 123
Book was added successfully. ✅
```

## Requirements

- Python 3.x

## Notes

- Members can borrow up to 3 books at a time.
- Late returns (after 14 days) incur a fine.
- Books cannot be removed if currently issued.
- Members cannot be removed if they have borrowed books.
- All data is stored in memory for the current session only.

---