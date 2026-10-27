# 📚 Book Tracker

## About the Project
Book Tracker is a beginner-friendly Python project that helps users manage their personal book collection. It allows users to add books, view their collection, update reading status, and delete books through a simple menu-driven interface.

## Features
- **Add Book:** Add a book by entering its title and author's name.
- **View Books:** Display the book collection and reading status.
- **Update Reading Status:** Change the status to Not Started, Reading, or Completed.
- **Delete Book:** Remove a book from the collection using its book number.
- **Input Validation:** Handle invalid numerical inputs and book numbers.
- **Exit:** Exit the program safely.

## Technologies Used
- Python

## Concepts Used
- Lists and Dictionaries
- While Loop and For Loop
- Conditional Statements (`if-elif-else`)
- User Input (`input()`)
- `enumerate()`
- Exception Handling (`try-except`)
- List Methods (`append()` and `pop()`)

## How It Works
1. Run the Python program.
2. Select **1** to add a book.
3. Select **2** to view all books.
4. Select **3** to update a book's reading status.
5. Select **4** to delete a book.
6. Select **5** to exit the program.

## Reading Status Options
- Not Started
- Reading
- Completed

## Sample Output
```text
===== Book Tracker =====
1. Add Book
2. View Book
3. Update Reading Status
4. Delete Book
5. Exit

Enter your choice: 1
Enter book title: Atomic Habits
Enter author name: James Clear
Book added successfully!

Enter your choice: 2

Your book Collection:
1. Atomic Habits by James Clear
Status: Not started
```

## Learning Outcomes
- Understanding lists and dictionaries in Python.
- Performing add, view, update, and delete operations.
- Using loops and conditional statements.
- Handling invalid inputs using exception handling.
- Developing a menu-driven Python application.

## Limitation
The book collection is stored in memory and is lost when the program is closed.

## Author
**Riddhi Deshmukh**
