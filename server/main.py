import csv
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Livro(BaseModel):
    titulo: str
    autor: str
    ano: int

def carregar_livros():
    livros = []
    with open("server/app/livros.csv", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            livros.append(row)
    return livros

@app.get("/livros")
def listar_livros():
    return carregar_livros()

@app.get("/livros/{titulo}")
def buscar_livro(titulo: str):
    for livro in carregar_livros():
        if livro["titulo"].lower() == titulo.lower():
            return livro
    return {"erro": "Livro não encontrado"}

@app.post("/livros")
def adicionar_livro(livro: Livro):
    with open("server/app/livros.csv", "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([livro.titulo, livro.autor, livro.ano])
    return {"mensagem": f"Livro '{livro.titulo}' adicionado com sucesso!"}
