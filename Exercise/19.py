import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Tic-Tac-Toe")
        self.current_player = "X"
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.create_board()

    def create_board(self):
        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(self.root, text="", font=("Helvetica", 20), width=5, height=2,
                                                command=lambda row=i, col=j: self.make_move(row, col))
                self.buttons[i][j].grid(row=i, column=j)

    def make_move(self, row, col):
        if self.board[row][col] == ' ':
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player)
            if self.check_winner() or self.check_draw():
                self.end_game()
            else:
                self.current_player = 'O' if self.current_player == 'X' else 'X'

    def check_winner(self):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != ' ':
                self.highlight_winner(i, 0, i, 1, i, 2)
                return True
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != ' ':
                self.highlight_winner(0, i, 1, i, 2, i)
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ':
            self.highlight_winner(0, 0, 1, 1, 2, 2)
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ':
            self.highlight_winner(0, 2, 1, 1, 2, 0)
            return True
        return False

    def highlight_winner(self, *coords):
        for i in range(0, len(coords), 2):
            self.buttons[coords[i]][coords[i+1]].config(bg='light green')

    def check_draw(self):
        for row in self.board:
            for cell in row:
                if cell == ' ':
                    return False
        return True

    def end_game(self):
        if self.check_winner():
            messagebox.showinfo("Winner", f"Player {self.current_player} wins!")
        else:
            messagebox.showinfo("Draw", "It's a draw!")
        self.root.quit()

    def play(self):
        self.root.mainloop()

if __name__ == "__main__":
    game = TicTacToe()
    game.play()
