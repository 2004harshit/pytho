class Library :
    no_of_books=0
    books = []
    def bookRecord(self,book):
        self.books.append(book)
        self.no_of_books +=1
    
    def countBook(self):
        print(f"no of books in library : {self.no_of_books}")

    def printBookRecord(self):
        for book in self.books:
            print( f"{book}" )



l= Library()
l.bookRecord('The wings of fire ')
l.bookRecord('How to win friends')
l.countBook()
l.printBookRecord()