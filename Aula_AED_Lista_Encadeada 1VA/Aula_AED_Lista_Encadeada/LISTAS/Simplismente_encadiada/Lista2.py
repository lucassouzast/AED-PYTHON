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
        percf = self.fim
        if self.__tamanho == 0 or key == self.__tamanho:
            self.add(value)
        else:
            cont = 0
            while cont != key:
                perc = perc.proximo
                cont += 1
            perc.elemento = value

    def addIndex(self, i, elemento):

        if i > self.__tamanho:
            raise TypeError("Posição de memoria inválida")

        if i == self.__tamanho:
            self.add(elemento)
        elif i == 0:
            # ------- cria a caixinha ------
            no = No(elemento)
            # ------- vai receber inicio ---
            perc = self.inicio
            self.inicio = no
            no.proximo = perc

            self.__tamanho += 1
        else:
            # cria a caxinha
            no = No(elemento)
            # cria um contador para ir percorrendo, sabemdo que a posição e I-1
            cont = 0
            perc = self.inicio
            while cont < i - 1:
                perc = perc.proximo
                cont += 1
                # quandoa achar o local inverte as posiçoes
            no.proximo = perc.proximo
            perc.proximo = no

            self.__tamanho += 1

    def get_tamanho(self):
        return self.__tamanho

    def add(self, novo_elemento):
        no = No(novo_elemento)
        if self.inicio is None:
            self.inicio = no
        else:
            perc = self.inicio

            while perc.proximo is not None:
                perc = perc.proximo

            perc.proximo = no
        self.__tamanho += 1

    def getIndex(self, i):
        perc = self.inicio
        if self.__tamanho == 0:
            return '[]'
        cont = 0
        while cont != i:
            perc = perc.proximo
            cont += 1
        return perc


class NoAnt():
    def __init__(self, elemento):
        pass


class ListaDuplamente():
    pass


lista = Lista()
lista.add(1)
lista.add(2)
lista.add(3)
print(len(lista))
