import pytest

from main import somar_dois_numeros, calcular_area_do_circulo


def testar_somar_dois_numeros():
    # - 1° Etapa: Configura / Prepara
    # Dados / Valores
    # Entrada / Input
    num1 = 4
    num2 = 5
    # Saída / Output
    resultado_esperado = 9

    # 2° Etapa: Executa
    resultado_atual = somar_dois_numeros(num1,num2)

    # 3° Etapa: Confirma / Check / Valida
    assert resultado_atual == resultado_esperado

# anotação para utilizar como massa de testes
@pytest.mark.parametrize('raio, resultado_esperado',[
    #valores
                             (1,3.14),   #teste n° 1
                             (2,12.56),  #teste n° 2
                             (3,28.26),  #teste n° 3
                             (4,50.24),  #teste n° 4
                            ('a', 'Falha no calculo - Raio não é um número.')    #teste n° 5
                         ])

def testar_calcular_area_do_circulo(raio, resultado_esperado):
    # 1 - Configura / Comentado para que os parametros sejam lidos
    #raio = 1
    #resulta_esperado = 3.1415926539

    # 2- Executa
    resultado_atual = calcular_area_do_circulo(raio)

    # 3- Valida
    assert resultado_atual == resultado_esperado
