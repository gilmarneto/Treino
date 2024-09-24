# data: 24/09/2024

class Tela():
    rota = 'adicionar'
    btn = 'Adicionar'

    def componentes_tela(self):
        self.componentes = {}
        self.componentes['rota'] = self.rota
        self.componentes['btn'] = self.btn
        print(self.componentes)
        return self.componentes