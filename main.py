from library_books import library_books
from datetime import datetime, timedelta

# -------- Level 1 --------
# TODO: Create a function to view all books that are currently available
# Output should include book ID, title, and author
# help used: Google search "how to iterate through a dictionary"
# video used for accessing a dictionary syntax: https://www.youtube.com/watch?v=6x8oN6FtpLo
def view_available_books(all_books):
    for book in all_books:
        if book["available"]:
            print("ID:", book["id"])
            print("Title:", book["title"])
            print("Author:", book["author"])
            print()


# -------- Level 2 --------
# TODO: Create a function to search books by author OR genre
# Search should be case-insensitive
# Return a list of matching books

def search_books(all_books):
    method = input("Do you want to search by author or genre? ").lower()
    if method == "author":
        author = input("Enter the author: ").lower()
        for book in all_books:
            if book["author"].lower() == author:
                print("ID:", book["id"])
                print()
    elif method == "genre":
        genre = input("Enter the genre: ").lower()
        for book in all_books:
            if book["genre"].lower() == genre:
                print("ID:", book["id"])
                print()         
    else:
        print("Try again ") #asked chatgpt how to approach recursion for invalid input
        search_books(all_books)

# -------- Level 3 --------
# TODO: Create a function to checkout a book by ID
# If the book is available:
#   - Mark it unavailable
#   - Set the due_date to 2 weeks from today
#   - Increment the checkouts counter
# If it is not available:
#   - Print a message saying it's already checked out
def checkout_book(all_books):
    ID = input("Enter book ID: ").upper()
    for book in all_books:
        if book["id"] == ID:
            if book["available"] == True:
                book["available"] = False
                book["due_date"] = (datetime.now() + timedelta(weeks=2)) #asked github ai about how to approach the datetime logic
                book["checkouts"] += 1
                print("Book checked out ")
                return
            else:
                print("Book is already checked out ")
                return
    print("Try again ")
    return checkout_book(all_books)
# -------- Level 4 --------
# TODO: Create a function to return a book by ID
# Set its availability to True and clear the due_date

# TODO: Create a function to list all overdue books
# A book is overdue if its due_date is before today AND it is still checked out

def return_book(all_books):
    ID = input("Enter book ID: ").upper()
    for book in all_books:
        if book["id"] == ID:
            if not book["available"]:
                book["available"] = True
                book["due_date"] = None
                print("Book returned")
            else:
                print("Book not checked out")
            return
    print("Try again ")
    return return_book(all_books)

def overdue_books(all_books):
    today = datetime.now()
    for book in all_books:
        if book["due_date"] != None:
            if book["due_date"] < today and book["available"] != True: # asked github ai how to compare datetime
                print("ID:", book["id"])
                print()

# -------- Level 5 --------
# TODO: Convert your data into a Book class with methods like checkout() and return_book()
# TODO: Add a simple menu that allows the user to choose different options like view, search, checkout, return, etc.

# -------- Optional Advanced Features --------
# You can implement these to move into Tier 4:
# - Add a new book (via input) to the catalog
# - Sort and display the top 3 most checked-out books
# - Partial title/author search
# - Save/load catalog to file (CSV or JSON)
# - Anything else you want to build on top of the system!

if __name__ == "__main__":
    # You can use this space to test your functions
    #view_available_books(library_books)
    #search_books(library_books)
    #checkout_book(library_books)
    #return_book(library_books)
    #overdue_books(library_books)
