import sqlite3
from pathlib import Path

DB_PATH = Path("data/livraria.db")

def conectar():
    return sqlite3.connect(DB_PATH)

def criar_tabela():
    with conectar() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS livros (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                titulo TEXT NOT NULL,
                autor TEXT NOT NULL,
                ano_publicacao INTEGER NOT NULL,
                preco REAL NOT NULL
            )
        """)
        conn.commit()

def adicionar_livro(titulo, autor, ano_publicacao, preco):
    with conectar() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO livros (titulo, autor, ano_publicacao, preco)
            VALUES (?, ?, ?, ?)
        """, (titulo, autor, ano_publicacao, preco))
        conn.commit()

def listar_livros():
    with conectar() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM livros")
        return cursor.fetchall()

def atualizar_preco(livro_id, novo_preco):
    with conectar() as conn:
        cursor = conn.cursor()
        cursor.execute("UPDATE livros SET preco = ? WHERE id = ?", (novo_preco, livro_id))
        conn.commit()

def remover_livro(livro_id):
    with conectar() as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM livros WHERE id = ?", (livro_id,))
        conn.commit()

def buscar_por_autor(autor):
    with conectar() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM livros WHERE autor LIKE ?", (f"%{autor}%",))
        return cursor.fetchall()
