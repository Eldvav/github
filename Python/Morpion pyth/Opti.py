import tkinter
from tkinter import messagebox

class TicTacToe:
    SYMBOL_X = 'X'
    SYMBOL_O = 'O'

    def __init__(self, root):
        self.buttons = []
        self.current_player = self.SYMBOL_X
        self.win = False
        self.root = root
        self.draw_grid()

    def print_winner(self):
        self.win = True
        winner = f"Le joueur {self.current_player} a gagné le jeu !"
        restart_option = "Voulez-vous recommencer la partie ?"
        if messagebox.askyesno("Fin de partie", f"{winner}\n{restart_option}"):
            self.reset_game()
        else:
            quit()


    def switch_player(self):
        if self.current_player == self.SYMBOL_X:
            self.current_player = self.SYMBOL_O
        else:
            self.current_player = self.SYMBOL_X

    def check_win(self, clicked_row, clicked_col):
        # détecter victoire horizontale
        count = 0
        for i in range(3):
            current_button = self.buttons[i][clicked_row]
            if current_button['text'] == self.current_player:
                count += 1
        if count == 3:
            self.print_winner()

        # détecter victoire verticale
        count = 0
        for i in range(3):
            current_button = self.buttons[clicked_col][i]
            if current_button['text'] == self.current_player:
                count += 1
        if count == 3:
            self.print_winner()

        # détecter victoire diagonale
        count = 0
        for i in range(3):
            current_button = self.buttons[i][i]
            if current_button['text'] == self.current_player:
                count += 1
        if count == 3:
            self.print_winner()

        # détecter victoire diagonale inverse
        count = 0
        for i in range(3):
            current_button = self.buttons[2 - i][i]
            if current_button['text'] == self.current_player:
                count += 1
        if count == 3:
            self.print_winner()

        if not self.win:
            count = sum(1 for col in range(3) for row in range(3) if self.buttons[col][row]['text'] in (self.SYMBOL_X, self.SYMBOL_O))
            if count == 9:
                if messagebox.askyesno("Fin de partie", "Match Nul ! Inconcevable !"):
                    self.reset_game()
                else:
                    quit()

    def place_symbol(self, row, column):
        clicked_button = self.buttons[column][row]
        if clicked_button['text'] == "":
            clicked_button.config(text=self.current_player)
            self.check_win(row, column)
            self.switch_player()

    def draw_grid(self):
        for column in range(3):
            buttons_in_cols = []
            for row in range(3):
                button = tkinter.Button(
                    self.root, font=("Arial", 25),
                    width=10, height=4,
                    command=lambda r=row, c=column: self.place_symbol(r, c)
                )
                button.grid(row=row, column=column)
                buttons_in_cols.append(button)
            self.buttons.append(buttons_in_cols)

    def reset_game(self):
        for col in range(3):
            for row in range(3):
                self.buttons[col][row].config(text="")
        self.current_player = self.SYMBOL_X
        self.win = False

if __name__ == "__main__":
    root = tkinter.Tk()
    root.title("Morpion")
    tic_tac_toe_game = TicTacToe(root)
    root.mainloop()
