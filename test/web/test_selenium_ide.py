# 1 - Importar Bibliotecas / Pacotes

import pytest      #Framework de Teste de Unidade / Engine / Motor
import time        #Controle do Tempo
import json        # Ler e escrever no formato Json
from selenium import webdriver      #Bibliotecas do Selenium WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

# 2 - Classes e Dfinições (lembrando que nem sempre se usa classes)
class TestConsultarMantis():
    def setup_method(self, method):
        #Instanciar o objeto do Selenium Webdriver como Chrome
        self.drivers = webdriver.Chrome('C:/Users/emili/PycharmProjects/fts132_inicial/drivers/chrome/chromedriver.exe')
        browser = webdriver.Chrome()
        self.drivers.implicitly_wait(30)   #O robô irá esperar por 30 segundos pelo elemento
        self.drivers.maximize_window()   #Maximizar a janela do navegador
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_consultarMantis(self):
        self.driver.get("https://iterasys.com.br/plataforma/home/index.php?action=initial")
        self.driver.set_window_size(1280, 680)
        self.driver.find_element(By.ID, "searchtext").click()
        self.driver.find_element(By.ID, "searchtext").send_keys("mantis")
        self.driver.find_element(By.ID, "btn_form_search").click()
        #time.sleep(3)
        self.driver.find_element(By.CSS_SELECTOR, ".comprar").click()
        assert self.driver.find_element(By.CSS_SELECTOR, ".item-title").text == "Mantis"
        assert self.driver.find_element(By.CSS_SELECTOR, ".new-price").text == "R$ 59,99"