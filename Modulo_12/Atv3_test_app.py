from flask import Flask, jsonify, request

app = Flask(_name_)

@app.get("/soma")
def soma():
    a = float(request.args.get("a"))
    b = float(request.args.get("b"))
    return jsonify({"resultado": a + b})

@app.get("/dividir")
def dividir():
    a = float(request.args.get("a"))
    b = float(request.args.get("b"))
    if b == 0:
        return jsonify({"erro": "Divisão por zero"}), 400
    return jsonify({"resultado": a / b})

if _name_ == "_main_":
    app.run()