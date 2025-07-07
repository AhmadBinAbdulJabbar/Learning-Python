from datetime import datetime, date, timedelta

# Library Management System Project Structure

# 1. Book class
#    - Represents a single book in the library.
#    - Attributes: title, author, isbn, available
#    - Methods:
#        - issue(): Mark the book as issued (not available)
#        - return_book(): Mark the book as available
#        - Getters and setters for all attributes

class Book:
    def __init__(self, title, author, isbn, category=None):
        self._title = title
        self._author = author
        self._isbn = isbn
        self._available = True
        self._category = category
        self._reviews = []

    @property
    def title(self):
        return self._title
    
    @property
    def author(self):
        return self._author
    
    @property 
    def isbn(self):
        return self._isbn

    @property
    def available(self):
        return self._available
    
    @property
    def category(self):
        return self._category
    
    @category.setter
    def category(self, category):
        self._category = category

    def issue(self):
        if not self._available:
            raise Exception("Book already issued.")
        self._available =  False

    def return_book(self):
        self._available = True

    @title.setter
    def title(self, title):
        self._title = title

    @author.setter
    def author(self, author):
        self._author = author

    @isbn.setter
    def isbn(self, isbn):
        self._isbn = isbn

    def add_reviews(self, member, review, rating):
        """Add a review with rating for the book"""
        if not(0 <= rating <= 5):
            raise ValueError("Rating must be between 0 and 5")
        
        self._reviews.append(
            {
                "member": member,
                "review": review,
                "rating": rating,
                "date": datetime.now()
            }
        )

    @property
    def average_rating(self):
        """Calculating the average rating of the book"""
        if not self._reviews:
            return 0
        return sum(review["rating"] for review in self._reviews) / len(self._reviews)
        
    def get_reviews(self):
        """Return all reviews and ratings"""
        return self._reviews

    def __str__(self):
        return f"{self._title} by {self._author} having ISBN {self._isbn}"

# 2. Member class
#    - Represents a library member (user).
#    - Attributes: name, member_id, list of borrowed books
#    - Methods:
#        - borrow_book(book): Add a book to borrowed list
#        - return_book(book): Remove a book from borrowed list
#        - Getters and setters for all attributes

class Member:
    borrowing_limit = 3
    def __init__(self, name, member_id):
        self._name = name
        self._member_id = member_id
        self._borrowed_books = {}

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        try:
            if name == "":
                raise ValueError("Error empty name cannot be asigned")
            else:
                self._name = name
        except Exception as e:
            print(e)

    @property
    def member_id(self):
        return self._member_id
    
    @member_id.setter
    def member_id(self, member_id):
        self._member_id = member_id
    
    @property
    def borrowed_books(self):
        return list(self._borrowed_books.keys())
    
    def borrow_book(self, book):
        if len(self._borrowed_books) >= Member.borrowing_limit:
            print(f"You have already browwed {Member.borrowing_limit} books with is limit. First return a book then you can borrow this book!")
            return False
        try:
            if book not in self._borrowed_books and book.available:
                self._borrowed_books[book] = datetime.now()
                return True
            else:
                raise ValueError("Book already in the list")
        except Exception as e:
            print(e)
            return False
        
    def return_book(self, book):
        try:
            if book in self._borrowed_books:
                issue_date = self._borrowed_books.pop(book)
                book.return_book()
                days_borrowed = (datetime.now() - issue_date).days
                if days_borrowed > 14:
                    fine = (days_borrowed - 14) * 10
                    print(f"Late return! Fine: {fine}")
                return True
            else:
                raise ValueError("Book not in the borrowed list. ")
        except Exception as e:
            print(e)
            return False


# 3. Library class
#    - Represents the library itself.
#    - Attributes: list of books, list of members
#    - Methods:
#        - add_book(book): Add a new book to the library
#        - remove_book(book): Remove a book from the library
#        - find_book(title/isbn): Search for a book
#        - register_member(member): Add a new member
#        - issue_book(book, member): Issue a book to a member
#        - return_book(book, member): Accept a returned book from a member
#        - list_available_books(): Show all available books
#        - list_issued_books(): Show all issued books

