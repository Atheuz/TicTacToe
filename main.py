"""Tic Tac Toe game."""
import enum

import numpy as np


class Player(enum.Enum):
    """Player enum."""

    X = -1
    O = 1


class TicTacToe:
    """TicTacToe class."""

    def __init__(self, size: int) -> None:
        """Constructor."""
        self.size = size
        self.board = np.zeros((self.size, self.size), dtype=np.int8)
        self.players = (Player.X, Player.O)
        self.turn = Player.X

    def perform_play(self, x: int, y: int) -> None:
        """Make a play at (x,y) coordinates for the player whose turn it currently is."""
        if self.board[x, y] != 0:
            print("Not a valid move, someone has already played there.")
        if x > self.size - 1 or y > self.size - 1 or x < 0 or y < 0:
            print("Not a valid move, outside the board.")
        else:
            self.board[x, y] = self.turn.value
            # Check if the game is over.
            check = self.check_board()
            if check:
                print(check)
                print(self.draw_board())
                print("Game over!")
            else:
                if self.turn == Player.X:
                    self.turn = Player.O
                else:
                    self.turn = Player.X
                print(self.draw_board())

    def check_board(self) -> str:
        """Check if there is any winner yet, or a draw."""
        winner = (1 * self.size, -1 * self.size)
        checks = []
        for i in range(self.size):
            checks.append(sum(self.board[:, i]))
            checks.append(sum(self.board[i, :]))
        checks.append(sum(self.board.diagonal(0)))
        checks.append(sum(np.fliplr(self.board).diagonal(0)))

        winner = any(t in winner for t in checks)
        if winner:
            return "{} wins.".format(self.turn.name)
        if not 0 in self.board:
            return "Draw!"
        else:
            return ""

    def draw_board(self) -> str:
        """Draw the current board state."""
        top_row = ""
        cols = ""
        for i in range(self.size):
            top_row += " " + str(i)
            cols += str(i)
            for j in range(self.size):
                cell = self.board[i, j]
                if cell != 0:
                    val = Player(cell).name
                else:
                    val = " "
                cols += val + " "
            cols += "\n"
        return top_row + "\n" + cols


def main():
    """Main entry point."""
    t = TicTacToe(3)
    while not t.check_board():
        x, y = [int(x) for x in input("Where do you ({}) want to play? ".format(t.turn.name)).split(",")]
        t.perform_play(x, y)


if __name__ == "__main__":
    main()
