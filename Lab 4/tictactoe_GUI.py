import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, master):
        self.master = master
        master.title("Tic Tac Toe")
        self.current_player = "X"
        self.board = [None] * 9
        self.buttons = []

        self.status_label = tk.Label(master, text="Player X's turn", font=("Arial", 14))
        self.status_label.grid(row=0, column=0, columnspan=3)

        for i in range(9):
            btn = tk.Button(master, text="", font=("Arial", 24), width=5, height=2,
                            command=lambda i=i: self.make_move(i))
            btn.grid(row=1 + i // 3, column=i % 3)
            self.buttons.append(btn)

    def make_move(self, index):
        if self.board[index] is None:
            self.board[index] = self.current_player
            self.buttons[index].config(text=self.current_player)
            if self.check_winner(self.current_player):
                messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")
                self.reset_board()
            elif None not in self.board:
                messagebox.showinfo("Game Over", "It's a tie!")
                self.reset_board()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"
                self.status_label.config(text=f"Player {self.current_player}'s turn")

    def check_winner(self, player):
        wins = [
            [0,1,2], [3,4,5], [6,7,8], # rows
            [0,3,6], [1,4,7], [2,5,8], # columns
            [0,4,8], [2,4,6]           # diagonals
        ]
        for combo in wins:
            if all(self.board[i] == player for i in combo):
                return True
        return False

    def reset_board(self):
        self.board = [None] * 9
        for btn in self.buttons:
            btn.config(text="")
        self.current_player = "X"
        self.status_label.config(text="Player X's turn")

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()