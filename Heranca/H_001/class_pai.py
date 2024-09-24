# data: 19/09/2024

class Pai:
    # exemplo 1: neste caso é aguardado 2 valores de parâmetro
    """
    def __init__(self, n1, n2):
        self.n1 = n1
        self.n2 = n2
    """
    # exemplo 2: neste caso não é esperado valor de parâmetro ao instanciar uma classe
    def __init__(self, n1=0, n2=0):
        self.n1 = n1
        self.n2 = n2
    # exemplo 3: vamos aprender a usar o **kwargs, para mais argumentos
    def __init__(self, n1=0, n2=0, **kwargs):
        self.n1 = n1
        self.n2 = n2
        self.kwargs = kwargs
