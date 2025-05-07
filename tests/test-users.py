import app.users as u

def test_add_user():
    data = {'name': 'João', 'email': 'joao@example.com', 'password': '1234', 'cpf': '11122233344'}
    result, status = u.add_user(data)
    assert status == 201
    assert result['cpf'] == '11122233344'
    assert result['name'] == 'João'

def test_list_users():
    result, status = u.list_users()
    assert status == 200
    assert isinstance(result, list)
    assert len(result) >= 1


def setup_function():
    u.reset_users()
    u.add_user({'name': 'Maria', 'email': 'maria@example.com', 'password': 'abcd', 'cpf': '55566677788'})

def test_search_user_exist():
    cpf = '55566677788'
    result, status = u.search_user(cpf)
    assert status == 200
    assert result['cpf'] == cpf

def test_search_user_inexist():
    result, status = u.search_user('00000000000')
    assert status == 404
    assert result['error'] == 'User not found'

def test_delete_user_exist():
    cpf = '55566677788'
    result, status = u.delete_user(cpf)
    assert status == 200
    assert result['message'] == 'User successfully deleted'

def test_delete_user_inexist():
    result, status = u.delete_user('00000000000')
    assert status == 404
    assert result['error'] == 'User not found'
