from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Bienvenue !</h1><p>Utilisez le chemin /hello/VOTRE_NOM dans l\'URL.</p>'

@app.route('/hello/<string:name>')
def hello(name):
    return f'<h1>Hello, {name}!</h1>'
