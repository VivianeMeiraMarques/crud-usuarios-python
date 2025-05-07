users = []

def reset_users():
    users.clear()

def add_user(data):
    required_fields = ['name', 'email', 'password', 'cpf']
    if not all(field in data for field in required_fields):
        return {'error': 'Missing required fields'}, 400

    for u in users:
        if u['cpf'] == data['cpf']:
            return {'error': 'CPF already exists'}, 400

    users.append(data)
    return data, 201

def list_users():
    return users, 200

def search_user(cpf):
    for u in users:
        if u['cpf'] == cpf:
            return u, 200
    return {'error': 'User not found'}, 404

def delete_user(cpf):
    for u in users:
        if u['cpf'] == cpf:
            users.remove(u)
            return {'message': 'User successfully deleted'}, 200
    return {'error': 'User not found'}, 404
