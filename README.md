# Library Management System

This Library Management System is a Python-based application that helps manage a collection of books. It allows you to add, update, delete, list, and search for books. The project includes two main files: `book.py` and `main.py`, as well as a `database` folder for storing book information.

## Requirements

- Python 3.8
- Pandas library

## Project Structure

### book.py

This file contains the `BookManager` class, which handles the main functions of the library system.

#### Main Functions:

1. **add_book**: Adds a new book to the library.
2. **update_book**: Updates information about an existing book.
3. **delete_book**: Marks a book as deleted in the system.
4. **list_book**: Lists all books based on certain filters.
5. **search_book**: Searches for books based on various criteria.

### main.py

This file contains the main script that runs the Library Management System. It provides a simple menu for users to interact with the system.

Menu options:

```python
print("1. Add Book")
print("2. Update Book")
print("3. Delete Book")
print("4. List Book")
print("5. Search Book")
print("6. Exit")
```

#### Functions:

1. **main_menu**: Displays the main menu and gets the user's choice.
2. **main**: The main loop that keeps the system running and calls the appropriate functions based on user input.

### database

This folder contains the `book_data.csv` file, which stores all the information about the books. If the file doesn't exist, it will be created automatically when books are added.

## How to Use

1. Clone the repository.
2. Make sure you have Python 3.8 and Pandas installed.
3. Run the `main.py` file to start the system.

```bash
python main.py
```

## Logging

The system logs important actions like adding, updating, deleting, listing, and searching for books to a file called `library_management.log`. This helps keep track of what happens in the system.

## Advanced Features

### Clustering Search Results

In the future, the system can be improved to group search results based on attributes like genre, author, or publication year. This will make it easier to find related books.

### Enhanced Search with AI

Using Large Language Models (LLM) and embedding methods, we can improve the search function:

- **Contextual Search**: Search for books based on themes or book summaries and get more relevant results.
- **Related Books**: The system can suggest related books and notebooks based on the search context.

### Recommendation System

We can add a feature to recommend books based on user preferences and book similarities. This will help users find new books they might like.

## Future Features

### Book Tracking

We plan to track how long a book is checked out:

- **Due Date Tracking**: Keep track of when each book is due.
- **Availability Notifications**: Notify users when a book they want becomes available.

### Late Return Notifications

To ensure books are returned on time, we can send notifications to users when their books are overdue. This will help keep books available for everyone.

## Conclusion

This Library Management System is a simple and effective way to manage books. It's easy to use and extend, with plans for advanced features and future improvements to make it even better.