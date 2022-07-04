def case1 (peso):
    print("Seu peso na terra é ",(peso/10)*0.37)
    pass
def case2 (peso):
    print("Seu peso na terra é ", (peso/10)*0.88)
    pass
def case3 (peso):
    print("Seu peso na terra é ", (peso/10)*0.38)
    pass
def case4 (peso):
    print("Seu peso na terra é ", (peso/10)*2.64)
    pass
def case5 (peso):
    print("Seu peso na terra é ", (peso/10)*1.15)
    pass
def case6 (peso):
    print("Seu peso na terra é ", (peso/10)*1.17)
    pass
def caseerro ():
    print("Este planeta não pode ser analizado")
    pass


def atividade01 ():
    try:
        op= int(input("Planetas que podem ser analisados \n1 - Mercurio\n2 - Vênus\n"
          "3 - Marte\n4 - Jupiter\n5 - Saturno\n6 - Urano\nESCOLHA UM PLANETA A SER ANALISADO"))
        pterra = float(input("Entre com um peso na terra"))
    except:
        print("Planeta ou peso inválido, tente novamente")
    if (op == 1):
        case1(pterra)
        pass
    elif (op == 2):
        case2(pterra)
        pass
    elif (op == 3):
        case3(pterra)
        pass
    elif (op == 4):
        case4(pterra)
        pass
    elif (op == 5):
        case5(pterra)
        pass
    elif (op == 6):
        case6(pterra)
        pass
    else:
        caseerro()
        pass

    print("\nFIM")
def atividade02 ():
    print("Verificador de multiplo de 3")
    try:
        num = float(input("Digite um número"))
        if (num % 3 == 0):
            print("O número Digitado é multiplo de 3")
            pass
        else:
            print("O numero digitado não é multiplo de 3")
            pass
    except:
        print("Numero digitado inválido, digite somente números")
    print("\nFim atividade 02")
def atividade03 ():
    print("Verificação se o número é multiplo de 5")
    try:
        num = float(input("Digite um númeoro"))
        if (num % 5 == 0):
            print("\nO número inserido é multiplo de 5")
            pass
        else:
            print("\nO número inserido não é multiplo de 5")
            pass
        pass

    except:
        print("\nNúmero inválido")
        pass
def atividade04 ():
    print("Verificação se numero é divisivel por 10, por 5, por 2 ou por nenhum")
    try:
        num = float(input("Digite um numero"))
        if (num % 10 == 0):
            print("\nMultiplo de 10")
            pass
        elif (num % 2 == 0):
            print("\nMultiplo de 2")
            pass
        elif (num % 5 == 0):
            print("\nMultiplo de 5")
            pass
        else:
            print("\nNão é multiplo de 2 nem de 5")
            pass
        pass
    except:
        print("\nDigite um número válido")
        pass
def atividade05 ():
    print("Diagonal Principal")
    L =-1
    t = -1
    for L in range(10):
        print(L, "-", L,"\n")
        for t in range(L) :
            print('\t')
            pass
        pass
    print("\n")
    pass

def insere(estrutura,elemento):
    estrutura.append(elemento)
    print(estrutura)
    return estrutura
def remove(estrutura):
    if len(estrutura)>0:
        return estrutura.pop()
    else:
        print("erro")





#Main
estrutura =[]
insere(estrutura,1)
insere(estrutura,22)
insere(estrutura,333)
insere(estrutura,4444)
while (len(estrutura)>0):
    print(remove(estrutura))


numatividade = None #int(input("Digite o numero da atividade desejada"))



if numatividade == 1:
    atividade01()
    pass
elif numatividade == 2:
    atividade02()
    pass
elif numatividade == 3:
    atividade03()
    pass
elif numatividade ==4:
    atividade04()
    pass
elif numatividade == 5:
    atividade05()
    pass
elif numatividade == 6:
    atividade06()
    pass
elif numatividade == 7:
    atividade07()
    pass
elif numatividade == 8:
    atividade08()
    pass
elif numatividade == 9:
    atividade09()
    pass
elif numatividade == 10:
    atividade10()
    pass