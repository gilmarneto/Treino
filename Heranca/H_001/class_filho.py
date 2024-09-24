# data: 19/09/24
# vamos importar a classe Pai, para herdar seus atributos
from class_pai import Pai

class Filho(Pai):
    # não esquecer de passar como parêmetro os dados do Pai. Se no pai for n1=0, no filho também devemos colocar n1=0. No super não precisa. Veja o código:
    """
    def __init__(self, n1=0, n2=0):
        super().__init__(n1, n2)
    """
    # exemplo utilizando **kwargs
    def __init__(self, n1=0, n2=0, **kwargs):
        super().__init__(n1, n2, **kwargs)

    # Método de soma    
    def soma(self):
        resultado = self.n1 + self.n2
        print(resultado)
    # Método de multiplicação
    def multiplicacao(self):
        print(self.kwargs)
        resultado = self.kwargs['n3'] + self.kwargs['n4']
        print(type(resultado), " --- ", resultado)
