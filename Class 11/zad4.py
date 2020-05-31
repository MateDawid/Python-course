from flask import Flask

app = Flask(__name__)
#dla ścieżki głównej wykonaj funkcję:
@app.route("/")
def index():
    return "Hello world"
if __name__=='__main__':
    app.run(debug=True)

#po wpisaniu w przeglądarkę "localhost:5000" pojawia się output programu
#ctrl+c żeby zamknąć serwer