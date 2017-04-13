from tkinter import *
from tkinter import ttk
from Player import *
from Evaluator import *
from Board import Board

# a gui version of connect four

class GuiBoard:

    def __init__(self, gui):
        self.board = Board()
        self.board_frame = ttk.Frame(gui.root)
        self.refresh_gui_board()
        self.board_frame.grid(row=1, column=0, rowspan=6, columnspan=7)

    def refresh_gui_board(self):
        for i in range(self.board.row_count):
            for j in range(self.board.col_count):
                color_photo = PhotoImage(file="empty.gif")
                if self.board.pieceAt(i,j) is Color.RED:
                    color_photo = PhotoImage(file="red.gif")
                elif self.board.pieceAt(i,j) is Color.BLACK:
                    color_photo = PhotoImage(file="yellow.gif")

                color_photo = color_photo.subsample(10)

                cell_label = Label(image=color_photo, master=self.board_frame, width=100, height=100, borderwidth=1)
                cell_label.image = color_photo

                cell_label.grid(row=i, column=j)


class GUI:

    def __init__(self):
        self.root = Tk()
        self.gui_board = GuiBoard(self)
        self.root.wm_title("Connect Four!")

        # Player and the playing depth
        self.player = Player(4)

        self.button_1 = ttk.Button(self.root, text="1", command = lambda: self.gui_make_move(0))
        self.button_2 = ttk.Button(self.root, text="2", command = lambda: self.gui_make_move(1))
        self.button_3 = ttk.Button(self.root, text="3", command = lambda: self.gui_make_move(2))
        self.button_4 = ttk.Button(self.root, text="4", command = lambda: self.gui_make_move(3))
        self.button_5 = ttk.Button(self.root, text="5", command = lambda: self.gui_make_move(4))
        self.button_6 = ttk.Button(self.root, text="6", command = lambda: self.gui_make_move(5))
        self.button_7 = ttk.Button(self.root, text="7", command = lambda: self.gui_make_move(6))

        self.button_1.grid(column=0, row=0)
        self.button_2.grid(column=1, row=0)
        self.button_3.grid(column=2, row=0)
        self.button_4.grid(column=3, row=0)
        self.button_5.grid(column=4, row=0)
        self.button_6.grid(column=5, row=0)
        self.button_7.grid(column=6, row=0)

    def gui_make_move(self, move):
        self.gui_board.board.makeMove(move)

        if self.gui_board.board.win_color is Color.BLACK:
            self.gui_board.refresh_gui_board()
            lose_frame = Tk()
            lose_label = Label(lose_frame, text="You Lose! D:", width=10, height=10)
            lose_label.pack(side=TOP)
        elif self.gui_board.board.win_color is Color.RED:
            self.gui_board.refresh_gui_board()
            win_frame = Tk()
            win_label = Label(win_frame, text="You Win! :D", width=10, height=10)
            win_label.pack(side=TOP)
        elif not self.gui_board.board.getNextMoves():
            print("----------------------------------------------------------------------")
            self.gui_board.refresh_gui_board()
            tie_frame = Tk()
            tie_label = Label(tie_frame, text="It's a tie! :|", width=10, height=10)
            tie_label.pack(side=TOP)

        self.gui_board.refresh_gui_board()

    def AI_check(self):
        if self.gui_board.board.color is Color.BLACK:
            # signifying it is the AI's turn to play
            AI_move = self.player.get_best_move(self.gui_board.board, Evaluator())
            self.gui_make_move(AI_move.col)

        self.root.after(2000, self.AI_check)

    def run_game(self):
        self.root.after(2000, self.AI_check)
        self.root.mainloop()

if __name__ == '__main__':
    GUI().run_game()