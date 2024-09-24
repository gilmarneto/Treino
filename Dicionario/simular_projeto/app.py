# data: 24/09/2024
from class_tela import Tela
import os

os.system('cls')

tela = Tela()

print('***** Exemplo_01 *****')
print(tela.show_components())

print('***** Exemplo_02 *****')
tela.rota_form = input('Rota: ').lower()
tela.btn_form = input('Btn: ').lower()
tela.input_valor = input('Valor input: ').lower()
print("*"*80)
print(tela.show_components())