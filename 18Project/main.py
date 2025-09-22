class Book:

    def __init__(self, title, author, availability = True):
        self.title = title
        self.author = author
        self.availability = availability

    def checkOut(self):
        self.availability = False

    def returnBook(self):
        self.availability = True


def main():
    catalogue = [Book("The Book", "Kyle Webster", False), Book("The Book 2", "Kyle Webster")]

    loop = True

    while loop:
        newBook = input("Would you like to add a book to the catalogue (yes/no)?")
        if newBook == "yes":
            title = input("What is the title? ")
            author = input("What is the author?")
            catalogue.append(Book(title, author))

        else:
            loop = False

    print("The current catalogue of books and there availability is: ")
    for i in catalogue:
        if i.availability:
            print(f"{i.title} by {i.author} is currently available.")

main()