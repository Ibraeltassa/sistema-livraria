import shutil
import os
from datetime import datetime
from pathlib import Path
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

DB_PATH = Path("data/livraria.db")
BACKUP_DIR = Path("backups")
EXPORTS_DIR = Path("exports")

def inicializar_diretorios():
    for d in [DB_PATH.parent, BACKUP_DIR, EXPORTS_DIR]:
        d.mkdir(parents=True, exist_ok=True)

def fazer_backup():
    if DB_PATH.exists():
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        backup_file = BACKUP_DIR / f"backup_livraria_{timestamp}.db"
        shutil.copy(DB_PATH, backup_file)
        limpar_backups_antigos()

def limpar_backups_antigos(max_backups=5):
    backups = sorted(BACKUP_DIR.glob("backup_livraria_*.db"), key=os.path.getmtime, reverse=True)
    for old_backup in backups[max_backups:]:
        old_backup.unlink()

def exportar_csv(dados):
    arquivo_csv = EXPORTS_DIR / "livros_exportados.csv"
    with open(arquivo_csv, "w", encoding="utf-8") as f:
        f.write("id,titulo,autor,ano_publicacao,preco\n")
        for livro in dados:
            linha = f"{livro[0]},{livro[1]},{livro[2]},{livro[3]},{livro[4]}\n"
            f.write(linha)

def importar_csv(caminho_csv, func_inserir):
    with open(caminho_csv, "r", encoding="utf-8") as f:
        next(f)  # pula cabeçalho
        for linha in f:
            id, titulo, autor, ano, preco = linha.strip().split(",")
            func_inserir(titulo, autor, int(ano), float(preco))

def gerar_relatorio_pdf(dados):
    arquivo_pdf = EXPORTS_DIR / "relatorio_livros.pdf"
    c = canvas.Canvas(str(arquivo_pdf), pagesize=letter)
    c.setFont("Helvetica", 12)

    c.drawString(100, 750, "Relatório de Livros - Livraria")
    y = 720
    for livro in dados:
        linha = f"ID: {livro[0]} | {livro[1]} - {livro[2]} ({livro[3]}) - R${livro[4]:.2f}"
        c.drawString(50, y, linha)
        y -= 20
        if y < 50:  # nova página
            c.showPage()
            c.setFont("Helvetica", 12)
            y = 750

    c.save()
    print(f"✅ Relatório PDF gerado em: {arquivo_pdf}")

def gerar_relatorio_html(dados):
    arquivo_html = EXPORTS_DIR / "relatorio_livros.html"
    with open(arquivo_html, "w", encoding="utf-8") as f:
        f.write("<html><head><title>Relatório Livros</title></head><body>")
        f.write("<h1>Relatório de Livros - Livraria</h1>")
        f.write("<table border='1' cellpadding='5'><tr><th>ID</th><th>Título</th><th>Autor</th><th>Ano</th><th>Preço</th></tr>")
        for livro in dados:
            f.write(f"<tr><td>{livro[0]}</td><td>{livro[1]}</td><td>{livro[2]}</td><td>{livro[3]}</td><td>{livro[4]:.2f}</td></tr>")
        f.write("</table></body></html>")
    print(f"✅ Relatório HTML gerado em: {arquivo_html}")
