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
    c = 0
    if(0<jogada<10 and ok == True ):
        jogada = str(jogada)
        if(jogada in a):
            a = a.replace(jogada, p)
            print(a)
            if (bool(a[2] == p) and bool(a[7] == p) and bool(a[13] == p)):
                print("------\nGanhou\n------")
                break
            elif (bool(a[37] == p) and bool(a[42] == p) and bool(a[48] == p)):
                print("------\nGanhou\n------")
                break
            elif (bool(a[72] == p) and bool(a[77] == p) and bool(a[83] == p)):
                print("------\nGanhou\n------")
                break
            elif (bool(a[2] == p) and bool(a[37] == p) and bool(a[72] == p)):
                print("------\nGanhou\n------")
                break
            elif (bool(a[7] == p) and bool(a[42] == p) and bool(a[77] == p)):
                print("------\nGanhou\n------")
                break
            elif (bool(a[2] == p) and bool(a[42] == p) and bool(a[83] == p)):
                print("------\nGanhou\n------")
                break
            elif (bool(a[13] == p) and bool(a[42] == p) and bool(a[72] == p)):
                print("------\nGanhou\n------")
                break
            
        else:
            print("Escolha outra opção")
            ok = False
    else:
        print("Opção inválida")
        


    ok = False
    while ok == False:
        j = str(random.randrange(1,10))
        
        if j in a:
            a = a.replace(j, b)
            ok = True
                        
            if (bool(a[2] == b) and bool(a[7] == b) and bool(a[13] == b)):
                print("------\nPerdeu\n------")
                ok = True
                break
            elif (bool(a[37] == b) and bool(a[42] == b) and bool(a[48] == b)):
                print("------\nPerdeu\n------")
                ok = True
                break
            elif (bool(a[72] == b) and bool(a[77] == b) and bool(a[83] == b)):
                print("------\nPerdeu\n------")
                ok = True
                break
            elif (bool(a[2] == b) and bool(a[37]== b) and bool(a[72] == b)):
                print("------\nPerdeu\n------")
                ok = True
                break
            elif (bool(a[7] == b) and bool(a[42] == b)and bool(a[77] == b)):
                print("------\nPerdeu\n------")
                ok = True
                break
            elif (bool(a[2] == b) and bool(a[42] == b) and bool(a[83] == b)):
                print("------\nPerdeu\n------")
                ok = True
                break
            elif (bool(a[13] == b) and bool(a[42] == b) and bool(a[72] == b)):
                print("------\nPerdeu\n------")
                ok = True
                break
        else:
            ok = False  
            

        

    
