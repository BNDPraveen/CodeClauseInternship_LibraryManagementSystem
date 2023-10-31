import datetime

class LMS:
    """
    This class is designed to manage a library's book records.
    It provides four main modules: "Display Books", "Issue Books", "Return Books", and "Add Books".
    """

    def __init__(self, list_of_books, library_name):
        self.list_of_books = list_of_books
        self.library_name = library_name
        self.books_dict = {}
        Id = 101

        # Read the list of books from a file and initialize the library database
        with open(self.list_of_books) as bk:
            content = bk.readlines()
        for line in content:
            self.books_dict.update(
                {
                    str(Id): {
                        "book_title": line.replace("\n", ""),
                        "lender_name": "",
                        "Issue_date": "",
                        "Status": "Available",
                    }
                }
            )
            Id = Id + 1

    def display_books(self):
        # Display the list of books and their status
        print("----------------------List of Books---------------------------")
        print("Book Id", "\t", "Title")
        print("--------------------------------------------------------------")
        for key, value in self.books_dict.items():
            print(
                key,
                "\t\t",
                value.get("book_title"),
                "- [",
                value.get("Status"),
                "]",
            )

    def Issue_books(self):
        # Issue a book to a user
        books_id = input("Enter book ID: ")
        current_date = datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S")
        if books_id in self.books_dict.keys():
            if not (self.books_dict[books_id]["Status"] == "Available"):
                print(
                    f"This book is already issued to {self.books_dict[books_id]['lender_name']} on {self.books_dict[books_id]['Issue_date']}"
                )
                return self.Issue_books()
            elif self.books_dict[books_id]["Status"] == "Available":
                your_name = input("Enter your name: ")
                self.books_dict[books_id]["lender_name"] = your_name
                self.books_dict[books_id]["Issue_date"] = current_date
                self.books_dict[books_id]["Status"] = "already Issued"
                print(
                    f"Book Issued Successfully to {self.books_dict[books_id]['lender_name']} on {self.books_dict[books_id]['Issue_date']} !!! \n"
                )
        else:
            print("Book ID not found")
            #return self.Issue_books()

    def add_books(self):
        # Add a new book to the library
        new_books = input("Enter book title: ")
        if new_books == "":
            return self.add_books()
        elif len(new_books) > 25:
            print("Book title length too long!!! Title length should be 20 characters")
            return self.add_books()
        else:
            with open(self.list_of_books, "a") as bk:
                bk.writelines(f"{new_books}\n")
                self.books_dict.update(
                    {
                        str(int(max(self.books_dict)) + 1): {
                            "book_title": new_books,
                            "lender_name": "",
                            "Issue_date": "",
                            "Status": "Available",
                        }
                    }
                )
                print(f"This book '{new_books}' has been added successfully !!!")

    def return_books(self):
        # Return a book to the library
        books_id = input("Enter book ID: ")
        if books_id in self.books_dict.keys():
            if self.books_dict[books_id]["Status"] == "Available":
                print(
                    "This book is already present in the library. Please check your book ID."
                )
            else:
                self.books_dict[books_id]["lender_name"] = ""
                self.books_dict[books_id]["Issue_date"] = ""
                self.books_dict[books_id]["Status"] = "Available"
                print("Successfully updated !!!\n")
        else:
            print("Book ID is not found")


try:
    myLMS = LMS("List_of_books.txt", "Python's")
    press_key_list = {
        "D": "Display Books",
        "I": "Issue Books",
        "A": "Add Books",
        "R": "Return Books",
        "Q": "Quit",
    }
    key_press = False
    while not (key_press == "q"):
        print(
            f"\n-------Welcome To {myLMS.library_name} Library Management System------------\n"
        )
        for key, value in press_key_list.items():
            print("Press", key, "To", value)
        key_press = input("Press key: ").lower()
        if key_press == "i":
            print("\nCurrent Selection: Issue Books")
            myLMS.Issue_books()
        elif key_press == "a":
            print("\nCurrent Selection: Add Books")
            myLMS.add_books()
        elif key_press == "d":
            print("\nCurrent Selection: Display Books")
            myLMS.display_books()
        elif key_press == "r":
            print("\nCurrent Selection: Return Books")
            myLMS.return_books()
        else:
            continue
except Exception:
    print("Something went wrong. Please check your input !!!")
