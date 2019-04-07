class No:
    def __init__(self, elemento):
        self.elemento = elemento
        self.proximo = None


class Lista():
    def __init__(self):
        self.tamanho = 0
        self.inicio = None

    def __len__(self):
        return self.tamanho

    def add(self, elemento):
        no = No(elemento)
        if self.inicio is None:
            self.inicio = no
        else:
            perc = self.inicio
            while perc.proximo is not None:
                perc = perc.proximo
            perc.proximo = no
        self.tamanho += 1

    def addI(self, indice, elemento):
        pass


    def __str__(self):
        result = '['
        perc = self.inicio
        while perc.proximo is not None:
            result += perc.elemento + ','
            perc = perc.proximo
        result += perc.elemento + ']'
        return result

    def inserir(self, i, item):
        novo = self.no(item)
        if self.primeiro is None:
            self.primeiro = self.ultimo = novo
        elif i <= 0:
            novo.proximo = self.primeiro
            self.primeiro = novo
        elif i >= len(self):
            self.ultimo.proximo = novo
            self.ultimo = novo
        else:
            atual = self.primeiro
            indice_atual = 0
            while atual is not None:
                if indice_atual == i - 1:
                    novo.proximo = atual.proximo
                    atual.proximo = novo
                    break

                atual = atual.proximo
                indice_atual += 1

        self.__tamanho += 1
        self.__iterando = None