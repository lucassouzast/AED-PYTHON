class No:
    def __init__(self, elemento):
        self.elemento = elemento
        self.proximo = None
        self.anterior = None

    def __str__(self):
        return str(self.elemento)


class Lista:
    def __init__(self):
        self.__tamanho = 0
        self.inicio = None
        self.ultimo = None

    def __str__(self):

        valor = '['
        if self.inicio is not None:
            perc = self.inicio
            valor += str(perc.elemento)

            while perc.proximo is not None:
                perc = perc.proximo
                valor += ','
                valor += str(perc.elemento)

        valor += "]"

        return valor


    def __getitem__(self, item):
        return self.getIndex(item)

    def __setitem__(self, key, value):
        perc = self.inicio
        percf = self.ultimo
        if self.__tamanho == 0 or key == self.__tamanho:
            self.add(value)
        else:
            cont = 0
            while cont != key:
                perc = perc.proximo
                cont += 1
            perc.elemento = value

    def addIndex(self, i, novo_nó):
        nó = No(novo_nó)
        if i > self.__tamanho:
            self.add(nó)

        if i == 0:  # elemento adicionado no inicio da lista
            nó.proximo = self.inicio
            nó.proximo.anterior = nó
            self.inicio = nó

            self.__tamanho += 1

        elif i == self.__tamanho: #elemento adicionado no final da lista ou sendo o primeiro elemetnto
            self.add(nó)

        else: #adicionando no meio da lista

            nlista  = self.__tamanho // 2

            if i >= nlista:
                cont = self.__tamanho - 1
                perc = self.ultimo
                while cont != i:
                    perc = perc.anterior
                    cont -= 1
                nó.anterior = perc.anterior
                perc.anterior.proximo = nó
                perc.anterior = nó
                nó.proximo = perc

            elif i <= nlista:
                cont = 1
                perc = self.inicio
                while cont != i:
                    perc = perc.proximo
                    cont += 1
                nó.proximo = perc.proximo
                perc.proximo.anterior = nó
                nó.anterior = perc
                perc.proximo = nó

            self.__tamanho += 1


    def get_tamanho(self):
        return self.__tamanho

    def add(self, novo_nó):
        novo_nó = No(novo_nó)

        if self.inicio is None:
            self.inicio = novo_nó
            self.ultimo = novo_nó

            self.__tamanho += 1

        else:
            self.ultimo.proximo = novo_nó
            novo_nó.anterior = self.ultimo
            self.ultimo = novo_nó

            self.__tamanho += 1


    def getIndex(self, i):
        nlista = self.__tamanho // 2
        if self.__tamanho == 0:
            return 'Lista Vazia'

        if i >= nlista:
            cont = self.__tamanho
            perc = self.ultimo
            while cont != i:
                perc = perc.anterior
                cont -= 1
            return perc.elemento

        elif i <= nlista:
            cont = 1
            perc = self.inicio
            while cont != i:
                perc = perc.proximo
                cont += 1
            return perc.elemento


    def __delitem__(self, i):

        perc = self.inicio

        if self.__tamanho == 0:
            return 'Lista Vazia'

        elif self.__tamanho == 1:
            self.inicio = None
            self.ultimo = None
            return perc.elemento

        elif i == 0:
            self.inicio = perc.proximo
            perc.proximo.anterior = None
            perc.proximo = None
            return perc.elemento

        elif i == self.__tamanho - 1:
            perc = self.ultimo
            self.ultimo = perc.anterior
            perc.anterior.proximo = None
            perc.proximo = None
            return perc.elemento

        if i >= self.__tamanho:
            print('O Index informado não está nos limites da lista, será removido o ultimo elemento')
            perc = self.ultimo
            self.ultimo = perc.anterior
            perc.anterior.proximo = None
            perc.proximo = None
            return perc.elemento

        else:
            nlista = self.__tamanho // 2

            if i <= nlista:
                cont = 0
                perc = self.inicio
                while cont != i:
                    perc = perc.proximo
                    cont += 1
                perc.proximo.anterior = perc.anterior
                perc.anterior.proximo = perc.proximo
                return perc.elemento

            elif i >= nlista:
                cont = self.__tamanho -1
                perc = self.ultimo
                while cont != i:
                    perc = perc.anterior
                    cont -= 1
                perc.proximo.anterior = perc.anterior
                perc.anterior.proximo = perc.proximo
                return perc.elemento

lista = Lista()


lista.add(1)
lista.add(2)
lista.add(3)
lista.add(4)
lista.add(5)
lista.add(6)
lista.add(7)
lista.add(8)
print()
print('O tamanho da lista é {}'.format(lista.get_tamanho()))

print()
print(lista)
lista.__delitem__(8)
print()
print(lista)
