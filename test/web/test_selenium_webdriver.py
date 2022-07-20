#1 Importar Bibliotecas
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

#2 Classes
class Test_selenium_webdriver:
    #Definições de Início - Executar antes do teste
    def setup_method(self, method):
        #Declarar o objeto do Selenium e instanciar como o navegador desejado
        self.driver = webdriver.Chrome('C:/Users/emili/PycharmProjects/fts132_inicial/drivers/chrome/chromedriver.exe')
        self.driver.implicitly_wait(30)  # O Selenium irá esperar 30 segundos pelos elementos
        self.driver.maximize_window()    # Maximizar a janela do navegador

    #Definição de Fim - Executa depois do teste
    def teardown_method(self):
        self.driver.quit()

    #Definição do Teste
    def testar_comprar_curso_mantis(self, method):
        # O Selenium abre a url indicada - site alvo do teste
        self.driver.get('https://www.iterasys.com.br')
        # O Selenium escreve "mantis" na caixa de pesquisa
        self.driver.find_element(By.ID, 'searchtext').send_keys('mantis')
        #O Selenium clica no botão de lupa
        self.driver.find_element(By.ID, 'btn_form_search').click()
        #O Selenium clica em 'Matricule-se'
        self.driver.find_element(By.CSS_SELECTOR, 'span.comprar').click()
        #O Selenium valida o nome do curso no carrinho de compras
        assert self.driver.find_element(By.CSS_SELECTOR, 'span.item-title').text == 'Mantis'
        #O Selenium valida o preço do curso
        assert self.driver.find_element(By.CSS_SELECTOR, 'span.new-price').text == 'R$ 59,99'
