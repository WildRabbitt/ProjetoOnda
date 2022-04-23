from time import sleep
from utils import *
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
def inciarnav():
   WebDriver = webdriver.Edge()
   return WebDriver

def gerar_login(nome,contrato):
   nomes = str(nome).split()   #Separar o nome completo em nomes
   login = ''
   for inicial in nomes:     #Para cada nome pegar a primeira letra
      login = login + inicial[0]  #Juntar cada letra com o login
      pass
   login = login+str(contrato) #Juntar o login com o id do contrato
   return login




def verificar_contratos(contrato,navegador):
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
