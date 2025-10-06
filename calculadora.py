from flask import Flask, jsonify, request

app = Flask(__name__)

# ---------- Rota principal ----------
@app.route('/')
def home():
    return jsonify({
        "mensagem": "Bem-vindo à API Calculadora!",
        "rotas_disponiveis": [
            "/soma?num1=10&num2=5",
            "/subtracao?num1=10&num2=5",
            "/multiplicacao?num1=10&num2=5",
            "/divisao?num1=10&num2=5"
        ]
    })

# ---------- Soma ----------
@app.route('/soma')
def soma():
    num1 = float(request.args.get('num1', 0))
    num2 = float(request.args.get('num2', 0))
    resultado = num1 + num2
    return jsonify({"operacao": "soma", "resultado": resultado})

# ---------- Subtração ----------
@app.route('/subtracao')
def subtracao():
    num1 = float(request.args.get('num1', 0))
    num2 = float(request.args.get('num2', 0))
    resultado = num1 - num2
    return jsonify({"operacao": "subtracao", "resultado": resultado})

# ---------- Multiplicação ----------
@app.route('/multiplicacao')
def multiplicacao():
    num1 = float(request.args.get('num1', 0))
    num2 = float(request.args.get('num2', 0))
    resultado = num1 * num2
    return jsonify({"operacao": "multiplicacao", "resultado": resultado})

# ---------- Divisão ----------
@app.route('/divisao')
def divisao():
    num1 = float(request.args.get('num1', 0))
    num2 = float(request.args.get('num2', 0))
    if num2 == 0:
        return jsonify({"erro": "Divisão por zero não é permitida!"}), 400
    resultado = num1 / num2
    return jsonify({"operacao": "divisao", "resultado": resultado})

# ---------- Rodar servidor ----------
if __name__ == '__main__':
    app.run(debug=True)
