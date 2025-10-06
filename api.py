from flask import Flask, request

app = Flask(__name__)

@app.get("/ping")
def ping():
    # Retorna JSON a partir de um dict
    return {"mensagem": "pong"}  # Flask converte dict em JSON

@app.post("/soma")
def soma():
    # Lê JSON do corpo da requisição
    payload = request.get_json(silent=True) or {}
    a = payload.get("a", 0)
    b = payload.get("b", 0)
    return {"resultado": a + b}, 200  # Pode retornar (body, status)

if __name__ == "__main__":
    app.run(debug=True)

"------------------------------------------------"

import sqlite3

# Criando/conectando ao banco
con = sqlite3.connect("exemplo.db")
cur = con.cursor()

# Criando uma tabela
cur.execute("""
    CREATE TABLE IF NOT EXISTS pessoa (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        idade INTEGER NOT NULL
    );
""")

# Inserindo dados
cur.execute("INSERT INTO pessoa (nome, idade) VALUES (?, ?)", ("João", 30))
con.commit()

# Consultando dados
cur.execute("SELECT * FROM pessoa")
pessoas = cur.fetchall()
for pessoa in pessoas:
    print(pessoa)

# Fechando conexão

con.close()

