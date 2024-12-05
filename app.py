import pickle
from flask import Flask, render_template, request, redirect
from calendar import isleap

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/leap", methods=['GET', 'POST'])
def leap():
    if request.method == "GET":
        return render_template("ar_keliamieji.html")
    if request.method == "POST":
        metai = int(request.form['metai'])
        ar_keliamieji = isleap(metai)
        return render_template("rezultatas.html", ar_keliamieji=ar_keliamieji, metai=metai)

@app.route("/biudzetas", methods=['GET', 'POST'])
def biudzetas():
    try:
        with open("zurnalas.pkl", "rb") as file:
            zurnalas = pickle.load(file)
    except FileNotFoundError:
        zurnalas = []
    if request.method == "GET":
        balansas = sum(zurnalas)
        return render_template('biudzetas.html', zurnalas=zurnalas, balansas=balansas)
    if request.method == "POST":
        suma = float(request.form['suma'])
        zurnalas.append(suma)
        with open("zurnalas.pkl", 'wb') as file:
            pickle.dump(zurnalas, file)
        return redirect("biudzetas")



if __name__ == "__main__":
    app.run(debug=True)