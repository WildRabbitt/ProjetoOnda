from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
import pandas as pd
from time import sleep

email = 'thiago'
senha = '4815162342'
i = 1

navegador: WebDriver = webdriver.Chrome()
navegador.get('https://ondaagil.flashman.anlix.io/login')
sleep(3)
navegador.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div/div/div/div/form/div[1]/input').send_keys(email)
navegador.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div/div/div/div/form/div[2]/input').send_keys(senha)
navegador.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div/div/div/div/form/div[3]/button').click()
sleep(3)
navegador.find_element(By.XPATH,'//*[@id="devices-search-form"]/div/div[1]/input').send_keys('offline >720')
sleep(1.5)
navegador.find_element(By.XPATH,'/html/body/div[2]/div[18]/div/form/div/div[3]/button').click()
sleep(4)
navegador.find_element(By.XPATH,'/html/body/div[2]/div[20]/div/div[1]/div[2]/div/div/div[1]/select').send_keys('500')
sleep(4)
while i < 500:
    i = str(i)
    row = '/html/body/div[2]/div[20]/div/div[2]/div/div/table/tbody/tr[' + i + ']/td[5]'
    usuario = '/html/body/div[2]/div[20]/div/div[2]/div/div/table/tbody/tr[' + i + ']/td[4]'
    mac = navegador.find_element(By.XPATH,row)
    usuario = navegador.find_element(By.XPATH,usuario)
    print (mac,usuario)
    arquivo=open('relatorio.xlsx','a')

    i= int(i)
    i= i+1



