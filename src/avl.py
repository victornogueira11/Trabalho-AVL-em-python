from no import No

class AVL:
    def __init__(self):
        self.raiz = None
        # Contadores de rotações
        self.rotacoes_esq = 0
        self.rotacoes_dir = 0
        
    def maior(self, x, y):
        if x > y:
            return x
        return y

    def alturaNO(self, no):
        if no == None:
            return -1
        else:
            return no.altura

    def fatorBalanceamento_NO(self, no):
        return abs(self.alturaNO(no.esq) - self.alturaNO(no.dir))
    
    def RotacaoLL(self, A):
        self.rotacoes_dir += 1  # Rotação LL é um giro para a direita
        B = A.esq
        A.esq = B.dir
        B.dir = A
        A.altura = self.maior(self.alturaNO(A.esq), self.alturaNO(A.dir)) + 1
        B.altura = self.maior(self.alturaNO(B.esq), A.altura) + 1
        return B

    def RotacaoRR(self, A):
        self.rotacoes_esq += 1  # Rotação RR é um giro para a esquerda
        B = A.dir
        A.dir = B.esq
        B.esq = A
        A.altura = self.maior(self.alturaNO(A.esq), self.alturaNO(A.dir)) + 1
        B.altura = self.maior(self.alturaNO(B.dir), A.altura) + 1
        return B

    def RotacaoLR(self, A):
        A.esq = self.RotacaoRR(A.esq)
        A = self.RotacaoLL(A)
        return A

    def RotacaoRL(self, A):
        A.dir = self.RotacaoLL(A.dir)
        A = self.RotacaoRR(A)
        return A

    # Inserção
    def insere(self, livro):
        if self.busca(livro.codigo):
            return False
        else:
            self.raiz = self._insereNO(self.raiz, livro)
            return True

    def _insereNO(self, atual, valor):
        if atual == None:
            novo = No(valor)
            return novo
        else:
            if valor.codigo < atual.info.codigo:
                atual.esq = self._insereNO(atual.esq, valor)
                if self.fatorBalanceamento_NO(atual) >= 2:
                    if valor.codigo < atual.esq.info.codigo:
                        atual = self.RotacaoLL(atual)
                    else:
                        atual = self.RotacaoLR(atual)
            else:
                if valor.codigo > atual.info.codigo:
                    atual.dir = self._insereNO(atual.dir, valor)
                    if self.fatorBalanceamento_NO(atual) >= 2:
                        if valor.codigo > atual.dir.info.codigo:
                            atual = self.RotacaoRR(atual)
                        else:
                            atual = self.RotacaoRL(atual)
            
            atual.altura = self.maior(self.alturaNO(atual.esq), self.alturaNO(atual.dir)) + 1
            return atual

    # Remoção
    def remove(self, codigo):
        if self.raiz == None or not self.busca(codigo):
            return False
        else:
            self.raiz = self._removeNO(self.raiz, codigo)
            return True

    def _removeNO(self, atual, valor):
        if atual.info.codigo == valor:
            # Nó com 1 ou 0 filhos
            if atual.esq == None or atual.dir == None:
                if atual.esq != None:
                    atual = atual.esq
                else:
                    atual = atual.dir
            # Nó com 2 filhos
            else:
                temp = self.procuraMenor(atual.dir)
                atual.info = temp.info
                atual.dir = self._removeNO(atual.dir, atual.info.codigo)
                if self.fatorBalanceamento_NO(atual) >= 2:
                    if self.alturaNO(atual.esq.dir) <= self.alturaNO(atual.esq.esq):
                        atual = self.RotacaoLL(atual)
                    else:
                        atual = self.RotacaoLR(atual)
        else:
            if valor < atual.info.codigo:
                atual.esq = self._removeNO(atual.esq, valor)
                if self.fatorBalanceamento_NO(atual) >= 2:
                    if self.alturaNO(atual.dir.esq) <= self.alturaNO(atual.dir.dir):
                        atual = self.RotacaoRR(atual)
                    else:
                        atual = self.RotacaoRL(atual)
            else:
                atual.dir = self._removeNO(atual.dir, valor)
                if self.fatorBalanceamento_NO(atual) >= 2:
                    if self.alturaNO(atual.esq.dir) <= self.alturaNO(atual.esq.esq):
                        atual = self.RotacaoLL(atual)
                    else:
                        atual = self.RotacaoLR(atual)

        if atual != None:
            atual.altura = self.maior(self.alturaNO(atual.esq), self.alturaNO(atual.dir)) + 1
            
        return atual

    def procuraMenor(self, atual):
        no1 = atual
        no2 = atual.esq
        while no2 != None:
            no1 = no2
            no2 = no2.esq
        return no1

    # Busca
    def busca(self, codigo):
        if self.raiz == None:
            return False
        atual = self.raiz
        while atual != None:
            if codigo == atual.info.codigo:
                return atual.info
            if codigo > atual.info.codigo:
                atual = atual.dir
            else:
                atual = atual.esq
        return False

    def buscar_intervalo(self, codigo_inicial, codigo_final):
        livros = []
        self._buscar_intervalo(self.raiz, codigo_inicial, codigo_final, livros)
        if not livros:
            print(f"Nenhum livro encontrado entre {codigo_inicial} e {codigo_final}.")
        else:
            for l in livros:
                print(l)

    def _buscar_intervalo(self, atual, inicio, fim, lista):
        if atual == None:
            return
        if inicio < atual.info.codigo:
            self._buscar_intervalo(atual.esq, inicio, fim, lista)
        if inicio <= atual.info.codigo <= fim:
            lista.append(atual.info)
        if fim > atual.info.codigo:
            self._buscar_intervalo(atual.dir, inicio, fim, lista)
 
    def exibir_em_ordem(self):
        if self.raiz != None:
            self._emOrdem(self.raiz)

    def _emOrdem(self, atual):
        if atual != None:
            self._emOrdem(atual.esq)
            print(atual.info)
            self._emOrdem(atual.dir)

    def totalNO(self):
        if self.raiz == None:
            return 0
        else:
            return self._totalNO(self.raiz)

    def _totalNO(self, atual):
        if atual == None:
            return 0
        total_esq = self._totalNO(atual.esq)
        total_dir = self._totalNO(atual.dir)
        return total_esq + total_dir + 1

    def altura_arvore(self):
        return self.alturaNO(self.raiz)