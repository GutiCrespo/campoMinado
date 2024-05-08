import random         # para gerar números aleatórios
import time           # para gerar paradas temporárias
import os             # para executar funções do sistema operacional

campo = []
mina = []

tamanho = 5

bomba = "💣"
vazio = "⬛"
naoClicado = "⬜"

        
def setTable():
    
    for i in range(tamanho):
        campo.append([])
        for j in range(tamanho):
            campo[i].append(naoClicado)
            
    # showTable()

def showTable():
    os.system("cls")

    # Troca de Linha
    for i in range(tamanho):
        print(f"   {i+1}", end="")
    print("\n")

    # Troca de Coluna
    for i in range(tamanho):
        print(f"{i+1}", end="")
        for j in range(tamanho):
            print(f" {campo[i][j]} ", end="")
        print("\n")

    # setBomb()

def setBomb():
        
    # Cria o campo de minas
    for i in range(tamanho):
        mina.append([])
        for j in range(tamanho):
            mina[i].append(vazio)

    # Adiciona as bombas no campo de minas
    for i in range(tamanho):
        mina.append([])
        while True:
            x = random.randint(0, tamanho-1)        
            y = random.randint(0, tamanho-1)        
            # bombas.append((x*10)+y)

            if mina[x][y] != bomba:
                mina[x][y] = bomba
                break

    # inputUser()
      
def showBombs(x, y):

    os.system("cls")

    for i in range(tamanho):
        print(f"   {i+1}", end="")
    print("\n")
    for i in range(tamanho):
        print(f"{i+1}", end="")
        for j in range(tamanho):
            print(f" {mina[i][j]} ", end="")
        print("\n")
    
    print(f"Bomba! Você perdeu.")
    print(f"Você inseriu linha {x+1} coluna {y+1}")

    time.sleep(2)

    # endGame()
    
def inputUser():

    while True:
        # Mostra a tabela "atualizada"
        showTable()

        # Recebe e testa a resposta do usuário
        while True:
            coordinate = input(f"Insira o número da linha e coluna que você deseja testar: ")
                
            if len(coordinate) != 2:
                print("Invalid Number. Please, insert just the row and column numbers.")
                time.sleep(3)

                continue
            
            x = int(coordinate[0])-1
            y = int(coordinate[1])-1

            break

        # # Testa se a posição é "bomba"
        # if mina[x][y] == bomba:
        #     # print(f"Você perdeu.")
        #     # time.sleep(3)
        #     showBombs(x, y)
        #     break
        # else:
        #     campo[x][y] = vazio

        surroundingTeste(x, y)

def surroundingTeste(x, y):
    if mina[x][y] == bomba:
        showBombs(x, y)
    else:
        campo[x][y] = vazio



# def endGame():
#     opcao = input("Você deseja jogar novamente? (S/N) ").upper

#     if opcao == "N":
#         pararJogo = True


setTable()
showTable()
setBomb()
inputUser()