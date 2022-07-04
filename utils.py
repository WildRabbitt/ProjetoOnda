
import random
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

def geradorsenha():
   tamanho = 10
   valores = string.ascii_lowercase + string.digits + string.ascii_uppercase
   senha = ''
   for i in range(tamanho):
     senha += random.choice(valores)

   print(senha)


#https://brasilescola.uol.com.br/matematica/teorema-laplace.htm link das parada
#i == linha
#j == coluna
                        #colunas        #linhas
MATRIZ = [[0 for x in range(5)] for y in range(5)] #MATRIZ COMPLETA
matriz = [[0 for x in range(4)] for y in range(5)] #matriz sem a primeira coluna
column = [[0 for x in range(1)] for y in range(5)] #primeira coluna
linha = [[0 for x in range(5)] for y in range(1)] #primeira linha

for i in range(0,len(MATRIZ)): #Preencher MATRIZ

    for j in range(0,len(MATRIZ[i])):
        LINHA = random.randint(1,5)    #Preencher as linhas da MATRIZ
        MATRIZ[i][j] = LINHA
        column[i][0] = MATRIZ[i][0]
        if j>0:
            matriz[i][j-1] = MATRIZ[i][j]
        if i == 0:
            linha[i][j] = MATRIZ[i][j]



def imprimirmatriz3(matriz5):
   for i in range(len(matriz5)):
      for j in range(0, len(matriz5[i])):
         print(matriz5[i][j], end='  ')
      print()
      pass
   pass

print('MATRIZ COMPLETA')
imprimirmatriz3(MATRIZ)
print('\nMATRIZ SEM PRIMEIRA COLUNA')
imprimirmatriz3(matriz)
print('MATRIZ PRIMEIRA COLUNA')
imprimirmatriz3(column)
print('MATRIZ LINHA')
imprimirmatriz3(linha)