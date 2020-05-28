from datetime import date
class Book:
    def __init__(self,title,author,pages,release_date):
        self.title = title
        self.author = author
        self.pages = pages
        self.release_date = release_date
    def get_days(self):
        return (date.today()-self.release_date).days

books = []
b1 = Book('Data science od podstaw. Analiza danych w Pythonie', "Stefan Siara Siarzewski", 1024, date(2019,3,21))
b2 = Book('HTML i CSS. Zaprojektuj i zbuduj witrynę WWW', "Wąski", 253, date(2017,5,21))
b3 = Book('MATEMATYKA ZADANIA MATRUALNE I EGZAMINACYJNE', "Ktoś stary", 932, date(1998,3,1))
books.append(b1)
books.append(b2)
books.append(b3)
number = 1
oldest = None
for i in books:
    print(str(number)+". Book",i.title,"is",i.get_days(),"days old.")
    number+=1
    if oldest:
        if i.get_days()>oldest.get_days():
            oldest = i
    else:
        oldest = i

print('The oldest book is "'+str(oldest.title)+".")


