import numpy as np


class Game:
    def __init__(self):
        self.board = np.asarray([4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 0])
        self.is_played = True
        self.turn_of_player = 1

    def play(self, user_input):

        if user_input > 6 or user_input < 1:
            return
        distance = user_input
        if self.turn_of_player == 1:
            column = 6 - distance
        else:
            column = 13 - distance
        amount_of_stones = self.board[column]
        self.board[column] = 0
        if amount_of_stones + 6 - distance > 12:
            amount_of_stones += 1
            if self.turn_of_player == 1:
                self.board[13] -= 1
            else:
                self.board[6] -= 1

        if column + amount_of_stones > 13:
            diff = 13 - (column + amount_of_stones)
            self.board[column + 1: column + amount_of_stones + diff + 1] += 1
            self.board[0:-diff] += 1
            self.try_to_steal(distance, column, amount_of_stones, diff)
        else:
            self.board[column + 1:column + amount_of_stones + 1] += 1
            self.try_to_steal(distance, column, amount_of_stones)
        if amount_of_stones != distance:
            self.turn_of_player = self.turn_of_player % 2 + 1

    def start_game(self):
        while self.is_played:
            print(f"Turn of Player: {self.turn_of_player}")
            print(f"Score: Player 1:Player 2  ||  {self.board[6]}:{self.board[13]}")
            print("State of the Board")
            print("Row of Player 1: ["
                  f"{self.board[5]}][{self.board[4]}]"
                  f"[{self.board[3]}][{self.board[2]}][{self.board[1]}][{self.board[0]}]")
            print("       <-----     1  2  3  4  5  6")
            print("Row of Player 2: ["
                  f"{self.board[7]}][{self.board[8]}]"
                  f"[{self.board[9]}][{self.board[10]}][{self.board[11]}][{self.board[12]}]")
            print("       ----->     6  5  4  3  2  1")
            self.play(int(input()))
            if self.game_over():
                self.is_played = False
            print("".ljust(100, "*"))
            print("\n\n\n")

    def game_over(self):

        if np.asarray(self.board[0:6]).any() and np.asarray(self.board[7:13]).any():
            return False

        return True

    def try_to_steal(self, distance, column, amount_of_stones, diff=0):

        if -diff > 0:
            column = -diff - 1
            if self.turn_of_player == 1 and -diff< 6:
                if self.board[column] == 1 \
                        and self.board[column + 2*(5-column) + 2] > 0:
                    self.board[6] += self.board[column + 2*(5-column) + 2] + 1
                    self.board[column + 2*(5-column) + 2] = 0
                    self.board[column] = 0
                    return
            if self.turn_of_player == 2 and column + amount_of_stones < 13:
                if self.board[column] == 1 \
                        and self.board[column - 2*(column-7) -1] > 0:
                    self.board[13] += self.board[column - 2*(column-7) -1] + 1
                    self.board[column - 2*(column-7) -1] = 0
                    self.board[column] = 0
                    return

        elif self.turn_of_player == 1 and column + amount_of_stones < 6:
            if self.board[column + amount_of_stones] == 1 \
                    and self.board[column + amount_of_stones + (column + 1)] > 0:
                self.board[6] += self.board[column + amount_of_stones + (column + 1)] + 1
                self.board[column + amount_of_stones + (column + 1)] = 0
                self.board[column + amount_of_stones] = 0
                return
        elif self.turn_of_player == 2 and column + amount_of_stones < 13:
            if self.board[column + amount_of_stones] == 1 \
                    and self.board[13 - (column + amount_of_stones) - 1] > 0:
                self.board[13] += self.board[13 - (column + amount_of_stones) - 1] + 1
                self.board[13 - (column + amount_of_stones) - 1] = 0
                self.board[column + amount_of_stones] = 0
                return



if __name__ == "__main__":
    game = Game()
    game.start_game()
