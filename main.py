from database import criar_tabela
from file_manager import inicializar_diretorios
from menu import exibir_menu, executar_opcao

def main():
    inicializar_diretorios()
    criar_tabela()

    rodando = True
    while rodando:
        opcao = exibir_menu()
        rodando = executar_opcao(opcao)

if __name__ == "__main__":
    main()
