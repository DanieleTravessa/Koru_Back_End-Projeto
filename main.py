from flask import Flask, jsonify, request, redirect, url_for
import repositorio

app = Flask(__name__)

#Verificar o que a nossa função retornar_produtos() devolve e se são necessárias alterações

#ROTA para retornar todos os produtos
@app.route("/produtos", methods=["GET"])
def get_produtos():
    lista_produtos = repositorio.retornar_produtos()
    return jsonify(lista_produtos)


#ROTA para retornar um único produto
@app.route("/produto/<int:id>", methods=["GET"])
def get_produto(id):
    produto - repositorio.retornar_produto(id)
    
    if produto:
        return jsonify(produto)
    else:
        return jsonify({"message": "Produto não encontrado!"}), 404
    
#ROTA para cadastrar um produto
@app.route("/produto", methods=["POST"])
def criar_produto():
    produto = request.json
    id_produto = repositorio.criar_produto(**produto)
    produto["id"] = id_produto
    return jsonify(produto), 201
    

#ROTA para alterar um personagem
@app.route("/produto/<int:id>", methods=["PUT"])
def atualizar_produto(id):
    produto = repositorio.retornar_produto(id)
    if produto:
        dados_atualizados = request.json
        dados_atualizados["id"] = id
        repositorio.atualizar_produto(**dados_atualizados)
        return(jsonify(dados_atualizados))
    else:
        return jsonify({"message": "Personagem nao encontrado"}), 404

#ROTA para deletar um produto
@app.route("/produto/<int:id>", methods=["DELETE"])
def remover_prsonagem(id):
    produto = repositorio.retornar_produto(id)
    if produto:
        repositorio.remover_produto(id)
        return jsonify({"message":"Produto removido com sucesso!"})
    else:
        return jsonify({"message":"O Produto que você procura, não foi encontrado em nossos registros..."}), 404
        
app.run(debug=True)