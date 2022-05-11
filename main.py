import pytest

def somar_dois_numeros(num1, num2):
    return num1 + num2

def subtrair_dois_numeros(num1, num2):
    return num1 - num2

def multiplicar_dois_numeros(num1, num2):
    return num1 * num2

def dividir_dois_numeros(num1, num2):
    return num1 / num2

   # Calcular e testar a área de um circulo
    # Area = Pi * raio ** 2

def calcular_area_do_circulo(raio):
    return 3.1415926539 * raio ** 2

if __name__ == '__main__':
    soma = somar_dois_numeros(5,7)
    print(f'A soma é {soma}')

    subtrair = subtrair_dois_numeros(5,7)
    print(f'A subtração é {subtrair}')

    multiplicar = multiplicar_dois_numeros(5,7)
    print(f'A multiplicação é {multiplicar}')

    dividir = dividir_dois_numeros(5,7)
    print(f'A divisão é {dividir}')

def testar_somar_dois_numeros():
    # - 1° Etapa: Configura / Prepara
    # Dados / Valores
    # Entrada / Input
    num1 = 8
    num2 = 9
    # Saída / Output
    resultado_esperado = 17

    # 2° Etapa: Executa
    resultado_atual = somar_dois_numeros(num1,num2)

    # 3° Etapa: Confirma / Check / Valida
    assert resultado_atual == resultado_esperado


