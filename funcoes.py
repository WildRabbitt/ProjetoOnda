from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from time import sleep

def gerar_login(nome,contrato):
   nomes = str(nome).split()   #Separar o nome completo em nomes
   login = ''
   for inicial in nomes:     #Para cada nome pegar a primeira letra
      login = login + inicial[0]  #Juntar cada letra com o login
      pass
   login = login+str(contrato) #Juntar o login com o id do contrato
   return login


def criacaologin(navegador):
    navegador.find_element(By.XPATH, '/html/body/div[1]/div[3]/div/div[1]/div[11]/div/a').click()  # Clicar em suporte
    sleep(1.8)
    navegador.find_element(By.XPATH,
                           '/html/body/div[1]/div[3]/div/div[1]/div[12]/ul/li[2]/a').click()  # Clicar em Ordem de Serviço
    sleep(2)

    # Preencher assunto e setor
    navegador.find_element(By.XPATH, '//*[@id="1_grid"]/div/div[3]/table/tbody/tr/td[1]/div[4]/input[1]').send_keys(
        'login')
    navegador.find_element(By.XPATH, '//*[@id="1_grid"]/div/div[3]/table/tbody/tr/td[1]/div[4]/input[2]').send_keys(
        'estoque')
    sleep(1)
    navegador.find_element(By.XPATH, '/html/body/div[2]/div/div[3]/table/tbody/tr/td[5]/div[1]/input[1]').click()
    sleep(1.5)

    row = 1  # Linha das criações de login
    try:
        for row in range(1, 19):
            row = str(row)
            xpathlog = '/html/body/div[2]/div/div[6]/table/tbody/tr[' + row + ']/td[15]/div'
            print(row)
            mensagemOS = ''
            mensagemEvento = str(
                "Processo: Eventos. Tarefa: Criar Login/Configurar KIT EVENTO Descrição OS anterior: CONTRATO CONFERIDO E ASSINADO")
            if mensagemOS == mensagemEvento:
                print('Evento!')

            if row == '1':
                navegador.find_element(By.XPATH, xpathlog).click()
                navegador.find_element(By.XPATH, xpathlog).click()
            else:
                navegador.find_element(By.XPATH, xpathlog).click()
            print("Ok")

            navegador.find_element(By.XPATH,
                                   '/html/body/div[2]/div/div[2]/div[1]/button[2]').click()  # Cliar em editar /
            sleep(1.5)
            navegador.find_element(By.XPATH,
                                   '/html/body/form[2]/div[3]/div[1]/dl[6]/dd/button[3]').click()  # Abrir cadastro cliente
            sleep(1.5)
            navegador.find_element(By.XPATH, '/html/body/form[3]/div[3]/ul/li[7]/a').click()  # Abrir aba contrato
            sleep(1.5)
            nome = str.lower(navegador.find_element(By.XPATH,
                                                    '/html/body/form[3]/div[3]/div[7]/dl/div/div/div[5]/table/tbody/tr/td[5]/div').text)  # Salvar nome da cliente
            print("Nome é:", nome)
            sleep(1)

            rowcont = '1'  # Linha de verificação dos contratos
            xpathcont_stats = '/html/body/form[3]/div[3]/div[7]/dl/div/div/div[5]/table/tbody/tr/td[3]/div/span'
            xpathcont_id = '/html/body/form[3]/div[3]/div[7]/dl/div/div/div[5]/table/tbody/tr/td[1]/div'
            sleep(2)
            statuscontr = navegador.find_element(By.XPATH, xpathcont_stats).text  # Copiar o status do contrato

            if statuscontr != '(P) Pré-contrato':  # Verificar se o status não está como pre contrato
                while statuscontr != '(P) Pré-contrato':
                    rowcont = str(int(rowcont) + 1)
                    xpathcont_stats = '/html/body/form[3]/div[3]/div[7]/dl/div/div/div[5]/table/tbody/tr[' + rowcont + ']/td[3]/div/span'
                    statuscontr = navegador.find_element(By.XPATH, xpathcont_stats)
                    pass
                xpathcont_id = '/html/body/form[3]/div[3]/div[7]/dl/div/div/div[5]/table/tbody/tr[' + rowcont + ']/td[1]/div'
                pass

            idcont = str(navegador.find_element(By.XPATH, xpathcont_id).text)  # Pegar o id do contrato
            print("Numero contrato é " + idcont)
            login = gerar_login(nome, idcont)
            print(login)
            navegador.find_element(By.XPATH, xpathcont_id).click()
            navegador.find_element(By.XPATH, xpathcont_id).click()
            navegador.find_element(By.XPATH,
                                   '/html/body/form[3]/div[3]/div[7]/dl/div/div/div[2]/div[1]/button[2]').click()  # Clicar em editar contrato
            sleep(3)
            navegador.find_element(By.XPATH,
                                   '/html/body/form[4]/div[3]/ul/li[10]/a').click()  # Clicar aba login dentro do contrato
            sleep(1)
            navegador.find_element(By.XPATH,
                                   '/html/body/form[4]/div[3]/div[10]/dl/div/div/div[3]/div[1]/button[1]').click()  # Clicar em Novo login
            sleep(2)
            navegador.find_element(By.XPATH,
                                   '/html/body/form[5]/div[3]/div[1]/dl[10]/dd/button[2]').click()  # Selecionar o plano (botao de pesquisa (/html/body/form[4]/div[3]/div[1]/dl[10]/dd/button[2]))
            sleep(2)
            navegador.find_element(By.XPATH,
                                   '//*[@id="6_grid"]/div/div[3]/span[1]/i[3]').click()  # Selecionar o plano (Botao de atualizar (/html/body/div[14]/div/div[3]/span[1]/i[3])
            sleep(2)
            # navegador.find_element(By.XPATH,'/html/body/div[12]/div/div[6]/table/tbody/tr/td[1]/div').click()  #Selecionar o plano (Primeira linha(/html/body/div[14]/div/div[6]/table/tbody/tr/td[2]/div)
            sleep(1)
            navegador.find_element(By.XPATH,
                                   '//*[@id="btn_inserir_registro_sel_grid"]').click()  # Inserir Registro de plano
            sleep(2)
            navegador.find_element(By.XPATH, '/html/body/form[5]/div[3]/div[1]/dl[11]/dd/input').send_keys(
                login)  # Preencher o login (/html/body/form[4]/div[3]/div[1]/dl[11]/dd/input)
            sleep(1)
            navegador.find_element(By.XPATH,
                                   '/html/body/form[5]/div[3]/div[1]/dl[14]/dd/button[1]').click()  # Preencher a senha (/html/body/form[4]/div[3]/div[1]/dl[14]/dd/button[1])
            sleep(0.5)
            ssid = (str.upper(nome).split())
            ssid = ssid[0]
            navegador.find_element(By.XPATH, '/html/body/form[5]/div[3]/div[1]/dl[18]/dd/input').send_keys(
                str.upper(ssid))  # Preencher nome do wifi
            sleep(0.5)
            navegador.find_element(By.XPATH, '/html/body/form[5]/div[3]/div[1]/dl[20]/dd/input').send_keys(
                str.upper(ssid))  # preencher nome do wifi
            sleep(0.5)
            print("Salvar")
            navegador.find_element(By.XPATH,
                                   '/html/body/form[5]/div[2]/button[2]').click()  # Salvar (/html/body/form[4]/div[2]/button[2])
            sleep(1.5)
            navegador.find_element(By.XPATH,
                                   '/html/body/form[5]/div[1]/div[3]/a[4]').click()  # Botaão fechar login(/html/body/form[4]/div[1]/div[3]/a[4])
            sleep(0.5)
            navegador.find_element(By.XPATH,
                                   '/html/body/form[4]/div[1]/div[3]/a[4]').click()  # Botao fechar contrato cliente (/html/body/form[3]/div[1]/div[3]/a[4])
            sleep(0.5)
            navegador.find_element(By.XPATH,
                                   '/html/body/form[3]/div[1]/div[3]/a[4]').click()  # Botão fechar Cliente(/html/body/form[2]/div[1]/div[3]/a[3])
            sleep(0.5)
            navegador.find_element(By.XPATH,
                                   '/html/body/form[2]/div[1]/div[3]/a[3]').click()  # Botão fechar Cliente(/html/body/form[2]/div[1]/div[3]/a[3])
            sleep(1)
            feito = feito.append(nome)
    except Exception as e:
        print(feito)
        print(e)
