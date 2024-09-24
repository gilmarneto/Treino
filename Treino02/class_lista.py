# data: 18/09/2024

from class_produto import Produto

class Lista(Produto):

    lista = []

    def __init__(self, produto, quantidade):
        super().__init__(produto, quantidade)    

    def adicionar(self):
        Lista.lista.append(self)

    def ver_lista(self):
        for l in self.lista:
            print(f'{l.produto} --- {l.quantidade}')
    