import sqlite3

def create_table():
    db = sqlite3.connect("bookstore.db")
    cursor = db.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY,
            title TEXT,
            author TEXT,
            quantity INTEGER
        )
    ''')
    
    Book_information = [
        (3001, "A Tale of Two Cities", "Charles Dickens", 30),
        (3002, "Harry Potter and the Philosopher's Stone", "J.K Rowling", 40),
        (3003, "The Lion, the Witch and the Wardrobe", "C.S Lewis", 25),
        (3004, "The Lord of the Rings", "J.R.R Tolkien", 37),
        (3005, "Alice In Wonderland", "Lewis Carrol", 12)
    ]
    
    cursor.executemany('''
            INSERT INTO books (id, title, author, quantity)
            VALUES(?, ?, ?, ?)              
    ''', Book_information)
    
    db.commit()
    db.close()

def add_book(id, title, author, quantity):
    db = sqlite3.connect("bookstore.db")
    cursor = db.cursor()

    cursor.execute('''
        INSERT INTO books (id, title, author, quantity)
        VALUES (?, ?, ?, ?)
    ''', (id, title, author, quantity))

    db.commit()
    db.close()

def update_book(book_id, title, author, quantity):
    db = sqlite3.connect("bookstore.db")
    cursor = db.cursor()

    # Update book information
    cursor.execute('''
        UPDATE books
        SET title=?, author=?, quantity=?
        WHERE id=?
    ''', (title, author, quantity, book_id))

    db.commit()
    db.close()

def delete_book(book_id):
    db = sqlite3.connect("bookstore.db")
    cursor = db.cursor()

    # Delete book from the database
    cursor.execute('''
        DELETE FROM books
        WHERE id=?
    ''', (book_id,))

    db.commit()
    db.close()

def search_book(title):
    db = sqlite3.connect("bookstore.db")
    cursor = db.cursor()

    # Search for the availability of a book
    cursor.execute('''
        SELECT title, author, quantity
        FROM books
        WHERE title=?
    ''', (title,))

    result = cursor.fetchone()
    db.close()

    if result:
        print("Book Found:")
        print("Title:", result[0])
        print("Author:", result[1])
        print("Availability:", "Available" if result[2] else "Not Available")
    else:
        print("Book not found.")

# Main program
create_table()

while True:
    print("\nBookstore Management System")
    print("1. Add New Book")
    print("2. Update Book Information")
    print("3. Delete Book")
    print("4. Search Book Quantity")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        id = int(input("Enter book id: "))
        title = input("Enter book title: ")
        author = input("Enter author name: ")
        quantity = int(input("Enter availability (1 for available, 0 for not available): "))
        add_book(id, title, author, quantity)

    elif choice == "2":
        book_id = int(input("Enter book ID to update: "))
        title = input("Enter new book title: ")
        author = input("Enter new author name: ")
        quantity = int(input("Enter new availability (1 for available, 0 for not available): "))
        update_book(book_id, title, author, quantity)

    elif choice == "3":
        book_id = int(input("Enter book ID to delete: "))
        delete_book(book_id)

    elif choice == "4":
        title = input("Enter book title to search: ")
        search_book(title)

    elif choice == "5":
        print("Exiting the program.")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 5.")