from LISTAS.Simplismente_encadiada.Lista import Lista2

lista = Lista()
print(lista)
lista.add('10')
lista.add('20')
lista.add('30')
print(lista)
lista.addIndex(0, '11')
lista.addIndex(3, '50')
print(lista)

print(lista.getIndex(0))
obj = lista.getIndex(3)
print('----------')
print(lista[0])
print(lista[1])
print(lista[2])
print('----------')
print(lista)
lista[1] = 'heldon'
lista[0] = 'jose'
lista.__setitem__(4, 9)
print(lista)
#FAZ EM CASA
#lista[-1] = 'jose'
#print(lista)



#Exercício 01
  # - Colocar o fim na lista simplesmente Encadeada

#Exercício 02
  # - Faz a lista duplamente encadeada - usando o inicio e o fim da lista e colocando o anterior no novo Noli

