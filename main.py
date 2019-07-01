# import a todos los elementos necesarios para el juego
import random
from flask import Flask, render_template, request, make_response
#invocamos Flask
app = Flask(__name__)
# definimos una ruta de tipo POST para logear al usuario.
@app.route("/login", methods=["POST"])
def login():
    name = request.form.get("user-name")
    email = request.form.get("user-email")
    return render_template("login.html")

# definimos una ruta de tipo GET y definimos que compruebe si hay un secret number, si no lo hay crea una cookie con el
@app.route("/", methods=["GET"])
def index():
    secret_number = request.cookies.get("secret_number")

    response = make_response(render_template("index.html"))
    if not secret_number:
        new_secret = random.randint(1, 30)
        response.set_cookie("secret_number", str(new_secret))

    return response
# finalmente hace return con la respuesta

# En este cuadro, definimos una ruta de tipo POST en la que el programa comprueba si el numero del jugador es igual a la cookie
@app.route("/login", methods=["POST"])
def result():
    guess = int(request.form.get("guess"))
    secret_number = int(request.cookies.get("secret_number"))

    if guess == secret_number:
        message = "Correct! The secret number is {0}".format(str(secret_number))
        response = make_response(render_template("result.html", message=message))
        response.set_cookie("secret_number", str(random.randint(1, 30)))
        return response
    elif guess > secret_number:
        message = "Your guess is not correct... try something smaller."
        return render_template("result.html", message=message)
    elif guess < secret_number:
        message = "Your guess is not correct... try something bigger."
        return render_template("result.html", message=message)
# si la cookie es igual, se genera una nueva cookie y vuelve al inicio.

if __name__ == '__main__':
    app.run(debug=True)