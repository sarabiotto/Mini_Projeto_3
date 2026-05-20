import csv
from fastapi import FastAPI
from pydantic import BaseModel
import os

app = FastAPI()

class Livro(BaseModel):
    titulo: str
    autor: str
    ano: int

CSV_PATH = os.path.join(os.path.dirname(__file__), "livros.csv")

def carregar_livros():
    livros = []

    if not os.path.exists(CSV_PATH):
        return livros

    with open(CSV_PATH, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)

        for row in reader:
            livros.append(row)

    return livros

@app.get("/")
def home():
    return {"mensagem": "API de Livros funcionando!"}

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

    file_exists = os.path.exists(CSV_PATH)

    with open(CSV_PATH, "a", newline="", encoding="utf-8") as f:

        writer = csv.writer(f)

        if not file_exists:
            writer.writerow(["titulo", "autor", "ano"])

        writer.writerow([
            livro.titulo,
            livro.autor,
            livro.ano
        ])

    return {
        "mensagem": f"Livro '{livro.titulo}' adicionado com sucesso!"
    }