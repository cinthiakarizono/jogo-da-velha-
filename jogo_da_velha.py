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


a = "  1  |  2  |  3  \n-----------------\n  4  |  5  |  6  \n-----------------\n  7  |  8  |  9  "

print("Mapa do tabuleiro")
print(a)
jogada = input(f"Você é {p}, faça sua primeira jogada: ")
if(jogada in a):
    a = a.replace(jogada, p)
    print(a)        

