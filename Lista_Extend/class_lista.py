# data: 20/09/2024
# Teste 1 = como funciona o extend
"""
lista = []

teste = "a",1

lista.extend(teste)

print(lista[0])
"""

from class_valor import Valor
from class_tela import Tela

# Teste 2 = agora com uma class
class ListaProdutos(Valor, Tela):

    lista = []

    def __init__(self) -> None:
        super().__init__()
        
    def add_produto(self):
        ListaProdutos.lista.append(self)

    def exibir_produtos(self):
        for lp in self.lista:
            print(f'_________{lp.nome}')
            print(f'_________{lp.idade}')

