print("###########################")
print("Bem vindo ao jogo da velha!")
print("###########################")


s = False
while s:
    input("Escolha a sua peça:\n1 - X\n2 - O\n:")
    if(input == "1"):
        p = "X"
        b = "O"
        s = True
    elif(input == "2"):
        p = "O"
        b = "X"
        s = True
    else:
        print("Opção inválida")

