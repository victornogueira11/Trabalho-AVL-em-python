import random
from livro import Livro
from avl import AVL

def main():
    print("="*50)
    print(" SISTEMA DE GERENCIAMENTO DE LIVROS - ÁRVORE AVL")
    print("="*50)
    
    arvore = AVL()

    # Inserir pelo menos 100 livros com códigos gerados aleatoriamente
    print("\nInserido 100 livros aleatórios na árvore...")
    codigos_inseridos = []
    
    while len(codigos_inseridos) < 100:
        codigo = random.randint(1, 10000) # Códigos entre 1 e 10000
        
        # Evita a inserção de códigos duplicados
        if codigo not in codigos_inseridos:
            titulo = f"Livro_{codigo}"
            autor = "Autor Desconhecido"
            ano = random.randint(1950, 2026)
            
            novo_livro = Livro(codigo, titulo, autor, ano)
            if arvore.insere(novo_livro):
                codigos_inseridos.append(codigo)
                
    print(f"-> Sucesso! Total de livros na árvore: {arvore.totalNO()}")

    # Realizar pelo menos 20 buscas
    print("\nRealizado 20 buscas aleatórias...")
    # Escolhe 20 códigos aleatórios dos que acabámos de inserir
    codigos_para_buscar = random.sample(codigos_inseridos, 20)
    sucesso_buscas = 0
    
    for cod in codigos_para_buscar:
        if arvore.busca(cod):
            sucesso_buscas += 1
            
    print(f"-> Concluído! Foram encontrados {sucesso_buscas}/20 livros.")

    # Remover 20 livros
    print("\nRemovido 20 livros da árvore...")
    # Escolhe outros 20 códigos diferentes para remover
    codigos_para_remover = random.sample(codigos_inseridos, 20)
    sucesso_remocoes = 0
    
    for cod in codigos_para_remover:
        if arvore.remove(cod):
            sucesso_remocoes += 1
            # Remove da nossa lista de controlo também
            codigos_inseridos.remove(cod)
            
    print(f"-> Concluído! Foram removidos {sucesso_remocoes}/20 livros.")

    print("\n[Extra] A testar a busca por intervalo (Códigos entre 2000 e 2500):")
    arvore.buscar_intervalo(2000, 2500)

    # Apresentar métricas finais 
    print("\n" + "="*50)
    print(" RELATÓRIO FINAL DE EXECUÇÃO")
    print("="*50)
    print(f"Altura final da árvore:               {arvore.altura_arvore()}")
    print(f"Total de rotações à esquerda (RR):    {arvore.rotacoes_esq}")
    print(f"Total de rotações à direita (LL):     {arvore.rotacoes_dir}")
    print(f"Quantidade de elementos restantes:    {arvore.totalNO()}")
    print("="*50)

if __name__ == "__main__":
    main()