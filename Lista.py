#### LISTA EM PYTHON ### 

class Lista:
    def __init__(self):
        self.primeiro = None
        self.ultimo = None
        self.__tamanho = 0
        self.__iterando = None

    class no:
        def __init__(self, conteudo):
            self.conteudo = conteudo
            self.proximo = None

    def __len__(self):
        return self.__tamanho

    def __iter__(self):
        return self

    def __next__(self):
        if self.__iterando is None:
            self.__iterando = self.primeiro
        else:
            self.__iterando = self.__iterando.proximo

        if self.__iterando is not None:
            return self.__iterando.conteudo

        raise StopIteration

    def __getitem__(self, i):
        atual = self.primeiro
        indice_atual = 0
        while atual is not None:
            if indice_atual == i:
                return atual.conteudo

            indice_atual +=1
            atual = atual.proximo

        raise IndexError("list index out of range")
    def __setitem__(self, i, valor):
        atual = self.primeiro
        indice_atual = 0
        while atual is not None:
            if indice_atual == i:
                atual.conteudo = valor
                return
            indice_atual += 1
            atual = atual.proximo
        raise IndexError("list index out of range")

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        retorno = "<"
        for i, e in enumerate(self):
            retorno += e.__repr__()
            if i < len(self)-1:
                retorno += ", "

        retorno += ">"
        return retorno


    def __delitem__(self, i):
        if i < len(self):
            atual = self.primeiro
            if i == 0:
                self.primeiro = atual.proximo
                atual.proximo = None
                if i == len(self)-1:
                    self.ultimo = None
            else:
                anterior = None
                indice_atual = 0
                while atual is not None:
                    if indice_atual == i:
                        anterior.proximo = atual.proximo
                        atual.proximo = None

                        if i == len(self)-1:
                            self.ultimo = anterior
                    indice_atual +=1
                    anterior = atual
                    atual = atual.proximo

            self.__iterando = None
            self.__tamanho -= 1

        else:
            raise IndexError("list index out of renge")



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
                if indice_atual == i-1:
                    novo.proximo = atual.proximo
                    atual.proximo = novo
                    break

                atual = atual.proximo
                indice_atual += 1

        self.__tamanho +=1
        self.__iterando = None
