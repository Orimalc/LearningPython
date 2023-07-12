import numpy as np

gameboard = np.asarray([[4, 4, 4, 4, 4, 4], [4, 4, 4, 4, 4, 4]])
scores = [0, 0]
isPlayed = True
turnOfPlayer = 1
def play():
    column = int(input()) - 1
    if turnOfPlayer == 2:
        column = 6 - column
    gameboard[turnOfPlayer - 1, column] = 0
while(isPlayed):
    print(f"Turn of Player: {turnOfPlayer}")
    print("State of the Board")
    print("Row of Player 1: ["
          f"{gameboard[0,0]}][{gameboard[0,1]}][{gameboard[0,2]}][{gameboard[0,3]}][{gameboard[0,4]}][{gameboard[0,5]}]")
    print("       <-----     1  2  3  4  5  6")
    print("Row of Player 2: ["
          f"{gameboard[1,0]}][{gameboard[1,1]}][{gameboard[1,2]}][{gameboard[1,3]}][{gameboard[1,4]}][{gameboard[1,5]}]")
    print("       ----->     6  5  4  3  2  1")
    play()
    print("".ljust(100, "*" ))
    print("\n\n\n")
    if (turnOfPlayer==1):
        turnOfPlayer = 2
    else:
        turnOfPlayer = 1