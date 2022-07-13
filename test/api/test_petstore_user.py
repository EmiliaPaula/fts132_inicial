# Bibliotecas
import time

import pytest  # Framework de Teste Unitário - Engine
import requests  # Framework de Testes de API - Request / Responses  (Requisiçoes / Respostas)

# Endereço da API
base_url = 'https://petstore.swagger.io/v2/user'
headers = {'Content-Type': 'application/json'}  # Nos .asmx seria 'text/xml    # Está dizendo qual o formato dos dados
token_usuario = ''

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

    print(f'Token: {token_usuario}')


def test_consultar_usuario_com_token(token_usuario):
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

    print(f'Token: {token_usuario}')

def test_alterar_usuario():
    # Configura
    username = 'Mihh'
    status_code_esperado = 200
    codigo_esperado = 200
    tipo_esperado = 'unknown'
    mensagem_esperada = '1001'

    # Executa
    resposta = requests.put(
        url=f'{base_url}/{username}',
        data=open('C:/Users/emili/PycharmProjects/fts132_inicial/test/db/user2.json', 'rb'),  # O Endpoint da API
        headers=headers
    )

    # Formatação
    corpo_da_resposta = resposta.json()
    print(resposta)
    print(resposta.status_code)
    print(corpo_da_resposta)

    # Validação
    assert resposta.status_code == status_code_esperado
    assert corpo_da_resposta['code'] == codigo_esperado
    assert corpo_da_resposta['type'] == tipo_esperado
    assert corpo_da_resposta['message'] == mensagem_esperada


def test_excluir_usuario():
    # Configura
    username = 'Mihh'
    status_code_esperado = 200
    codigo_esperado = 200
    tipo_esperado = 'unknown'
    mensagem_esperada = 'Mihh'

    # Executa
    resposta = requests.delete(
        url=f'{base_url}/{username}',
        headers=headers
    )

    # Formatação
    corpo_da_resposta = resposta.json()
    print(resposta)
    print(resposta.status_code)
    print(corpo_da_resposta)

    # Validação
    assert resposta.status_code == status_code_esperado
    assert corpo_da_resposta['code'] == codigo_esperado
    assert corpo_da_resposta['type'] == tipo_esperado
    assert corpo_da_resposta['message'] == mensagem_esperada


def test_login_do_usuario():
    # Configura
    username = 'Mihh'
    password = 'sucesso'
    status_code_esperado = 200
    codigo_esperado = 200
    tipo_esperado = 'unknown'
    inicio_mensagem_esperada = 'logged in user session:'


    # Executa
    resposta = requests.get(
        url=f'{base_url}/login?username={username}&password={password}',
        headers=headers
    )

    # Formata
    corpo_da_resposta = resposta.json()
    print(resposta)
    print(resposta.status_code)
    print(corpo_da_resposta)


    # Validação
    assert resposta.status_code == status_code_esperado
    assert corpo_da_resposta['code'] == codigo_esperado
    assert corpo_da_resposta['type'] == tipo_esperado
    assert corpo_da_resposta['message'].find(inicio_mensagem_esperada) != -1


    # Extrair
    # Na mensagem "logged in user session:1653022985573" queremos pegar os números
    mensagem_recebida = corpo_da_resposta['message']
    print(f'A mensagem recebida é: {mensagem_recebida}')
    token_usuario = mensagem_recebida[23:37]
    print(f'O token do usuario é: {token_usuario}')
    test_consultar_usuario_com_token(token_usuario)

    #Exemplo
    frase = 'Saldo: R$ 1.987,65'
    valor = frase[7:18]
    print(f'O valor é: {valor}')

#TODO: Controlar o tempo entre as requisições na sequenacia
'''
def testar_sequencia_de_testes():
    testar_criar_usuario()
    testar_login_do_usuario()
    test_alterar_usuario()
    testar_consultar_usuario()
    test_excluir_usuario()
'''
