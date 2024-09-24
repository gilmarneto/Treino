"""
Data: 19/09/2024
Na classe de tela, eu vou atribuir valores aos botes, form(action) e campos de input.
"""

class Tela:
    def __init__(self):
        self.btn_form = ""
        self.rota_form = ""
        self.input_produto = ""
        self.input_quantidade = ""

    def exibir_componentes(self):
        # teste-1: sem dicionário
        print(f'teste saída_01: {self.btn_form}, {self.rota_form}, {self.input_produto}, {self.input_quantidade}')
        # teste-2: com dicionário
        # dicionário de componentes
        # adicionando chaves e valores ao dicionário
        dic_componentes = {
            'btn_form':self.btn_form,
            'rota_form':self.rota_form,
            'input_produto':self.input_produto,
            'input_quantidade':self.input_quantidade
        }
        # exibindo dicionário
        print(f'teste saída_02: {dic_componentes}')
        # retornar valor para o render_template
        return dic_componentes
