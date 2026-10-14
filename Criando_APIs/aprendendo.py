from flask import Flask, jsonify, request

app = Flask(__name__) # inicia o app em flask

livros = [
    {
        'id': 1,
        'titulo' : 'Harry Potter',
        'autor': 'J.K Rowling'
    },
    {
        'id': 2,
        'titulo' : 'Homem aranhas',
        'autor': 'Stan Lee'
    },
]

@app.route('/livros', methods=['GET']) #com METHODS a API somente irá funcionar com o comando especificado como GET
def obter_livros():
    return jsonify(livros)

@app.route('/livros/<int:id>', methods=['GET'])
def obter_livro_por_id(id):
    for livro in livros:
        if livro.get('id') == id:
            return jsonify(livro)

@app.route('/livros/<int:id>', methods=['PUT'])  
def editar_livro_por_id(id):
    livro_alterado = request.get_json()
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            livros[indice].update(livro_alterado)
            return jsonify(livros[indice])
        
@app.route('/livros', methods=['POST'])
def incluir_novo_livro():
    novo_livro = request.get_json()
    livros.append(novo_livro)

    return jsonify(livros)

@app.route('/livros/<int:id>', methods=['DELETE'])  
def excluir_livros(id):
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            del livros[indice]

    return jsonify(livros)

app.run(port=5000,host='localhost',debug=True) # define em qual port e localhost vai estar
