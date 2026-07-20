from livro import Livro
from avl import AVL

def testar_buscas():
    print("="*50)
    print(" TESTE: BUSCA EXATA E POR INTERVALO")
    print("="*50)

    arvore = AVL()
    # Inserindo códigos: 10, 20, 30, 40, 50
    for i in range(10, 60, 10):
        arvore.insere(Livro(i, f"Livro {i}", "Autor", 2026))

    print("\n1. Busca Exata (Código Existente: 30)")
    livro_encontrado = arvore.busca(30)
    print(f"-> Resultado: {livro_encontrado}")

    print("\n2. Busca Exata (Código Inexistente: 99)")
    livro_nao_encontrado = arvore.busca(99)
    print(f"-> Resultado (Esperado False): {livro_nao_encontrado}")

    print("\n3. Busca por Intervalo (Entre 15 e 45)")
    print("-> Esperado: Livros 20, 30 e 40")
    arvore.buscar_intervalo(15, 45)
    print("="*50)

if __name__ == "__main__":
    testar_buscas()