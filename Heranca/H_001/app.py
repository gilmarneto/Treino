# importar class_pai
from class_filho import Filho
import os

os.system('cls')

# exemplo 1: neste caso tenho que passar 2 valores como parâmetro, caso eu não passe, será apresentado um erro:
# erro: Filho.__init__() missing 2 required positional arguments: 'n1' and 'n2'
"""
somar = Filho(2,8)
somar.soma()
"""
# exemplo 2:
# neste caso não preciso passar valor como parâmetro, pois na classe determinei os valores como 0
"""
somar = Filho()
somar.n1 = 8
somar.n2 = 90
somar.soma()
"""
# exemplo 3:
# vamos utilizar o **kwargs para adicionar mais atributos e valores
calculo = Filho()
calculo.n1 = 7
calculo.n2 = 2
calculo.soma()
# até aqui normal, abaixo vamos colocar mais 2 atributos, para vermos o funcionamento do **kwargs
calculo.kwargs['n3'] = 2
calculo.kwargs['n4'] = 3
calculo.multiplicacao()
