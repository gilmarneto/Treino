# data: 24/09/24
""" Atenção: Dicionário no Python não aceita valores iguais """
# Ex: 01
d1 = {'a':1, 'b':2}
print(d1)
for md1 in d1:
    print(md1) 
# Ex: 02
d2 = {}
d2['a'] = 1
d2['b'] = 2
print(d2)
for md2 in d2:
    print(md2)
# Ex: 03
d3 = {}
d3['a'] = ''
d3['b'] = ''
print(d3)
d3['a'] = '11'
d3['b'] = '21'
print(d3)