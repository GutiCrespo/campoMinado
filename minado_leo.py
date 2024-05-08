import os
import random

jogo = []

def preenche_matriz():
    for i in range(5):
        jogo.append([])
        for j in range(5):
            jogo[i].append("🟥")
            
 # Adiciona minas em três lugares aleatórios
    for _ in range(3):
        while True:
            linha = random.randint(0, 4)
            coluna = random.randint(0, 4)
            if jogo[linha][coluna] != "💣": 
                jogo[linha][coluna] = "💣"
                break


def mostra_tabuleiro():
    os.system("cls")
    print("  1  2  3  4  5")
    for i in range(5):
        print(f"{i+1}", end="")
        for j in range(5):
            print(f"{jogo[i][j]}", end=" ")
        print("")  # Print apenas uma quebra de linha após cada linha do tabuleiro

preenche_matriz()
mostra_tabuleiro()