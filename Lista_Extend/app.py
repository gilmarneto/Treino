# data: 20/09/2024
from class_lista import ListaProdutos
import os

os.system('cls')

lp = ListaProdutos()
lp.nome = 'Gilmar'
lp.idade = 40

lp.add_produto()
lp.exibir_produtos()