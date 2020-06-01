from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)
@app.route("/car")
def car():
    return render_template('car.html')

@app.route("/cars")
def cars():
    brand = request.args.get("brand")
    colour = request.args.get("colour")
    return render_template("cars.html",brand = brand, colour = colour)

if __name__ == '__main__':
    app.run(debug=True)