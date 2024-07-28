# Custom Packages
from book import BookManager 

########################################################################################################

def main_menu() -> str:
    """
    Displays the main menu and prompts the user to choose an option.

    Returns:
        str: The choice entered by the user.
    """
    print("\nLibrary Management System")
    print("1. Add Book")
    print("2. Update Book")
    print("3. Delete Book")
    print("4. List Book")
    print("5. Search Book")
    print("6. Exit")
    choice = input("Enter choice: ")
    return choice

########################################################################################################

def add_book(book_management: BookManager) -> None:
    """
    Prompts the user to enter book details and adds the book to the database.

    Args:
        book_management (BookManager): The BookManager instance.
    """
    title = input("Enter title: ")
    author = input("Enter author: ")
    isbn = int(input("Enter ISBN: "))
    genre = input("Enter Genre: ")
    lang = input("Enter Language: ")
    book_management.add_book(title=title, author=author, isbn=isbn, genre=genre, lang=lang)
    print("Book added.")

########################################################################################################

def update_book(book_management: BookManager) -> None:
    """
    Prompts the user to enter book details and updates the book in the database.

    Args:
        book_management (BookManager): The BookManager instance.
    """
    id = input("Enter ID: ")
    isbn = input("Enter ISBN: ")
    title = input("Enter Title: ")
    author = input("Enter Author: ")
    genre = input("Enter Genre: ")
    lang = input("Enter Language: ")
    book_management.update_book(id=id, title=title, author=author, isbn=isbn, genre=genre, lang=lang)
    print("Book Information updated.")

########################################################################################################

def delete_book(book_management: BookManager) -> None:
    """
    Prompts the user to enter book details and deletes the book from the database.

    Args:
        book_management (BookManager): The BookManager instance.
    """
    id = input("Enter ID: ")
    isbn = input("Enter ISBN: ")
    title = input("Enter Title: ")
    book_management.delete_book(id=id, title=title, isbn=isbn)
    print("Book Information Deleted.")

########################################################################################################

def list_book(book_management: BookManager) -> None:
    """
    Prompts the user to enter book details and lists the books from the database.

    Args:
        book_management (BookManager): The BookManager instance.
    """
    id = input("Enter ID: ")
    isbn = input("Enter ISBN: ")
    title = input("Enter Title: ")
    data = book_management.list_book(id=id, title=title, isbn=isbn)
    print(data)
    print("Book Listed Information.")

########################################################################################################

def search_book(book_management: BookManager) -> None:
    """
    Prompts the user to enter book details and searches for the book in the database.

    Args:
        book_management (BookManager): The BookManager instance.
    """
    id = input("Enter ID: ")
    isbn = input("Enter ISBN: ")
    title = input("Enter Title: ")
    data = book_management.search_book(id=id, title=title, isbn=isbn)
    print(data)
    print("Book Searched Information.")

########################################################################################################

def main() -> None:
    """
    The main function to run the Library Management System.
    """
    book_management = BookManager()
    while True:
        choice = main_menu()

        if choice == '1':
            add_book(book_management)
        elif choice == '2':
            update_book(book_management)
        elif choice == '3':
            delete_book(book_management)
        elif choice == '4':
            list_book(book_management)
        elif choice == '5':
            search_book(book_management)
        elif choice == '6':
            print("Exiting.")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
