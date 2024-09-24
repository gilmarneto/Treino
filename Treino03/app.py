from flask import Flask, render_template, redirect, url_for
from class_tela import Tela

app = Flask(__name__)
# instância da classe Tela
tela = Tela()

# declarar as rotas
# rota principal do site
@app.route('/')
def index():
    #return render_template('index.html', btn_form="Adicionar", rota_form="alterar", input_produto="A", input_quantidade=1)
    return render_template('index.html', componentes=tela.exibir_componentes())
# rota responsável por alterar os valores dos componentes de tela
# teste_01: sem receber valores de um formulario
@app.route('/alterar_componentes')
def altera_componentes():
    tela.btn_form = 'Adicionar'
    tela.rota_form = 'alterar'
    tela. input_produto = 'A'
    tela.input_quantidade = 1
    return redirect(url_for('index'))
# rodar app
app.run(debug=True)