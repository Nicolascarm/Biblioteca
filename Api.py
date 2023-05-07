#1. Objetivo - Criar um api que disponibiliza a consula, criação, edição e exclusão de livros.
#2. URL base - localhost
#3. Endpoints - 
 #- localhost/livros (GET)
 #- localhost/livros (POST)
 #- localhost/livros/id (GET)
 #- Localhost/livros/id (PUT)
 #- localhost/livros (DELETE)
#4. Quais recursos - Livros

from flask import Flask, jsonify, request

app = Flask(__name__)

vendas = [
	{
		"dia":1,
		"valor": 22174.1664
	},
	{
		"dia": 2,
		"valor": 24537.6698
	},
	{
		"dia": 3,
		"valor": 26139.6134
	},
	{
		"dia": 4,
		"valor": 0.0
	},
	{
		"dia": 5,
		"valor": 0.0
	},
	{
		"dia": 6,
		"valor": 26742.6612
	},
	{
		"dia": 7,
		"valor": 0.0
	},
	{
		"dia": 8,
		"valor": 42889.2258
	},
	{
		"dia": 9,
		"valor": 46251.174
	},
	{
		"dia": 10,
		"valor": 11191.4722
	},
	{
		"dia": 11,
		"valor": 0.0
	},
	{
		"dia": 12,
		"valor": 0.0
	},
	{
		"dia": 13,
		"valor": 3847.4823
	},
	{
		"dia": 14,
		"valor": 373.7838
	},
	{
		"dia": 15,
		"valor": 2659.7563
	},
	{
		"dia": 16,
		"valor": 48924.2448
	},
	{
		"dia": 17,
		"valor": 18419.2614
	},
	{
		"dia": 18,
		"valor": 0.0
	},
	{
		"dia": 19,
		"valor": 0.0
	},
	{
		"dia": 20,
		"valor": 35240.1826
	},
	{
		"dia": 21,
		"valor": 43829.1667
	},
	{
		"dia": 22,
		"valor": 18235.6852
	},
	{
		"dia": 23,
		"valor": 4355.0662
	},
	{
		"dia": 24,
		"valor": 13327.1025
	},
	{
		"dia": 25,
		"valor": 0.0
	},
	{
		"dia": 26,
		"valor": 0.0
	},
	{
		"dia": 27,
		"valor": 25681.8318
	},
	{
		"dia": 28,
		"valor": 1718.1221
	},
	{
		"dia": 29,
		"valor": 13220.495
	},
	{
		"dia": 30,
		"valor": 8414.61
	}
]

# Consultar(todos)
@app.route('/vendas', methods=['GET'])
def obter_livros():
    return jsonify(vendas)

# Consultar(id)
@app.route( '/vendas/<int:dia>' , methods = [ 'GET' ])
def  obter_livros_por_id (dia):
    for  venda  in  vendas :
        if  venda.get( "dia" ) ==  dia :
            return  jsonify ( venda )

# Editar livro
@app.route('/vendas/<int:dia>', methods=['PUT'])
def editar_livro(dia):
    venda_alterada = request.get_json()
    for indice,venda in enumerate(vendas):
        if venda.get('dia') == dia:
            vendas[indice].update(venda_alterada)
            return jsonify(vendas[indice])

# Adicionar nova venda
@app.route('/vendas',methods=['POST'])
def adicionar_nova_venda():
    nova_venda = request.get_json()
    vendas.append(nova_venda)
    return jsonify(vendas)

#Excluir venda
@app.route('/vendas/<int:dia>',methods=['DELETE'])
def excluir_venda(dia):
    for indice,venda in enumerate(vendas):
        if venda.get('dia') == dia:
            del vendas[indice]
            return jsonify(vendas)
       

app.run(port=5000, host='localhost', debug=True)