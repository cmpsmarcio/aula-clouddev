from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1>Olá FIAP!</h1>\n<strong>38SCJ</strong>MBA! o/"

