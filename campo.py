import random         # para gerar números aleatórios
import time           # para gerar paradas tempBomborárias
import os             # para executar funções do sistema operacional

field = []
mine = []

size = 10

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
            
    # showTable()

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

    # setBomb()

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
                mine[x][y] = bomb
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
        # if mine[x][y] == bomb:
        #     # print(f"Você perdeu.")
        #     # time.sleep(3)
        #     showBombs(x, y)
        #     break
        # else:
        #     field[x][y] = empty

        surroundingTeste(x, y)
        time.sleep(1)

def surroundingTeste(x, y):

    # Testa se o local selecionado é bomb:
    if mine[x][y] == bomb:
        showBombs(x, y)
    else:
        field[x][y] = empty

    # Testa se tem bomba nos "arredores"       
    for lineNumber in range(-1, 2):
        for columnNumber in range(-1, 2):
            if 0 <= x+lineNumber < size and 0 <= y+columnNumber < size:
                if mine[x+lineNumber][y+columnNumber] == bomb:
                    print(f"Bomba no Local {x+lineNumber+1}, {y+columnNumber+1} Loop A")
                    field[x+lineNumber][y+columnNumber] = tempBomb
                    time.sleep(0.2)
                else:
                        print(f"Nada no local {x+lineNumber+1}, {y+columnNumber+1} Loop A")

                        # Testa se tem bomba ao arredor, dos arredores
                        nextLine = x + lineNumber
                        nextColumn = y + columnNumber
                        bombsAround(nextLine, nextColumn)
                        # field[x+i][y+columnNumber] = tempField
                        time.sleep(0.05)

def bombsAround(x, y):

    x = int(x)
    y = int(y)

    bombsCount = 0
    for lineNumber in range(-1, 2):
        for columnNumber in range(-1, 2):
            if 0 <= x+lineNumber < size and 0 <= y+columnNumber < size:
                if mine[x+lineNumber][y+columnNumber] == bomb:
                    bombsCount += 1
                    field[x+lineNumber][y+columnNumber] = bombsCount
                    print(f"Bomba no Local {x+lineNumber+1}, {y+columnNumber+1} Loop B")
                    time.sleep(0.2)
                else:
                        field[x+lineNumber][y+columnNumber] = tempField
                        print(f"Nada no local {x+lineNumber+1}, {y+columnNumber+1} Loop B")
                        time.sleep(0.05)

def endGame():
    opcao = input("Você deseja jogar novamente? (S/N) ").upper

    if opcao == "N":
        pararJogo = True


setTable()
showTable()
setBomb()
inputUser()