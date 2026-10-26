books=[]
while True:
    print("===== Book Tracker====")
    print("1 Add Book")
    print("2.View Book ")
    print("3 Exit")

    choice=input("Enter your choice:")

    if choice=="1":
        title=input("Enter book title:")
        author=input("Enter author name:")

        book={
            "title":title,
            "author":author,
            "status":"Not started"

        }
        books.append(book)
        print("Book added successfully!")

    elif choice=="2":
        if not books:
            print("No books found!")
        else:
            print("\n Your book Collection:")
            for i ,book in enumerate(books,1):
                print(f"{i}.{book["status"]} by {book['author']}")
                print("status:",book["status"])
    elif choice=="3":
        print("Thank you for using Book Tracker!")
        break
    else:
        print("Invalid choice!please try again. ")
                