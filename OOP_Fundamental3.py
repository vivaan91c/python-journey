# You're building a Library Management System. Books can be added, borrowed, and returned.
# Members can join and borrow books.
# Premium members get extra privileges. You'll use every OOP concept — one step at a time — to build the whole system.

# 1) Create the Book blueprint

class Book:
    pass

book1 = Book()
book2 = Book()
print(type(book1))


# 2) Set up book details with __init__

class Book:
    def __init__(self, title, author, copies):
        self.title = title
        self.author = author
        self.copies = copies

book1 = Book("The Alchemist", "Paulo Coelho", 3)
print(book1.title)
print(book1.author)
print(book1.copies)


# 3) Add borrow and return methods


class Book:
    def __init__(self, title, author, copies):
        self.title = title
        self.author = author
        self.copies = copies

    def borrow(self):
        if self.copies > 0:
            self.copies -= 1
            print("Borrowed!")
        else:
            print("No copies available.")

    def return_book(self):
        self.copies += 1
        print("Returned!")

book1 = Book("The Alchemist", "Paulo Coelho", 3)
book1.borrow()
book1.return_book()



# 4) Stock the library with multiple books


class Book:
    def __init__(self, title, author, copies):
        self.title = title
        self.author = author
        self.copies = copies

    def borrow(self):
        if self.copies > 0:
            self.copies = self.copies - 1
            print(self.title, "has been borrowed")
            print("Copies remaining:", self.copies)
        else:
            print("No copies available")

    def return_book(self):
        self.copies = self.copies + 1
        print(self.title, "has been returned")


book1 = Book("The Alchemist", "Paulo Coelho", 3)
book2 = Book("Atomic Habits", "James Clear", 5)
book3 = Book("Rich Dad Poor Dad", "Robert Kiyosaki", 2)

book1.borrow()
book2.borrow()
book3.borrow()



# 5) Update a book's copy count

class Book:
    def __init__(self, title, author, copies):
        self.title = title
        self.author = author
        self.copies = copies

    def borrow(self):
        if self.copies > 0:
            self.copies = self.copies - 1
            print(self.title, "has been borrowed")
            print("Copies remaining:", self.copies)
        else:
            print("No copies available")

    def return_book(self):
        self.copies = self.copies + 1
        print(self.title, "has been returned")


book1 = Book("The Alchemist", "Paulo Coelho", 3)
book2 = Book("Atomic Habits", "James Clear", 5)
book3 = Book("Rich Dad Poor Dad", "Robert Kiyosaki", 2)

print(book2.copies)

book2.copies = book2.copies + 10
print(book2.copies)

book2.borrow()


# 6) Make books printable with __str__

class Book:
    def __init__(self, title, author, copies):
        self.title = title
        self.author = author
        self.copies = copies

    def borrow(self):
        if self.copies > 0:
            self.copies = self.copies - 1
            print(self.title, "has been borrowed")
            print("Copies remaining:", self.copies)
        else:
            print("No copies available")

    def return_book(self):
        self.copies = self.copies + 1
        print(self.title, "has been returned")
    
    def __str__(self):
        return f"{self.title} by {self.author} | Available copies: {self.copies}"
    
book1 = Book("The Alchemist", "Paulo Coelho", 3)
book2 = Book("Atomic Habits", "James Clear", 5)
book3 = Book("Rich Dad Poor Dad", "Robert Kiyosaki", 2)

print(book1)
print(book2)
print(book3)


# 7) Create Member and PremiumMember

class Member:
    def __init__(self, name):
        self.name = name
        self.books_borrowed = 0

    def borrow_book(self):
        self.books_borrowed += 1
        print("Borrowing book...")
        print("Books borrowed:", self.books_borrowed)


class PremiumMember(Member):
    def __init__(self, name):
        super().__init__(name)
        self.max_books = 10

    def borrow_book(self):
        if self.books_borrowed < self.max_books:
            super().borrow_book()
            print("Premium: borrowing with priority!")
        else:
            print("Maximum book limit reached.")


m1 = Member("Arjun")
pm1 = PremiumMember("Ram")

m1.borrow_book()
pm1.borrow_book()


# 8) Run the full library catalogue

class Book:
    def __init__(self, title, author, copies):
        self.title = title
        self.author = author
        self.copies = copies

    def borrow(self):
        if self.copies > 0:
            self.copies -= 1
            print("Book borrowed successfully.")
        else:
            print("No copies available.")

    def return_book(self):
        self.copies += 1
        print("Book returned successfully.")

    def __str__(self):
        return f"{self.title} by {self.author} | Available copies: {self.copies}"


# List containing 4 Book objects
books = [
    Book("The Alchemist", "Paulo Coelho", 3),
    Book("Atomic Habits", "James Clear", 5),
    Book("Rich Dad Poor Dad", "Robert Kiyosaki", 2),
    Book("Ikigai", "Hector Garcia", 4)
]


for book in books:
    print(book)  # Automatically calls __str__()

    if book.copies > 2:
        book.borrow()
        print("Remaining copies:", book.copies)
    else:
        print("Not borrowed because copies are 2 or less.")

    print()


