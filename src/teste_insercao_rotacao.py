from livro import Livro
from avl import AVL

def testar_insercao_rotacoes():
    print("="*50)
    print(" TESTE: INSERÇÃO E ROTAÇÕES (LL, RR, LR, RL)")
    print("="*50)

    print("\n1. Forçando Rotação RR (Árvore pesa para a direita)")
    avl_rr = AVL()
    avl_rr.insere(Livro(10, "Livro A", "Autor", 2026))
    avl_rr.insere(Livro(20, "Livro B", "Autor", 2026))
    avl_rr.insere(Livro(30, "Livro C", "Autor", 2026))
    print(f"-> Esperado: Raiz 20 | Obtido: Raiz {avl_rr.raiz.info.codigo}")

    print("\n2. Forçando Rotação LL (Árvore pesa para a esquerda)")
    avl_ll = AVL()
    avl_ll.insere(Livro(30, "Livro A", "Autor", 2026))
    avl_ll.insere(Livro(20, "Livro B", "Autor", 2026))
    avl_ll.insere(Livro(10, "Livro C", "Autor", 2026))
    print(f"-> Esperado: Raiz 20 | Obtido: Raiz {avl_ll.raiz.info.codigo}")

    print("\n3. Forçando Rotação LR (Esquerda-Direita)")
    avl_lr = AVL()
    avl_lr.insere(Livro(30, "Livro A", "Autor", 2026))
    avl_lr.insere(Livro(10, "Livro B", "Autor", 2026))
    avl_lr.insere(Livro(20, "Livro C", "Autor", 2026))
    print(f"-> Esperado: Raiz 20 | Obtido: Raiz {avl_lr.raiz.info.codigo}")

    print("\n4. Forçando Rotação RL (Direita-Esquerda)")
    avl_rl = AVL()
    avl_rl.insere(Livro(10, "Livro A", "Autor", 2026))
    avl_rl.insere(Livro(30, "Livro B", "Autor", 2026))
    avl_rl.insere(Livro(20, "Livro C", "Autor", 2026))
    print(f"-> Esperado: Raiz 20 | Obtido: Raiz {avl_rl.raiz.info.codigo}")
    print("="*50)

if __name__ == "__main__":
    testar_insercao_rotacoes()