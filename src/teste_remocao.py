from livro import Livro
from avl import AVL

def testar_remocao():
    print("="*50)
    print(" TESTE: REMOÇÃO (0, 1 e 2 FILHOS)")
    print("="*50)

    arvore = AVL()
    codigos = [30, 20, 40, 10, 25, 35, 50, 5]
    for cod in codigos:
        arvore.insere(Livro(cod, f"Livro {cod}", "Autor", 2026))

    print(f"Total de nós inicial: {arvore.totalNO()}")

    print("\n1. Removendo Nó Folha (Código 5)")
    arvore.remove(5)
    print(f"-> Total após remover (Esperado 7): {arvore.totalNO()}")

    print("\n2. Removendo Nó com 1 Filho (Código 10)")
    arvore.remove(10)
    print(f"-> Total após remover (Esperado 6): {arvore.totalNO()}")

    print("\n3. Removendo Nó com 2 Filhos (Código 30 - RAIZ)")
    arvore.remove(30)
    print(f"-> Total após remover (Esperado 5): {arvore.totalNO()}")
    
    print("\nValidação: Nova Raiz após remover o 30")
    # O menor da sub-árvore direita do 30 era o 35, ele deve ter subido.
    print(f"-> Nova Raiz (Esperado 35): {arvore.raiz.info.codigo}")
    print("="*50)

if __name__ == "__main__":
    testar_remocao()