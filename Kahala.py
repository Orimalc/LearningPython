import numpy as np


class Game:
    def __init__(self):
        self.board = np.asarray([[4, 4, 4, 4, 4, 4], [4, 4, 4, 4, 4, 4]])
        self.scores = [0, 0]
        self.is_played = True
        self.turn_of_player = 1

    def play(self):
        distance = int(input())
        column = distance - 1
        if self.turn_of_player == 2:
            column = 5 - column
        amount_of_stones = self.board[self.turn_of_player - 1, column]
        if amount_of_stones >= distance:
            self.scores[self.turn_of_player - 1] += 1

        for i in range(1, amount_of_stones + 1):
            if self.turn_of_player == 1:
                if column - i < -1:
                    self.board[self.turn_of_player, -(column - i)-2] += 1
                elif column - i > -1:
                    self.board[self.turn_of_player - 1, column - i] += 1
            else:
                if column + i > 6:
                    #TODO fehler beim übergang !!!
                    self.board[self.turn_of_player - 2, 6 - (np.abs(i - column))] += 1
                elif column + i < 6:
                    self.board[self.turn_of_player - 1, column + i] += 1
        self.board[self.turn_of_player - 1, column] = 0

        if amount_of_stones != distance:
            self.turn_of_player = self.turn_of_player % 2 + 1
    def startGame(self):
        while (self.is_played):
            print(f"Turn of Player: {self.turn_of_player}")
            print(f"Score: Player 1 | Player 2 : {self.scores[0]} | {self.scores[1]}")
            print("State of the Board")
            print("Row of Player 1: ["
                f"{self.board[0, 0]}][{self.board[0, 1]}]"
                f"[{self.board[0, 2]}][{self.board[0, 3]}][{self.board[0, 4]}][{self.board[0, 5]}]")
            print("       <-----     1  2  3  4  5  6")
            print("Row of Player 2: ["
                f"{self.board[1, 0]}][{self.board[1, 1]}]"
                f"[{self.board[1, 2]}][{self.board[1, 3]}][{self.board[1, 4]}][{self.board[1, 5]}]")
            print("       ----->     6  5  4  3  2  1")
            self.play()
            print("".ljust(100, "*"))
            print("\n\n\n")


game = Game()
game.startGame()