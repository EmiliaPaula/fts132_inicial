#1 Importar Bibliotecas
import os
from datetime import datetime

import pytest
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

caminho_print = 'C:/Users/emili/PycharmProjects/fts132_inicial/prints/' \
                + datetime.now().strftime('%Y-%m-%d %H-%M-%S') + '/'


#2 Classes
class Test_Selenium_Webdriver:
    primeira_vez = "S"  # Controla se é a primeira execução: S ou outra: N

    #Definições de Início - Executar antes do teste
    def setup_method(self, method):
        #Declarar o objeto do Selenium e instanciar como o navegador desejado
        self.driver = webdriver.Chrome('C:/Users/emili/PycharmProjects/fts132_inicial/drivers/chrome/chromedriver.exe')
        self.driver.implicitly_wait(30)  # O Selenium irá esperar 30 segundos pelos elementos
        self.driver.maximize_window()    # Maximizar a janela do navegador

        #Cria a pasta caminho_print apenas antes do 1° teste
        try:
            os.mkdir(caminho_print)
        except:
            print('A pasta já existia')

    #Definição de Fim - Executa depois do teste
    def teardown_method(self):
        self.driver.quit()

    #Definição do Teste
    @pytest.mark.parametrize('id, termo, curso, preco', [
        ('1', 'mantis', 'Mantis', 'R$ 59,99'),
        ('2', 'ctfl', 'Preparatório CTFL', 'R$ 199,00'),
    ])
    def testar_comprar_curso_com_click_na_lupa(self, id, termo, curso, preco):

        # O Selenium abre a url indicada - site alvo do teste
        self.driver.get('https://www.iterasys.com.br')
        self.driver.get_screenshot_as_file(f'{caminho_print}teste {id} - passo 1 - home.png')
        #O Selenium clica na caixa de pesquisa
        self.driver.find_element(By.ID, 'searchtext').click()
        #O Selenium apaga o conteúdo da caixa de pesquisa
        self.driver.find_element(By.ID, 'searchtext').clear()
        # O Selenium escreve "mantis" na caixa de pesquisa
        self.driver.find_element(By.ID, 'searchtext').send_keys(termo)
        self.driver.get_screenshot_as_file(f'{caminho_print}teste {id} - passo 2 - pesquisa pelo curso.png')
        #O Selenium clica no botão de lupa
        self.driver.find_element(By.ID, 'btn_form_search').click()
        #O Selenium clica em 'Matricule-se'
        self.driver.find_element(By.CSS_SELECTOR, 'span.comprar').click()
        #O Selenium valida o nome do curso no carrinho de compras
        assert self.driver.find_element(By.CSS_SELECTOR, 'span.item-title').text == curso
        #O Selenium valida o preço do curso
        assert self.driver.find_element(By.CSS_SELECTOR, 'span.new-price').text == preco

    def testar_comprar_curso_mantis_com_enter(self, method):
        # O Selenium abre a url indicada - site alvo do teste
        self.driver.get('https://www.iterasys.com.br')
        #O Selenium clica na caixa de pesquisa
        self.driver.find_element(By.ID, 'searchtext').click()
        #O Selenium apaga o conteúdo da caixa de pesquisa
        self.driver.find_element(By.ID, 'searchtext').clear()
        # O Selenium escreve "mantis" na caixa de pesquisa
        self.driver.find_element(By.ID, 'searchtext').send_keys('mantis')
        #O Selenium pressiona a tecla Enter
        self.driver.find_element(By.ID, 'btn_form_search').send_keys(Keys.ENTER)
        #O Selenium clica em 'Matricule-se'
        self.driver.find_element(By.CSS_SELECTOR, 'span.comprar').click()
        #O Selenium valida o nome do curso no carrinho de compras
        assert self.driver.find_element(By.CSS_SELECTOR, 'span.item-title').text == 'Mantis'
        #O Selenium valida o preço do curso
        assert self.driver.find_element(By.CSS_SELECTOR, 'span.new-price').text == 'R$ 59,99'