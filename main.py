# from utils import *
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from time import sleep
from funcoes import *

email = 'thiago@ondaagil.com.br'  # input("Digite aqui seu e-mail: ")
senha = '4815162342'  # input("Digite aqui a sua senha: ")
statuscontr = ''
feito = ['']


navegador: WebDriver = webdriver.Edge()
navegador.get('https://ondaagilixc.com.br/login.php')
navegador.find_element(By.XPATH, '//*[@id="email"]').send_keys(email)
navegador.find_element(By.XPATH, '//*[@id="senha"]').send_keys(senha)
navegador.find_element(By.XPATH, '//*[@id="entrar"]').click()
sleep(0.2)

if navegador.title == 'Login IXCsoft':
    navegador.find_element(By.XPATH, '//*[@id="entrar"]').click()
    sleep(5)
else:
    sleep(5)
# entrou no ixc

criacaologin(navegador)


# pesquisa ID contrato
