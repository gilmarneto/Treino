# data: 24/09/2024

class Dic_02:
    def __init__(self):
        self.letra = 'A'
        self.numero = 1
        self.d = {}

    def insert_dic(self):
        self.d[self.letra] = self.numero
    
    def show_dic(self):
        return self.d
