from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)
@app.route("/form")
def form():
    return render_template("form.html")

@app.route("/form2",methods=["POST"])
def form2():
    items = request.form.items()
    email = ''
    for argument,value in items:
        if argument == 'email':
            email = value
    return render_template('form2.html',email=email)


if __name__ == '__main__':
    app.run(debug=True)