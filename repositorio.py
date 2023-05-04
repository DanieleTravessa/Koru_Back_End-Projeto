import sqlite3

#Essa rotina simula as funcionalidades de banco de dados para uso em um projeto de CRUD

#Conectar com o banco de dados
conexao = sqlite3.connect('korupet.db')


#Função que gera novo id
def gerar_id():
    conn = sqlite3.connect('korupet.db')
    cursor = conn.cursor()
    cursor.execute("SELECT seq FROM sqlite_sequence WHERE nome='produtos'")
    next_id = cursor.fetchone()[0]
    return next_id + 1
 #
 #Inserir dados no banco
 #ursor = conexao.cursor()
 #ql_insert = "INSERT INTO produtos (nome_produto, peso_produto, descricao_produto, preco_produto, fornecedor_produto) VALUES (?, ?, ?, ?, ?)"
 #
 #ursor.execute(sql_insert, (nome, peso, descricao, preco, fornecedor))
 #
 #roduto_id = cursor.lastrowid
 #onexao.commit()
 #rint(f"O último código inserido foi: {produto_id}")
 #
 #rint("Produto de código 2")
 #ursor = conexao.cursor()
 #ql_select_unico = "SELECT * FROM produtos WHER id_produto = ?"
 #ursor.execute(sql_select_unico, (2, ))
 #rint(cursor.fetchone())
 #
 
#Cria um novo produto no dicionário.
def criar_produto(nome, preco, peso, descricao, fornecedor):
    try:
        conn = sqlite3.connect("korupet.db")
        cursor = conn.cursor()
        sql_insert = "INSERT INTO produtos (nome_produto, preco_produto, peso_produto, descricao_produto, fornecedor_produto) VALUES (?, ?, ?, ?, ?)"
        cursor.execute(sql_insert, (nome, preco, peso, descricao, fornecedor))
        produto_id = cursor.lastrowid
        conn.commit()
        conn.close()
        return produto_id
    except Exception as ex:
        print(ex)
        return 0

#Retorna um dicionário com todos os produtos **
def retornar_produtos():
    try:
        resultado = []
        conn = sqlite3.connect("korupet.db")
        cursor = conn.cursor()
        sql_select = "SELECT * FROM produtos"
        cursor.execute(sql_select)
        produtos = cursor.fetchall()
        conn.close()
        for item in produtos:
            produto = {
                'id': item[0],
                'nome': item[1],
                'preco': item[2],
                'peso': item[3],
                'descricao': item[4],
                'fornecedor': item[5]
            }
            resultado.append(produto)
        return resultado
    except:
        return False    
        
#Retorna um único produto
def retornar_produto(id:int):
    try:
        if id == 0:            
            return gerar_id(), "", "", "", "", "", ""
        conn = sqlite3.connect("korupet.db")
        cursor = conn.cursor()
        
        sql_select = "SELECT * FROM produtos WHERE id_produto = ?"
        cursor.execute(sql_select, (id, ))
        id, nome, preco, peso, descricao, fornecedor = cursor.fetchone()
        conn.close()
        return {
            "id": id, 
            "nome": nome,              
            "preco": preco,
            "peso": peso, 
            "descricao": descricao,             
            "fornecedor": fornecedor
            }
    except:
        return False
    
    #Atualiza os dados de um produto
    def atualizar_produto(id:int, nome, preco, peso, descricao, fornecedor):
        try:
            #Tenta atualizar
            conn = sqlite3.connect("korupet.db")
            cursor = conn.cursor()
            sql_update = "UPDATE produtos SET nome_produto = ?, preco_produto = ?, peso_produto = ?, descricao_produto = ?, fornecedor_produto = ?"
            cursor.execute(sql_update, (nome, preco, peso, descricao, fornecedor, id))
            conn.commit()
            conn.close()
            return True
        except Exception as ex:
            print(ex)
            return False
        
        #Remove um produto
        def remover_produto(id:int):
            try:
                conn = sqlite3.connect("korupet.db")
                cursor = conn.cursor()
                sql_delete = "DELETE FROM personagens WHERE id_personagens = ?"
                cursor.execute(sql_delete, (id, ))
                conn.commit()
                conn.close()
                return True
            except Exception as ex:
                print(ex)
                return False
            
            
            '''
            #Area de testes
            
            nome = ""
            preco = 0
            peso = 0
            descricao = ""
            fornecedor = ""
            
            id = criar_produto(nome, preco, peso, descricao, fornecedor)
            print(id)
            print(retornar_produto(id))
            
            id, nome, preco, peso, descricao, fornecedor = retornar_produto(id)
            atualizar_produto(id, '', preco, peso, descricao, fornecedor)
            
            print(retornar_produto(id))
            id, nome, preco, peso, descricao, fornecedor = retornar_produto(id)
            
            print(retornar_produtos())
            
            remover_produto(id)
            
            print(retornar_produtos())
            '''