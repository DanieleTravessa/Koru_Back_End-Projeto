#Criar uma API para um sistema de e.commerce
#A API deve trafegar dados 
#A API Deve

from flask import Flask, jsonify, request
import repositorio

app = Flask(__name__)

#Criar endpoints para listar um produto

@app.route("/produtos", methods=["GET"])
def get_produtos():
    produtos = repositorio.retornar_produtos()
    if produto:
        return jsonify(produto), 200
    else:
        return jsonify({"message":"Produto não encontrado"}), 404
    
    @app.route("/produto", methods=["POST"])
    def set_produto():
        produto = request.json
        id = repositorio.criar_produto(**produto)
        if id:
            produto["id"] = id
            return jsonify(produto), 201
        else:
            return jsonify({"message":"Não foi possível criar o produto"}), 500
        
    @app.route("/produto/<int:id>", methods=["PUT"])
    def update_produto(id):
        produto = repositorio.retornar_produto(id)
        if produto:
            dados_atualizados = request.json
            dados_atualizados["id"] = id
            if repositorio.atualizar_produto(**dados_atualizados):
                return jsonify(dados_atualizados), 200
            else:
                return jsonify({"message":"Produto não localizado"}), 404
            
    @app.route("/produto/<int:id>", methods=["DELETE"])
    def delete_produto(id):
        produto = repositorio
            
app.run(debug=True)