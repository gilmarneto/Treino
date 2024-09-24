# data: 24/09/2024
from flask import Flask, render_template, redirect, url_for
from class_lista import Lista

l = Lista()

app = Flask(__name__)
@app.route('/')
def index():
    l.adicionar()
    return render_template('index.html', titulo='Herança e Flask', componente=l.componentes_tela())

app.run(debug=True)


