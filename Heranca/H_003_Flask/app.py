# data: 24/09/2024
from flask import Flask, render_template, request, redirect, url_for
from class_lista import Lista 

l = Lista()

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html', titulo='Herança e Flask', componente=l.componentes_tela())

@app.route('/adicionar', methods=['POST',])
def adicionar_letra():
    letra = request.form['let']
    print(letra)
    return redirect(url_for('index'))

@app.route('/editar')
def editar():
    return redirect(url_for('index'))

app.run(host='0.0.0.0', port=8888, debug=True)


