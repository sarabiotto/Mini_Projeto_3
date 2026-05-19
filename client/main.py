import requests

BASE_URL = "http://127.0.0.1:8000"

def listar_livros():
    response = requests.get(f"{BASE_URL}/livros")
    if response.status_code == 200:
        print("📚 Lista de livros disponíveis:")
        for livro in response.json():
            print("-", livro)
    else:
        print("Erro ao buscar livros:", response.status_code)

def buscar_livro(titulo):
    response = requests.get(f"{BASE_URL}/livros/{titulo}")
    if response.status_code == 200:
        print("🔎 Livro encontrado:", response.json())
    else:
        print("Livro não encontrado:", response.status_code)

if __name__ == "__main__":
    listar_livros()
    buscar_livro("Dom Casmurro")
