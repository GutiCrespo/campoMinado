import random         # para gerar números aleatórios
import time           # para gerar paradas temporárias
import os             # para executar funções do sistema operacional

field = []     # campo total
mine = []      # local das minas

size = 10      # tamanho do tabuleiro/número de bombas

bomb = "💣"
empty = "🟥"
default = "⬜"
tempBomb = "❌"
tempField = "⬛"
        
def setTable():
    
    for i in range(size):
        field.append([])
        for j in range(size):
            field[i].append(default)

def showTable():
    os.system("cls")

    # Troca de Linha
    for i in range(size):
        print(f"   {i+1}", end="")
    print("\n")

    # Troca de Linha:
    for i in range(size):
        print(f"{i+1}", end="")
        # Troca de Coluna:
        for j in range(size):
            print(f" {field[i][j]} ", end="")
        print("\n")

def setBomb():
        
    # Cria o campo de minas
    for i in range(size):
        mine.append([])
        for j in range(size):
            mine[i].append(empty)

    # Adiciona as bombas no campo de minas
    for i in range(size):
        mine.append([])
        while True:
            x = random.randint(0, size-1)        
            y = random.randint(0, size-1)        
            # bombs.append((x*10)+y)

            if mine[x][y] != bomb:
                print(f"Bomba no Local: {x} e {y} ")
                mine[x][y] = bomb
                # time.sleep(0.5)
                break

    # inputUser()
      
def showBombs(x, y):

    os.system("cls")

    for i in range(size):
        print(f"   {i+1}", end="")
    print("\n")

    for i in range(size):
        print(f"{i+1}", end="")
        for j in range(size):
            print(f" {mine[i][j]} ", end="")
        print("\n")
    
    print(f"bomb! Você perdeu.")
    print(f"Você inseriu linha {x+1} coluna {y+1}")

    time.sleep(2)

    endGame()
    
def inputUser():

    while True:
        # Mostra a tabela "atualizada"
        showTable()

        # Recebe e testa a resposta do usuário
        # while True:
        x = (int(input(f"Insira o a linha que você deseja testar: ")) - 1)
        y = (int(input(f"Insira o a coluna que você deseja testar: ")) - 1)
                           
            # break

        bombTest(x, y)
        time.sleep(1)

def bombTest(x, y):

    # Testa se o local selecionado é bomb:
    if mine[x][y] == bomb:
        showBombs(x, y)
    else:
        bombsAround(x, y)


def bombsAround(x, y):

    x = int(x)
    y = int(y)

    bombsCount = 0

    
    # faz um check na volta do local
    for lineNumber in range(-1, 2):
        for columnNumber in range(-1, 2):
            if (0 <= x+lineNumber < size and 0 <= y+columnNumber < size):   # Valida se ta dentro do campo
                if mine[x+lineNumber][y+columnNumber] == bomb:
                    bombsCount += 1
                    field[x+lineNumber][y+columnNumber] = tempBomb
                    print(f"Bomba no Local {x+lineNumber+1}, {y+columnNumber+1} Loop B")
                    time.sleep(0.2)
                else:
                    field[x+lineNumber][y+columnNumber] = tempField
                    print(f"Nada no local {x+lineNumber+1}, {y+columnNumber+1} Loop B")
                    time.sleep(0.05)
                

    print(bombsCount)

    # if bombsCount > 0:
    #     field[x][y] = bombsCount
    #     # return bombsCount
    # else:
    #     field[x][y] = empty
    
    # if x > 0 and y > 0:
    #     bombsCount(x+1, y+1)
    

def endGame():
    opcao = input("Você deseja jogar novamente? (S/N) ").upper

    if opcao == "N":
        pararJogo = True


setTable()
showTable()
setBomb()
inputUser()