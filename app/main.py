from flask import Flask, request, jsonify
from app.users import add_user, list_user, search_user, delete_user

app = Flask(__name__)

users = []

@app.route('/users', methods=['POST'])
def criar_user():
    data = request.get_json()
    response, status = add_user(data)
    return jsonify(response), status

@app.route('/users', methods=['GET'])
def listar_user():
    response, status = list_user()
    return jsonify(response), status

@app.route('/users/<cpf>', methods=['GET'])
def buscar_user(cpf):
    response, status = search_user(cpf)
    return jsonify(response), status

@app.route('/users/<cpf>', methods=['DELETE'])
def delete_user(cpf):
    response, status = delete_user(cpf)
    return jsonify(response), status
    
if __name__ == '__main__':
    app.run(debug=True)