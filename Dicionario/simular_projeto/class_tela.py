# data: 24/09/2024

class Tela:
    def __init__(self):
        self.rota_form = 'adicionar'
        self.btn_form = 'Adicionar'
        self.input_valor = ''
    
    def show_components(self):
        self.componentes = {
            'rota_form' : self.rota_form,
            'btn_form' : self.btn_form,
            'input_valor' : self.input_valor
        }
        return self.componentes



