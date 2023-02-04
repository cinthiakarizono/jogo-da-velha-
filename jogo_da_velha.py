import random

print("##########################################")
print("       Bem vindo ao jogo da velha!")
print("##########################################")


s = False
while s == False:
    
    n = int(input("Escolha a sua peça:\n1 - X\n2 - O\n:"))
    if(n == 1):
        p = "X"
        b = "O"
        s = True
    elif(n == 2):
        p = "O"
        b = "X"
        s = True
    else:
        print("Opção inválida")


a = "  1 |  2  |  3  \n-----------------\n  4 |  5  |  6  \n-----------------\n  7 |  8  |  9  "
   

    
while True:
    print("Mapa do tabuleiro")
    print(a)
    

    
    jogada = input(f"Você é {p}, faça sua jogada: ")
    jogada = int(jogada)
    ok = True
    if(0<jogada<10 and ok == True ):
        jogada = str(jogada)
        if(jogada in a):
            a = a.replace(jogada, p)
            print(a)
            if (a[2] and a[7] and a[13] == p):
                print("Ganhou")
                break
            elif (a[37] and a[42] and a[48] == p):
                print("Ganhou")
                break
            elif (a[72] and a[77] and a[83] == p):
                print("Ganhou")
                break
            elif (a[2] and a[37] and a[72] == p):
                print("Ganhou")
                break
            elif (a[7] and a[42] and a[77] == p):
                print("Ganhou")
                break
            elif (a[2] and a[42] and a[83] == p):
                print("Ganhou")
                break
            elif (a[13] and a[42] and a[72] == p):
                print("Ganhou")
                break
            
        else:
            print("Escolha outra opção")
            ok = False
    else:
        print("Opção inválida")
        


    ok = False
    while ok == False:
        j = str(random.randrange(1,10))
        print(j)
        if j in a:
            a = a.replace(j, b)
            print(a)
            ok = True
            print(a)
            
            if (a[2] and a[7] and a[13] == b):
                print("Perdeu")
                break
            elif (a[37] and a[42] and a[48] == b):
                print("Perdeu")
                break
            elif (a[72] and a[77] and a[83] == b):
                print("Perdeu")
                break
            elif (a[2] and a[37] and a[72] == b):
                print("Perdeu")
                break
            elif (a[7] and a[42] and a[77] == b):
                print("Perdeu")
                break
            elif (a[2] and a[42] and a[83] == b):
                print("Perdeu")
                break
            elif (a[13] and a[42] and a[72] == b):
                print("Perdeu")
                break
        else:
            ok = False  
 

        

    
