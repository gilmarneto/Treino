# data: 18/09/24

from class_lista import Lista
import os

os.system('cls')

def main():

    continuar = "s"

    while continuar == "s":
        produto = input('informe produto: ')
        qtde = input('informe quantidade: ')

        prod = Lista(produto, qtde)

        continuar = input('deseja continuar, s(sim) ou n(não)? ').lower()

    print('*'*50)
    
    prod.ver_lista()

if __name__ == "__main__":
    main()