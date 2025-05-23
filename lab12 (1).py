class LibraryBook:
    def __init__(self, title: str, author: str ,renew_count = 0):
        self.title = title
        self.author = author
        self.is_checked_out = False
        self.borrower = ""
        self.renew_count = renew_count
    def get_author(self):
        # return the author's name
        return self.author
    def get_title(self):
        # return the book's title
        return self.title
    def get_borrower(self):
        # return the name of the borrower or "NONE" if the book is not checked out
        if self.is_checked_out:
            return self.borrower
        else:
            return "NONE"
    def check_out(self, borrower_name: str):
        # check out the book to the given borrower
        if self.is_checked_out == True:
            return -1
        else:
            self.borrower = borrower_name
            self.is_checked_out = True
            self.renew_count = 0
            return 1
    def renew(self):
        # renew the book for the current borrower
        if self.is_checked_out:
            self.renew_count = self.renew_count + 1
            return 1
        else:
            return -1
    def return_book(self):
        # return the book to the library
        if not self.is_checked_out:
            return -1
        else:
            self.borrower = ""
            self.is_checked_out = False
            self.renew_count = 0
            return 1
    def get_status(self):
        # return True if the book is available for checkout, False otherwise
        if not self.is_checked_out:
            return "AVAILABLE"
        else:
            return "NOT AVAILABLE"
    def get_renew_count(self):
        # return the number of times the book has been renewed
        if not self.is_checked_out:
            return 0
        return self.renew_count
t,a = map(str,input().split())
book = LibraryBook(t,a)
inp = ''
c = 0
while True:
    inp = input()
    if inp == "END":
        break
    elif "author?" in inp:
        print(book.get_author())
    elif "title?" in inp:
        print(book.get_title())
    elif "borrower?" in inp:
        print(book.get_borrower())
    elif 'check_out' in inp:
        print(book.check_out(inp.split()[1]))
    elif 'status?' in inp:
        print(book.get_status())
    elif "renew_count?" in inp:
        print(book.get_renew_count())
    elif "renew" in inp:
        print(book.renew())
    elif "return" in inp:
        print(book.return_book())