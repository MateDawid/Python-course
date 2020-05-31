class Book:
    def __init__(self,title,author,price):
        self.title = title
        self.author = author
        self.price = price
    def __repr__(self):
        return self.title+', '+self.author+', '+self.price+' zł'