class Library:
    def __init__(self, books=None, members=None):
        self._books = books if books is not None else []
        self._members = members if members is not None else []

    def add_book(self, book):
        if any(b.isbn == book.isbn for b in self._books):
            print("A book with this ISBN already exists.")
            return False
        self._books.append(book)
        return True

    def remove_book(self, book):
        if book.available:
            self._books.remove(book)
            print("Successfully removed. ✅")
            return True
        else: 
            print("Book is issued to a member. You can not remove it. First make it available.")
            return False

    def find_book(self, title=None, isbn=None, author=None):
        all_matches = []
        for book in self._books:
            if title and title in book.title.lower():
                all_matches.append(book)
            if isbn and book.isbn.lower() == isbn:
                return book
            if author and author in book.author.lower():
                all_matches.append(book)

        if len(all_matches) == 1:
            return all_matches[0]
        elif len(all_matches) > 1:
            return all_matches
        else:
            return None
        
    def register_member(self, member): 
        if any(m.member_id == member.member_id for m in self._members):
            print("A member with this ID already exists.")
            return False
        self._members.append(member)
        return True

    def remove_member(self, member):
        if len(member.borrowed_books()) > 0:
                print("Member has borrowed books. return them first then you can remove him.")
                return False
        else:
            self._members.remove(member)
            print("Member removed successfully. ✅")
            return True

    def issue_book(self, book, member):
        for m in self._members:
            if m.member_id ==  member.member_id:
                try:
                    if book.available:
                        m.borrow_book(book)
                        book.issue()
                        return True
                except Exception as e:
                    print(e)
                    return False
        return False

    def return_book(self, book, member):
        for m in self._members:
            if m.member_id ==  member.member_id:
                m.return_book(book)
                book.return_book()
                return True
        return False

    def list_available_books(self):
        return [book for book in self._books if book.available == True]
    
    def list_issued_books(self):
        return [book for book in self._books if book.available == False]
    
    def get_statistics(self):
        return {
            "total_books": len(self._books),
            "total_available_books": len(self.list_available_books()),
            "total_issued_books": len(self.list_issued_books()),
            "total_members": len(self._members)
        }


# 4. Admin/User Interface class or functions
#    - Handles user input/output for interacting with the system
#    - Menu for adding/removing books, registering members, issuing/returning books, etc.

# You can expand with more features such as:
# - Book reservation
# - Fines for late returns
# - Book categories/genres
# - Exporting/importing data

# Start by implementing the Book, Member, and Library classes as described above.


def main_menu():
    library = Library()
    while True:
        print("\n=== Library Management System ===")
        print("1. Add Book")
        print("2. Register Member")
        print("3. Issue Book")
        print("4. Return Book")
        print("5. List Available Books")
        print("6. List Issued Books")
        print("7. Remove Book")
        print("8. Remove Member")
        print("9. Search Book")
        print("0. Exit")
        choice = input("Select an option: ")

        if choice == "1":
            title = input("Book title: ")
            author = input("Author: ")
            isbn = input("ISBN: ")
            book = Book(title, author, isbn)
            code = library.add_book(book)
            if code:
                print("Book was added successfully. ✅")
            else:
                print("Book was not added ❌.")

        elif choice == "2":
            name = input("Member name: ")
            member_id = input("Member ID: ")
            member = Member(name, member_id)
            code = library.register_member(member)
            if code:
                print("Member registered. ✅")
            else:
                print("Member not registered. ❌")

        elif choice == "3":
            member_id = input("Member ID: ")
            isbn = input("Book ISBN: ")
            member = next((m for m in library._members if m.member_id == member_id), None)
            book = next((b for b in library._books if b.isbn == isbn), None)
            if member and book:
                if library.issue_book(book, member):
                    print("Book issued.")
                else:
                    print("Could not issue book.")
            else:
                print("Member or book not found.")

        elif choice == "4":
            member_id = input("Member ID: ")
            isbn = input("Book ISBN: ")
            member = next((m for m in library._members if m.member_id == member_id), None)
            book = next((b for b in library._books if b.isbn == isbn), None)
            if member and book:
                if library.return_book(book, member):
                    print("Book returned.")
                else:
                    print("Could not return book.")
            else:
                print("Member or book not found.")

        elif choice == "5":
            print("Available books:")
            for book in library.list_available_books():
                print(f"{book.title} by {book.author} (ISBN: {book.isbn})")

        elif choice == "6":
            print("Issued books:")
            for book in library.list_issued_books():
                print(f"{book.title} by {book.author} (ISBN: {book.isbn})")
        elif choice == "7":
            isbn = input("Enter ISBN of the book to remove: ").strip()
            book = next((b for b in library._books if b.isbn == isbn), None)

            if book:
                library.remove_book(book)
            else:
                print("Book not found.")
        elif choice == "8":
            member_id = input("Enter member_id to remove: ").strip()
            member = next((m for m in library._members if m.member_id == member_id), None)

            if member:
                library.remove_member(member)
            else:
                print("Member not found.")

        elif choice == "9":
            print("searching for books by title, author, or ISBN.")
            search_type = input("By which you want to search? ").strip().lower()

            if search_type == "title":
                title = input("Enter Title: ").strip().lower()
                book = library.find_book(title=title)
            elif search_type == "author":
                author = input("Enter Author name: ").strip().lower()
                book = library.find_book(author=author)
            elif search_type == "isbn":
                isbn = input("Enter isbn: ").strip().lower()
                book = library.find_book(isbn=isbn)

            if book:
                if isinstance(book, list):
                    print(f"Found {len(book)} books: ")
                    for b in book:
                        print(b)
                else:
                    print("Found book: ")
                    print(book)
            else:
                print("Book not found!")
                    
        elif choice == "10":
            isbn = input("Enter ISBN of the book to review: ").strip()
            book = next((b for b in library._books if b.isbn == isbn), None)
            if not book:
                print("Book not found.")
                continue

            print(f"\nBook: {book.title} by {book.author}")
            print(f"Average Rating: {book.average_rating:.1f}/5")
            print("\nReviews:")
            reviews = book.get_reviews()
            if reviews:
                for review in reviews:
                    print(f"- {review['member'].name} rated {review['rating']}/5: {review['review']} ({review['date'].strftime('%Y-%m-%d')})")
            else:
                print("No reviews yet.")

            add_review = input("\nWould you like to add a review? (y/n): ").strip().lower()
            if add_review == "y":
                member_id = input("Enter your member ID: ").strip()
                member = next((m for m in library._members if m.member_id == member_id), None)
                if not member:
                    print("Member not found.")
                    continue
                try:
                    rating = float(input("Enter rating (0-5): ").strip())
                    review_text = input("Enter your review: ").strip()
                    book.add_reviews(member, review_text, rating)
                    print("Review added successfully!")
                except Exception as e:
                    print(f"Error adding review: {e}")            

        elif choice == "0":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Try again.")

