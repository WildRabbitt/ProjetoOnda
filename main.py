from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
import pandas as pd
from time import sleep
import tkinter as tk

email = 'thiago@ondaagil.com.br'#input("Digite aqui seu e-mail: ")
senha = '4815162342'#input("Digite aqui a sua senha: ")

navegador: WebDriver = webdriver.Chrome()
navegador.get('https://ondaagilixc.com.br/login.php')
navegador.find_element(By.XPATH, '//*[@id="email"]').send_keys(email)
navegador.find_element(By.XPATH, '//*[@id="senha"]').send_keys(senha)
navegador.find_element(By.XPATH, '//*[@id="entrar"]').click()
sleep(0.2)
if (navegador.title == 'Login IXCsoft'):
   navegador.find_element(By.XPATH, '//*[@id="entrar"]').click()
   sleep(4)
else:
   sleep(4)
#entrou no ixc

navegador.find_element(By.XPATH,'/html/body/div[1]/div[3]/div/div[1]/div[11]/div/a').click() #Clicar em suporte
sleep(1.8)
navegador.find_element(By.XPATH,'/html/body/div[1]/div[3]/div/div[1]/div[12]/ul/li[2]/a').click() #Clicar em Ordem de Serviço
sleep(2)

#Preencher assunto e setor
navegador.find_element(By.XPATH,'//*[@id="1_grid"]/div/div[3]/table/tbody/tr/td[1]/div[4]/input[1]').send_keys('login')
navegador.find_element(By.XPATH,'//*[@id="1_grid"]/div/div[3]/table/tbody/tr/td[1]/div[4]/input[2]').send_keys('estoque')
sleep(1)
navegador.find_element(By.XPATH,'/html/body/div[2]/div/div[3]/table/tbody/tr/td[5]/div[1]/input[1]').click()
sleep(1.5)


row='1'
xpath='/html/body/div[2]/div/div[6]/table/tbody/tr['+row+']/td[1]/div'
print(xpath)

navegador.find_element(By.XPATH,xpath).click()#Clicar
navegador.find_element(By.XPATH,xpath).click()#Clicar
sleep(0.7)
navegador.find_element(By.XPATH,'/html/body/div[2]/div/div[2]/div[1]/button[2]').click()#Cliar em editar /
sleep(1.5)
nome = navegador.find_element(By.XPATH,'/html/body/form[2]/div[3]/div[1]/dl[6]/dd/input[2]')
contrato = navegador.find_element(By.XPATH,'/html/body/form[2]/div[3]/div[1]/dl[10]/dd/input')
print (nome,contrato)

def gerar_login(nome,contrato):
   nomes = str(nome).split()
   login = ''
   for x in nomes:
      login = login + x[0]
      pass
   login = login+str(contrato)
   return login
login = gerar_login(nome,contrato)

navegador.find_element(By.XPATH,'/html/body/form[2]/div[3]/div[1]/dl[6]/dd/button[2]/img').click() #Abrir cliente
sleep(1.5)
navegador.find_element(By.XPATH,'/html/body/form[3]/div[3]/ul/li[8]/a').click() #clicar em login
sleep(0.8)
navegador.find_element(By.XPATH,'/html/body/form[3]/div[3]/div[8]/dl/div/div/div[2]/div[1]/button[1]').click() #Novo Login
sleep(1.5)
navegador.find_element(By.XPATH,'/html/body/form[4]/div[3]/div[1]/dl[7]/dd/input[1]').send_keys(contrato)#Preencher contrato
sleep(1)
navegador.find_element(By.XPATH,'/html/body/form[4]/div[3]/div[1]/dl[10]/dd/button[2]').click() #Abrir Planos
sleep(1)
navegador.find_element(By.XPATH,'/html/body/div[12]/div/div[3]/span[1]/i[3]').click()
sleep(1)
navegador.find_element(By.XPATH,'/html/body/div[12]/div/div[6]/table/tbody/tr/td[2]/div').click()
sleep(1)
navegador.find_element(By.XPATH,'/html/body/div[12]/div/div[2]/div[1]/button[2]').click()
sleep(1)
navegador.find_element(By.XPATH,'/html/body/div[12]/div/div[1]/div[2]/a[2]').click()
sleep(0.5)
login = gerar_login(nome,contrato)
navegador.find_element(By.XPATH,'/html/body/form[4]/div[3]/div[1]/dl[11]/dd/input').send_keys(login)
navegador.find_element(By.XPATH,'/html/body/form[4]/div[3]/div[1]/dl[14]/dd/button[1]').click()

def verificar_contratos(contrato):
   for i in range(12):
      try:
         linha = '1'
         q = '/html/body/form/div[3]/div[8]/dl/div/div/div[5]/table/tbody/tr['+linha+']/td[5]/div'
         ids=[]
         ids.append(navegador.find_element(By.XPATH,q))
         linha = int(linha) + 1
         linha = str(linha)
      except:
         Janela = tk.Tk()
         Janela.title('Erro!')
         labelctt = tk.Label (Janela,text='Não possui outro login')
         labelctt.grid(column=0,row=0)
         btnctt = tk.Button(Janela,command=Janela.destroy())
         btnctt.grid(column=2,row=0)
         Janela.mainloop()
         pass
      if contrato in ids:
         Janela2 = tk.Tk()
         Janela2.title('Erro!')
         labelctt = tk.Label(Janela2, text='Ja existe um login com este contrato')
         labelctt.grid(column=0, row=0)
         btnctt = tk.Button(Janela, command=Janela2.destroy())
         btnctt.grid(column=2, row=0)
         Janela2.mainloop()
      else:
         pass
      pass





#pesquisa ID contrato










