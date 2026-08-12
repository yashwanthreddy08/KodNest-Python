class Book:

    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

title = input("Enter the Title: ").strip()
author= input("Enter the Author: ").strip()
price = int(input("Enter the price: "))

book = Book(title, author, price)

print("BOOK DETAILS")
print(f"Title: {book.title}")
print (f"Author: {book.author}")
print(f"Price: {book.price}")