def test():
    print("=== TESTING LIBRARY MANAGEMENT SYSTEM ===")
    library = Library()

    # Add books
    book1 = Book("Python 101", "John Doe", "123")
    book2 = Book("Data Science", "Jane Smith", "456")
    book3 = Book("Python Advanced", "John Doe", "789")
    print("Add book1:", library.add_book(book1))  # True
    print("Add book2:", library.add_book(book2))  # True
    print("Add duplicate book1:", library.add_book(book1))  # False

    # Add members
    member1 = Member("Alice", "M001")
    member2 = Member("Bob", "M002")
    print("Register member1:", library.register_member(member1))  # True
    print("Register member2:", library.register_member(member2))  # True
    print("Register duplicate member1:", library.register_member(member1))  # False

    # Issue book1 to member1
    print("Issue book1 to member1:", library.issue_book(book1, member1))  # True
    print("Issue book1 to member2 (should fail):", library.issue_book(book1, member2))  # False

    # Try to remove issued book
    print("Remove issued book1 (should fail):")
    if book1.available:
        library.remove_book(book1)
        print("Book removed.")
    else:
        print("Book is issued to a member.")

    # Return book1 from member1 (simulate late return)
    # Manually set borrow date to 20 days ago for fine test
    member1._borrowed_books[book1] = datetime.now() - timedelta(days=20)
    print("Return book1 from member1 (should show fine):", library.return_book(book1, member1))  # True

    # Remove book1 (now available)
    print("Remove book1 (should succeed):")
    if book1.available:
        library.remove_book(book1)
        print("Book removed.")
    else:
        print("Book is issued to a member.")

    # Issue book2 to member2
    print("Issue book2 to member2:", library.issue_book(book2, member2))  # True

    # Try to remove member2 (should fail)
    print("Remove member2 (should fail):")
    if len(member2.borrowed_books) > 0:
        print("Member has borrowed books. return them first then you can remove him.")
    else:
        library.remove_member(member2)
        print("Member removed.")

    # Return book2 from member2
    print("Return book2 from member2:", library.return_book(book2, member2))  # True

    # Remove member2 (should succeed)
    print("Remove member2 (should succeed):")
    if len(member2.borrowed_books) > 0:
        print("Member has borrowed books. return them first then you can remove him.")
    else:
        library.remove_member(member2)
        print("Member removed.")

    # Search by title
    print("Search by title 'python':")
    result = library.find_book(title="python")
    print(result if result else "Not found")

    # Search by author
    print("Search by author 'jane':")
    result = library.find_book(author="jane")
    print(result if result else "Not found")

    # Search by ISBN
    print("Search by ISBN '456':")
    result = library.find_book(isbn="456")
    print(result if result else "Not found")

    # List available and issued books
    print("Available books:", [b.title for b in library.list_available_books()])
    print("Issued books:", [b.title for b in library.list_issued_books()])

    # Show statistics
    print("Library statistics:", library.get_statistics())


if __name__ == "__main__":
    # main_menu()
    test()


