from LISTAS.Simplismente_encadiada.lista2 import Lista

lista = Lista()
lista.inserir(1, 'heldon')

lista.inserir(2,'MARCOS')

print(len(lista))
print(lista)

lista.inserir(3, 'joao')
print(lista)


lista.inserir(1, 'pedro')
print(lista)

lista.__delitem__(2)
print(lista)
