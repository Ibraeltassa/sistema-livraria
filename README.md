# Sistema de Gerenciamento de Livraria

## Descrição
Sistema completo de gerenciamento de livraria que combina SQLite, manipulação de arquivos, CSV e geração de relatórios em PDF/HTML.
*lembre de baixar a extensão vscode-pdf

## Funcionalidades

### Operações CRUD
- ✅ Adicionar novo livro
- ✅ Exibir todos os livros cadastrados
- ✅ Atualizar preço de um livro
- ✅ Remover um livro
- ✅ Buscar livros por autor

### Manipulação de Arquivos
- ✅ Exportar dados para CSV
- ✅ Importar dados de CSV
- ✅ Backup automático do banco de dados
- ✅ Limpeza automática de backups antigos (mantém apenas os 5 mais recentes)

### Desafios Extras
- ✅ Validação completa de entradas (ano, preço, texto)
- ✅ Geração de relatórios em PDF
- ✅ Geração de relatórios em HTML

## Estrutura do Projeto
```
/livraria/
├── main.py              # Arquivo principal
├── database.py          # Operações do banco SQLite
├── menu.py              # Interface do usuário
├── file_manager.py      # Manipulação de arquivos e relatórios
├── utils.py             # Funções de validação
├── requirements.txt     # Dependências
├── README.md           # Este arquivo
├── /data/
│   └── livraria.db     # Banco de dados SQLite
├── /backups/           # Backups automáticos
└── /exports/           # Arquivos CSV e relatórios
```

## Instalação e Execução

1. Instale as dependências:
```bash
pip install -r requirements.txt
```

2. Execute o sistema:
```bash
python main.py
```

## Banco de Dados
O sistema utiliza SQLite com a seguinte estrutura:

**Tabela: livros**
- `id`: INTEGER PRIMARY KEY AUTOINCREMENT
- `titulo`: TEXT NOT NULL
- `autor`: TEXT NOT NULL
- `ano_publicacao`: INTEGER NOT NULL
- `preco`: REAL NOT NULL

## Validações Implementadas
- **Título/Autor**: Não podem estar vazios
- **Ano**: Deve ser um número entre 1000 e 2100
- **Preço**: Deve ser um número positivo

## Funcionalidades de Backup
- Backup automático antes de qualquer modificação (inserção, atualização, remoção)
- Manutenção automática de apenas 5 backups mais recentes
- Nomenclatura com timestamp: `backup_livraria_YYYY-MM-DD_HH-MM-SS.db`

## Relatórios
- **PDF**: Gerado com ReportLab, formatação profissional
- **HTML**: Tabela estruturada com bordas e formatação

## Menu do Sistema
1. Adicionar novo livro
2. Exibir todos os livros
3. Atualizar preço de um livro
4. Remover um livro
5. Buscar livros por autor
6. Exportar dados para CSV
7. Importar dados de CSV
8. Fazer backup do banco de dados
9. Sair
10. Gerar relatório em PDF
11. Gerar relatório em HTML
