from flask import Flask
from flask import render_template
from classBook import Book
app = Flask(__name__)

books = []
books.append(Book("Narrenturm","Andrzej Sapkowski",59.99))
books.append(Book("Boży bojownicy","Andrzej Sapkowski",59.99))
books.append(Book("Lux Perpetua","Andrzej Sapkowski",59.99))
books.append(Book("Futu.re","Dmitry Glukhovsky",39.99))
books.append(Book("Gra o tron","George R.R. Martin",49.99))
books.append(Book("Krótka historia czasu","Stephen Hawking",29.99))

@app.route('/')
def book_list():
    return render_template('books.html',books=books)

if __name__ == '__main__':
    app.run(debug=True)