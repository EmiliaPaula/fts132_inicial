# Bibliotecas
import pytest  # Framework de Teste Unitário - Engine
import requests  # Framework de Testes de API - Request / Responses  (Requisiçoes / Respostas)

# Endereço da API
base_url = 'https://petstore.swagger.io/v2/user'
headers = {'Content-Type': 'application/json'}  # Nos .asmx seria 'text/xml    # Está dizendo qual o formato dos dados


# 0 teste
def test_criar_usuario():
    # Configura
    status_code_esperado = 200
    codigo_esperado = 200
    tipo_esperado = 'unknown'
    mensagem_esperada = '1001'

    # Executa
    resposta = requests.post(
        url=base_url,  # Faz a requisição
        data=open('C:/Users/emili/PycharmProjects/fts132_inicial/test/db/user1.json', 'rb'),  # O Endpoint da API
        headers=headers  # O header com Content-Type
    )

    # Formatação
    corpo_da_resposta = resposta.json()  # Formata como JSON
    print(resposta)  # Resposta Bruta         - Opcional
    print(resposta.status_code)  # Status Code            - Opcional
    print(corpo_da_resposta)  # Resposta Formatada     - Opcional

    # Valida
    assert resposta.status_code == status_code_esperado
    assert corpo_da_resposta['code'] == codigo_esperado
    assert corpo_da_resposta['type'] == tipo_esperado
    assert corpo_da_resposta['message'] == mensagem_esperada

def test_consultar_usuario():
    # Configura
    status_code = 200
    id = 1001
    username = 'Mihh'
    firstName = 'Emília'
    lastName = 'Paula'
    email = 'emiliaand_paula1@teste.com'
    password = '1234567'
    phone = '11999998888'
    userStatus = 0

    # Executa
    resposta = requests.get(
        url=f'{base_url}/{username}',
        headers=headers
    )
    # Formata
    corpo_da_resposta = resposta.json()  # Formata como JSON
    print(resposta)  # Resposta Bruta         - Opcional
    print(resposta.status_code)  # Status Code            - Opcional
    print(corpo_da_resposta)

    # Valida
    assert resposta.status_code == status_code
    assert corpo_da_resposta['id'] == id
    assert corpo_da_resposta['username'] == username
    assert corpo_da_resposta['email'] == email
    assert corpo_da_resposta['phone'] == phone
    assert corpo_da_resposta['password'] == password
