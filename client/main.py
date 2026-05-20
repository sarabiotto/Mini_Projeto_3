import os

import requests
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("BASE_URL")

print(BASE_URL)

def listar_livros():

    response = requests.get(f"{BASE_URL}/livros")

    if response.status_code == 200:

        print("\n📚 Lista de livros disponíveis:\n")

        for livro in response.json():

            print(
                f"{livro['titulo']} - "
                f"{livro['autor']} "
                f"({livro['ano']})"
            )

    else:
        print("Erro ao buscar livros")


def buscar_livro(titulo):

    response = requests.get(f"{BASE_URL}/livros/{titulo}")

    if response.status_code == 200:

        livro = response.json()

        print("\n🔎 Livro encontrado:\n")

        print(
            f"{livro['titulo']} - "
            f"{livro['autor']} "
            f"({livro['ano']})"
        )

    else:
        print("\n❌ Livro não encontrado")


if __name__ == "__main__":

    listar_livros()

    buscar_livro("Dom Casmurro")