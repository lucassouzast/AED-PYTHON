'''Aluno: Lucas Pereira de Souza'''


class No():

    def __init__(self, elemento):
        self.elemento = elemento
        self.esquerda = None
        self.direita = None
        self.altura = None
        self.pai = None


class ArvoreBinaria:

    def __init__(self):
        self.raiz = None
        self.tamanho = 0


    def inserir(self, elemento):
        no = No(elemento)
        # x = perc
        # z = no
        # p = pai
        # y = pai_atual
        pai_atual = None

        perc = self.raiz

        while perc is not None:
            pai_atual = perc
            if no.elemento < perc.elemento:
                perc = perc.esquerda
            else:
                perc = perc.direita

        no.pai = pai_atual

        if pai_atual == None:
            self.raiz = no #Arvore era vazia

        elif no.elemento < pai_atual.elemento:
            pai_atual.esquerda = no

        else:
            pai_atual.direita = no

        self.tamanho += 1
        self.balanceamento(no)


    def get_tamanho(self):
        return self.tamanho


    def minimo(self, perc=None):


        if perc is None:

            perc = self.raiz

        anterior = None
        while perc is not None:
            anterior = perc
            perc = perc.esquerda

        return anterior

    def _minimo(self):
        return print('O minimo da árvore é {}'.format(self.minimo().elemento))

    def maximo(self, perc=None):

        if perc is None:

            perc = self.raiz

        anterior = None
        while perc is not None:
            anterior = perc
            perc = perc.direita

        return anterior

    def _maximo(self):
        return print('O maximo da árvore é {}'.format(self.maximo().elemento))

    def remover(self, elemento):

        if self.raiz == None:
            return False
        perc = self.raiz
        pai = self.raiz
        filho_esquerda = True
        while perc.elemento != elemento:
            pai = perc
            if elemento < perc.elemento:
                perc = perc.esquerda
                filho_esquerda = True
            else:
                perc = perc.direita
                filho_esquerda = False
            if perc == None:
                return False

        if perc.esquerda == None and perc.direita == None:

            if perc == self.raiz:
                self.raiz = None
            else:
                if filho_esquerda:
                    pai.esquerda = None
                else:
                    pai.direita = None

        elif perc.direita == None:

            if perc == self.raiz:
                self.raiz = perc.esquerda
            else:
                if filho_esquerda:
                    pai.esquerda = perc.esquerda
                else:
                    pai.direita = perc.esquerda

        elif perc.esquerda == None:

            if perc == self.raiz:
                self.raiz = perc.direita
            else:
                if filho_esquerda:
                    pai.esquerda = perc.direita
                else:
                    pai.direita = perc.direita

        else:
            sucessor = self.sucessor(perc)
            if perc == self.raiz:
                self.raiz = sucessor
            else:
                if filho_esquerda:
                    pai.esquerda = sucessor
                else:
                    pai.direita = sucessor
            sucessor.esquerda = perc.esquerda

        self.tamanho -= 1
        self.balanceamento(elemento)
        return True

    def sucessor(self, elemento):
        elemento = self.buscar(elemento)

        if elemento.direita is not None:
            return self.minimo(elemento.direita)

        y = elemento.pai  # y é o pai atual

        while y is not None and elemento == y.direita:
            elemento = y
            y = y.pai

        return y

    def _sucessor(self, elemento):
        return print('O sucessor de {} na árvore é {}.'.format(elemento, self.sucessor(elemento).elemento))

    def antecessor(self, elemento):

        elemento = self.buscar(elemento)

        if elemento.esquerda is not None:
            return self.maximo(elemento.esquerda)

        y = elemento.pai #y é o pai atual

        while y is not None and elemento == y.esquerda:
            elemento = y
            y = y.pai

        return y

    def _antecessor(self, elemento):
        return print('O antecessor de {} na árvore é {}.'.format(elemento, self.antecessor(elemento).elemento))


    def niveis_arvore(self, elemento):

        if elemento == None or elemento.esquerda == None and elemento.direita == None:
            return 0
        else:
            if self.niveis_arvore(elemento.esquerda) > self.niveis_arvore(elemento.direita):
                return 1 + self.niveis_arvore(elemento.esquerda)
            else:
                return 1 + self.niveis_arvore(elemento.direita)

    def _niveis_arvore(self):
        return print('A árvore possui {} niveis.'.format(self.niveis_arvore(self.raiz)))


    def buscar(self, elemento):

        perc = self.raiz

        while perc is not None and elemento != perc.elemento:
            if elemento < perc.elemento:
                perc = perc.esquerda
            else:
                perc = perc.direita

        return perc

    def _buscar(self, elemento):
        return print('O elemento {} existe na árvore.'.format(self.buscar(elemento).elemento))

    def nivel_elemento(self, elemento):

        nvl_elemento = 0

        perc = self.raiz

        while perc is not None and elemento != perc.elemento:
            if elemento < perc.elemento:
                perc = perc.esquerda
                nvl_elemento += 1
            else:
                perc = perc.direita
                nvl_elemento += 1

        return nvl_elemento

    def _nivel_elemento(self,elemento):
        return print('O elemento {} existe e seu nivel é {}'.format(elemento, self.nivel_elemento(elemento)))



    def somatorio(self):

        lista = []
        soma = 0
        def elementos(no):
            if no != None:
                elementos(no.esquerda)
                lista.append(no.elemento)
                elementos(no.direita)

        elementos(self.raiz)
        for i in lista:
            soma += i
        return print('A soma de todos os elementos da árvore é de {}'.format(soma))


    def elementosno(self,no=None):

        quantidade = 0

        if no is None:
            elemento = self.raiz
            if elemento.esquerda is not None:
                quantidade += 1
            if elemento.direita is not None:
                quantidade += 1
        else:
            elemento = self.buscar(no)
            if elemento is None:
                print('Elemento não existe na árvore')
                exit()
            if elemento.esquerda is not None:
                quantidade += 1
            if elemento.direita is not None:
                quantidade += 1
        return print('O Nó {} possui {} filho(s)'.format(elemento.elemento,quantidade))

    def altura(self, no):
        if no is None:
            return -1
        else:
            return no.altura

    def nova_alt(self, no):
        no.altura = max(self.altura(no.esquerda), self.altura(no.direita)) + 1

    def rot_esquerda(self, sera_balanceado):
        sub_direita = sera_balanceado.direita
        sub_direita.pai = sera_balanceado.pai
        if sub_direita.pai is None:
            self.raiz = sub_direita
        else:
            if sub_direita.pai.esquerda is sera_balanceado:
                sub_direita.pai.esquerda = sub_direita
            elif sub_direita.pai.direita is sera_balanceado:
                sub_direita.pai.direita = sub_direita
        sera_balanceado.direita = sub_direita.esquerda
        if sera_balanceado.direita is not None:
            sera_balanceado.direita.pai = sera_balanceado
        sub_direita.esquerda = sera_balanceado
        sera_balanceado.pai = sub_direita
        self.nova_alt(sera_balanceado)
        self.nova_alt(sub_direita)

    def rot_direita(self, sera_balanceado):
        sub_esquerda = sera_balanceado.esquerda
        sub_esquerda.pai = sera_balanceado.pai
        if sub_esquerda.pai is None:
            self.raiz = sub_esquerda
        else:
            if sub_esquerda.pai.esquerda is sera_balanceado:
                sub_esquerda.pai.esquerda = sub_esquerda
            elif sub_esquerda.pai.direita is sera_balanceado:
                sub_esquerda.pai.direita = sub_esquerda
        sera_balanceado.esquerda = sub_esquerda.direita
        if sera_balanceado.esquerda is not None:
            sera_balanceado.esquerda.pai = sera_balanceado
        sub_esquerda.direita = sera_balanceado
        sera_balanceado.pai = sub_esquerda
        self.nova_alt(sera_balanceado)
        self.nova_alt(sub_esquerda)


    def balanceamento(self, no):
        while no is not None:
            self.nova_alt(no)
            if self.altura(no.esquerda) >= 2 + self.altura(no.direita):
                if self.altura(no.esquerda.direita) >= self.altura(no.esquerda.direita):
                    self.rot_esquerda(no)
                else:
                    self.rot_esquerda(no.esquerda)
                    self.rot_direita(no)
            elif self.altura(no.direita) >= 2 + self.altura(no.esquerda):
                if self.altura(no.direita.esquerda) >= self.altura(no.direita.esquerda):
                    self.rot_esquerda(no)
                else:
                    self.rot_direita(no.direita)
                    self.rot_esquerda(no)
            no = no.pai


    def elementosnivel(self, nivel):
        perc = self.raiz
        lista_nivel = []

        if nivel == 0:
            return perc.elemento
        else:
            lista = self.listar()

            for i in lista:
                if self.nivel_elemento(i) == nivel:
                    lista_nivel.append(i)

        return print('Os elementos do nivel {} são : {} '.format(nivel, lista_nivel))

    def listar(self):

        lista = []

        def listagem(atual):
            if atual is not None:
                listagem(atual.esquerda)
                lista.append(atual.elemento)
                listagem(atual.direita)

        listagem(self.raiz)

        return lista

    def _listar(self):
        return print(self.listar())