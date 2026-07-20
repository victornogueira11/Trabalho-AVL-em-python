from livro import Livro
from avl import AVL

def testar_metricas():
    print("="*50)
    print(" TESTE: PERCURSO IN-ORDER E MÉTRICAS")
    print("="*50)

    arvore = AVL()
    # Inserindo códigos desordenados para testar o In-Order
    codigos = [50, 10, 40, 20, 30]
    for cod in codigos:
        arvore.insere(Livro(cod, f"Livro {cod}", "Autor", 2026))

    print("\n1. Percurso Em Ordem (Deve imprimir: 10, 20, 30, 40, 50)")
    arvore.exibir_em_ordem()

    print("\n2. Leitura de Métricas")
    print(f"-> Altura da Árvore: {arvore.altura_arvore()} (Esperado 2)")
    print(f"-> Total de Elementos: {arvore.totalNO()} (Esperado 5)")
    print(f"-> Rotações à Esquerda (RR): {arvore.rotacoes_esq}")
    print(f"-> Rotações à Direita (LL): {arvore.rotacoes_dir}")
    print("="*50)

if __name__ == "__main__":
    testar_metricas()