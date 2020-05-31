#importowana klasa Flask
from flask import Flask
#importowana funkcja render_template
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    #wyświetla index.html z katalogu templates. Katalog musi być tak nazwany.
    #zmienna name z Pythona będzie widoczna w html
    return render_template('index.html',name='Python')

if __name__ == '__main__':
    app.run(debug=True)