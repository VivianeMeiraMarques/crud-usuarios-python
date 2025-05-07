import app.users as u

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
