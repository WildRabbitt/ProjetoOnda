from utils import *
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

email = 'thiago@ondaagil.com.br'  # input("Digite aqui seu e-mail: ")
senha = '4815162342'  # input("Digite aqui a sua senha: ")
statuscontr = ''
row = '1'

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

navegador.find_element(By.XPATH, '/html/body/div[1]/div[3]/div/div[1]/div[11]/div/a').click()  # Clicar em suporte
sleep(1.8)
navegador.find_element(By.XPATH,'/html/body/div[1]/div[3]/div/div[1]/div[12]/ul/li[2]/a').click()  # Clicar em Ordem de Serviço
sleep(2)

# Preencher assunto e setor
navegador.find_element(By.XPATH, '//*[@id="1_grid"]/div/div[3]/table/tbody/tr/td[1]/div[4]/input[1]').send_keys('login')
navegador.find_element(By.XPATH, '//*[@id="1_grid"]/div/div[3]/table/tbody/tr/td[1]/div[4]/input[2]').send_keys('estoque')
sleep(1)
navegador.find_element(By.XPATH, '/html/body/div[2]/div/div[3]/table/tbody/tr/td[5]/div[1]/input[1]').click()
sleep(1.5)

while row != 0:
        xpathlog = '/html/body/div[2]/div/div[6]/table/tbody/tr[' + row + ']/td[1]/div'

        navegador.find_element(By.XPATH, xpathlog).click()
        navegador.find_element(By.XPATH, xpathlog).click()
        print("Ok")

        navegador.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div[1]/button[2]').click()  # Cliar em editar /
        sleep(1.5)

        navegador.find_element(By.XPATH,'/html/body/form[2]/div[3]/div[1]/dl[6]/dd/button[2]').click()  # Abrir cadastro cliente
        sleep(1.5)
        navegador.find_element(By.XPATH, '/html/body/form[3]/div[3]/ul/li[7]/a').click()  # Abrir aba contrato
        sleep(1.5)
        nome = str.lower(navegador.find_element(By.XPATH,'/html/body/form[3]/div[3]/div[7]/dl/div/div/div[5]/table/tbody/tr/td[5]/div').text)  #Salvar nome da cliente
        print("Nome é:",nome)
        sleep(1)

        rowcont = '1'
        xpathcont_stats = '/html/body/form[3]/div[3]/div[7]/dl/div/div/div[5]/table/tbody/tr/td[3]/div/span'
        xpathcont_id = '/html/body/form[3]/div[3]/div[7]/dl/div/div/div[5]/table/tbody/tr/td[1]/div'
        sleep(2)
        statuscontr = navegador.find_element(By.XPATH, xpathcont_stats).text # Copiar o status do contrato

        if statuscontr != '(P) Pré-contrato':  # Verificar se o status não está como pre contrato
            while statuscontr != '(P) Pré-contrato':
                rowcont = str(int(rowcont) + 1)
                xpathcont_stats = '/html/body/form[3]/div[3]/div[7]/dl/div/div/div[5]/table/tbody/tr[' + rowcont + ']/td[3]/div/span'
                statuscontr = navegador.find_element(By.XPATH, xpathcont_stats)
                pass
            xpathcont_id = '/html/body/form[3]/div[3]/div[7]/dl/div/div/div[5]/table/tbody/tr[' + rowcont + ']/td[1]/div'
            pass

        idcont = str(navegador.find_element(By.XPATH, xpathcont_id).text)  # Pegar o id do contrato
        print("Numero contrato é "+idcont)
        login = gerar_login(nome,idcont)
        print(login)






# pesquisa ID contrato
