# data: 24/09/2024

from class_valor import Valor
from class_tela import Tela

class Lista(Valor, Tela):
    def __init__(self) -> None:
        super().__init__()
        self.lista = {}

    # MÉTODO ADICIONAR
    def adicionar(self):
        self.lista['letra'] = self.letra
        self.lista['numero'] = self.numero
        print(self.lista)