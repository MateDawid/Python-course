from datetime import date
class Book:
    def __init__(self,title, author, pages,release_date):
        self.title = title
        self.author = author
        self.pages = pages
        self.release_date = release_date
    def __repr__(self):
        return 'Title: "'+self.title+'" - Release date: '+str(self.release_date)
    def get_days(self):
        return abs((date.today() - self.release_date).days)

books = []
b1 = Book("Ogniem i mieczem","XY",900,date(1969,12,21))
b2 = Book("Nówka","YZ",890,date(2020,2,12))
books.append(b1)
books.append(b2)

oldest = None
for book in books:
    print(book)
    if oldest:
        if book.get_days() > oldest.get_days():
            oldest = book
    else:
        oldest = book
print('The oldest book is "'+oldest.title+'".')
    