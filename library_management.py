# Library Management System

# 1. & 2. Creating a list and storing book info in a dictionary
books = [
    {"title": "Python Basics", "author": "John Smith", "year": 2020},
    {"title": "Data Science 101", "author": "Jane Doe", "year": 2022},
    {"title": "Web Dev Guide", "author": "Alan Turing", "year": 2018}
]

print("--- Library System ---")

# 3. Allow user to Search, Add, and Display
while True:
    print("\n1. Search Book\n2. Add Book\n3. Display All\n4. Filter by Year\n5. Exit")
    choice = input("Enter choice (1-5): ")

    if choice == '1':
        search_title = input("Enter book title to search: ")
        found = False
        for book in books:
            if book["title"].lower() == search_title.lower():
                print(f"Found: {book['title']} by {book['author']} ({book['year']})")
                found = True
        if not found:
            print("Book not found.")

    elif choice == '2':
        new_title = input("Enter title: ")
        new_author = input("Enter author: ")
        new_year = int(input("Enter year: "))
        books.append({"title": new_title, "author": new_author, "year": new_year})
        print("Book added successfully!")

    elif choice == '3':
        print("\nAll Books:")
        for book in books:
            print(f"- {book['title']} by {book['author']}")

    elif choice == '4':
        # 4. List comprehension to return books after a given year
        year_limit = int(input("Show books published after year: "))
        filtered_books = [b["title"] for b in books if b["year"] > year_limit]
        print(f"Books after {year_limit}: {filtered_books}")

    elif choice == '5':
        break