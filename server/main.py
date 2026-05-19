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

