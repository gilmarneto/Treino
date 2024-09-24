# data: 18/09/2024

from class_produto import Produto

class Lista(Produto):

    lista = []

    def __init__(self, produto, quantidade):
        super().__init__(produto, quantidade)
        Lista.lista.append(self)
    
    @classmethod
    def ver_lista(cls):
        for l in cls.lista:
            print(f'{l.produto} --- {l.quantidade}')
    