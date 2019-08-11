from ArvoreBinariaProjeto import ArvoreBinaria


arvere = ArvoreBinaria()

arvere.inserir(10)
arvere.inserir(20)
arvere.inserir(30)


arvere._niveis_arvore()

arvere._buscar(10)

arvere._maximo()
arvere._minimo()

arvere._sucessor(10)
arvere._antecessor(20)

arvere.elementosno(10) #total de elementos de um nó

arvere.nivel_elemento(5)
arvere._listar()
arvere.somatorio()

print(arvere.raiz.elemento)

arvere.elementosnivel(1)

#Eu tive algumas dificuldades mas ultilizei o livro cormem 3° edição que o monitor me recomendou, que me ajudou a entender muito bem sobre como fazer
#algumas funções logo depois de entender o conceito


#realizei algumas mudanças sobre algumas funções que eu coloquei na prova e as que coloquei aqui, pois não estavam retornando o elemento especifico e sim a memoria ou outros que retornavam NULO kkkk
# como por exemplo o MINIMO E O MAXIMO, que logo quando sai da sala foi que percebi que tinha esquecido de escrever "perc.esquerda" e acabei deixando só perc
#que no caso retornaria NULO quando saisse do WHILE e não o valor. :(

