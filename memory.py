import random
import time
import os

# game = [21 = 🍟]
# bets = [21 = 🍟]

game = []
bets = []

temp = "🍕🍕🍔🍔🍟🍟🌭🌭🧀🧀🥩🥩🍤🍤🍣🍣"

images = list(temp)

def fill_matriz():
    for i in range(4):
        game.append([])
        bets.append([])
        for _ in range(4):
            num = random.randint(0, len(images)-1)
            game[i].append(images[num])
            bets[i].append("🟥")
            images.pop(num)
            
def show_images():
    os.system("cls")
    print("   1   2   3   4")
    for i in range(4):
        print(f"{i+1}", end="")
        for j in range(4):
            print(f" {game[i][j]} ", end="")
        print("\n")
    
    print("Memorize the food position")
    
    print("Game starting in: ", end="")
    for i in range(5, 0, -1):
        print(f"{i} ", end="", flush=True)
        time.sleep(1)

def show_board():
    os.system("cls")
    print("   1   2   3   4")
    for i in range(4):
        print(f" {i+1}", end="")
        for j in range(4):
            print(f" {bets[i][j]} ", end="")
        print("\n")

def make_bet(num):
    while True:
        show_board()
        
        bet = input(f"{num}ª Figure (insert row and column):")
        
        if len(bet) != 2:
            print("Invalid Number. Please, insert just the row and column numbers.")
            time.sleep(3)
 
            continue
        
        x = int(bet[0])-1
        y = int(bet[1])-1
        
        try:
            if  bets[x][y] == "🟥":
                bets[x][y] = game[x][y]
                print(bets[x][y])
                print(game[x][y])
                time.sleep(5)
                break
            else:
                print("Already showed. Try another number")
                time.sleep(3)
        
        except IndexError:
            print("Invlid Position. Please, try again.")
            time.sleep(3)
            
                  
    return (x, y)               

fill_matriz()
show_images()

while True:
    x1, y1 = make_bet(1)
    x2, y2 = make_bet(2)
    show_board()
    
    if bets[x1][y1] == bets[x2][y2]:
        print("Nice! You got it.")
        time.sleep(2)
    
    else:
        print("Nops, you missed")
        bets[x1][y1] = "🟥"
        bets[x2][y2] = "🟥"
        exit = input("Do you wanna continue (Y/N)? ").upper()
        if exit == "N":
            break
