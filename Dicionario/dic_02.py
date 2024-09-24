# data: 24/09/2024

from class_dic_02 import Dic_02

d = Dic_02()
d.letra = 'AA'
d.numero = 101
d.insert_dic()
d.letra = 'BB'
d.numero = 202
d.insert_dic()

d.letra = 'BB'
d.numero = 222
d.insert_dic()
        

print(d.show_dic())

