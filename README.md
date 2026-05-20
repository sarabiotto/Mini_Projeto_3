````md
# Mini Projeto 3 - Consumo de APIs com Python

Projeto desenvolvido para a disciplina de Estrutura de Dados utilizando Python, FastAPI e Requests.

## 📚 Objetivo

Implementar um servidor de API REST e um cliente capaz de consumir os dados dessa API.

O sistema desenvolvido permite:

- Listar livros cadastrados
- Buscar livros por título
- Adicionar novos livros
- Consumir a API por meio de um cliente Python

# 👨‍💻 Integrantes

- Neia  
- Sara

# 🚀 Tecnologias Utilizadas

- Python 3
- FastAPI
- Uvicorn
- Requests
- Pydantic
- CSV

# 📁 Estrutura do Projeto

```txt
Mini_Projeto_3/
│
├── README.md
├── requirements.txt
├── .gitignore
│
├── server/
│   ├── .env.example
│   └── app/
│       ├── __init__.py
│       ├── main.py
│       └── livros.csv
│
├── client/
│   ├── .env
│   ├── .env.example
│   └── main.py
```

# ⚙️ Instalação

## Clone o repositório

```bash
git clone LINK_DO_REPOSITORIO
```

## Crie o ambiente virtual

```bash
python -m venv venv
```

## Ative o ambiente virtual

### Windows PowerShell

```powershell
.\venv\Scripts\Activate
```

## Instale as dependências

```bash
pip install -r requirements.txt
```

# ▶️ Executando o Servidor

Entre na pasta server:

```bash
cd server
```

Execute:

```bash
uvicorn app.main:app --reload
```

Servidor disponível em:

```txt
http://127.0.0.1:8000/
```

# 📖 Documentação Swagger

A documentação automática da API pode ser acessada em:

```txt
http://127.0.0.1:8000/docs
```

# 🖥️ Executando o Cliente

Abra outro terminal e execute:

```bash
cd client
python main.py
```

# 🔗 Endpoints da API

## Listar livros

```http
GET /livros
```

## Buscar livro por título

```http
GET /livros/{titulo}
```

## Adicionar livro

```http
POST /livros
```

Exemplo JSON:

```json
{
  "titulo": "Neuromancer",
  "autor": "William Gibson",
  "ano": 1984
}
```

# ✅ Funcionalidades Implementadas

- API REST com FastAPI
- Leitura de dados em CSV
- Busca dinâmica de livros
- Inserção de novos livros
- Cliente Python consumindo API
- Variáveis de ambiente com `.env`
- Documentação automática com Swagger

# 📌 Observações

O projeto utiliza armazenamento simples em arquivo CSV para fins acadêmicos e didáticos.
````
