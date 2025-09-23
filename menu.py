from database import (
    adicionar_livro,
    listar_livros,
    atualizar_preco,
    remover_livro,
    buscar_por_autor
)
from file_manager import (
    fazer_backup,
    exportar_csv,
    importar_csv,
    gerar_relatorio_pdf,
    gerar_relatorio_html
)
from utils import validar_ano, validar_preco, validar_texto

def exibir_menu():
    print("\n=== Sistema de Gerenciamento de Livraria ===")
    print("1. Adicionar novo livro")
    print("2. Exibir todos os livros")
    print("3. Atualizar preço de um livro")
    print("4. Remover um livro")
    print("5. Buscar livros por autor")
    print("6. Exportar dados para CSV")
    print("7. Importar dados de CSV")
    print("8. Fazer backup do banco de dados")
    print("9. Sair")
    print("10. Gerar relatório em PDF")
    print("11. Gerar relatório em HTML")
    return input("Escolha uma opção: ")

def executar_opcao(opcao):
    if opcao == "1":
        titulo = None
        while titulo is None:
            titulo = validar_texto(input("Título: "), "Título")

        autor = None
        while autor is None:
            autor = validar_texto(input("Autor: "), "Autor")

        ano = None
        while ano is None:
            ano = validar_ano(input("Ano de publicação: "))

        preco = None
        while preco is None:
            preco = validar_preco(input("Preço: "))

        fazer_backup()
        adicionar_livro(titulo, autor, ano, preco)
        print("✅ Livro adicionado com sucesso!")

    elif opcao == "2":
        livros = listar_livros()
        if livros:
            for l in livros:
                print(f"ID: {l[0]} | {l[1]} - {l[2]} ({l[3]}) - R${l[4]:.2f}")
        else:
            print("Nenhum livro cadastrado.")

    elif opcao == "3":
        livro_id = input("ID do livro: ")
        preco = None
        while preco is None:
            preco = validar_preco(input("Novo preço: "))
        fazer_backup()
        atualizar_preco(livro_id, preco)
        print("✅ Preço atualizado.")

    elif opcao == "4":
        livro_id = input("ID do livro: ")
        fazer_backup()
        remover_livro(livro_id)
        print("✅ Livro removido.")

    elif opcao == "5":
        autor = input("Autor: ")
        livros = buscar_por_autor(autor)
        if livros:
            for l in livros:
                print(f"ID: {l[0]} | {l[1]} - {l[2]} ({l[3]}) - R${l[4]:.2f}")
        else:
            print("Nenhum livro encontrado.")

    elif opcao == "6":
        livros = listar_livros()
        if livros:
            exportar_csv(livros)
            print("✅ Dados exportados para exports/livros_exportados.csv")
        else:
            print("Nenhum livro para exportar.")

    elif opcao == "7":
        caminho = input("Digite o caminho do CSV: ")
        try:
            importar_csv(caminho, adicionar_livro)
            print("✅ Dados importados com sucesso.")
        except Exception as e:
            print(f"Erro ao importar CSV: {e}")

    elif opcao == "8":
        fazer_backup()
        print("✅ Backup realizado.")

    elif opcao == "9":
        print("Encerrando sistema...")
        return False

    elif opcao == "10":
        livros = listar_livros()
        if livros:
            gerar_relatorio_pdf(livros)
        else:
            print("Nenhum livro para gerar relatório.")

    elif opcao == "11":
        livros = listar_livros()
        if livros:
            gerar_relatorio_html(livros)
        else:
            print("Nenhum livro para gerar relatório.")

    else:
        print("❌ Opção inválida.")

    return True
