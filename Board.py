from Color import Color
from Evaluator import Evaluator

class Move:
    row = None
    col = None

    def __init__(self, row, col):
        self.row = row
        self.col= col

    def __repr__(self):
        return "(" + str(self.col) + ", " + str(5 - self.row) + ")"

    def equals(self, other):
        return self.row is other.row and self.col is other.col

    def get_sig(self):
        #return the move signature in the form of an int 10*row + col
        #since row,col < 10 this will alwyas be a unique indicator for the cell
        return 10*self.row + self.col

class Board:
    """board class with 2 dimensional array"""
    row_count = 6
    col_count = 7
    board = [[]]
    evaluator = Evaluator()

    color = Color.RED  # color of current player, red goes first
    win_color = Color.EMPTY

    # stack that keeps all the moves played on the board so they can be added in
    # or popped off, to simulate different board states
    history = []

    def __init__(self):
        self.board = [[Color.EMPTY for x in  range(self.col_count)] for y in range(self.row_count)]

    def flip_color(self):
        if self.color is Color.BLACK:
            self.color = Color.RED
        elif self.color is Color.RED:
            self.color = Color.BLACK

    def refresh_win(self):
        self.win_color = self.evaluator.check_four_4s(self)

    def pieceAt(self, row, col):
        if 0 <= row < self.row_count and 0 <= col < self.col_count:
            return self.board[row][col]
        else:
            return Color.EMPTY

    #Changing the value of a cell at a certain index
    def setPiece(self, row, col, val):
        if val is Color.BLACK or val is Color.RED :
            self.board[row][col] = val

    #Changing the value of a cell at a certain index
    def removePiece(self, row, col):
        self.board[row][col] = Color.EMPTY

    #Choose a column, and return the move the cell that would be filled by dropping
    #a token there
    def getMove(self, col):
        # determine the first open space in that column
        b = self.board
        openSpot = -1
        for i in range(self.row_count):
            idx = self.row_count - 1 - i
            if b[idx][col] is Color.EMPTY:
                openSpot = idx
                break

        # if openSpot == -1 then there are no open spots in this column
        # so this is an invalid move
        if openSpot == -1:
            return None  # value indicating invalid move
        else:
            return Move(openSpot, col)  # value indicating valid move

    #Choose a column to drop a piece into
    def makeMove(self, col):
        m = self.getMove(col)
        if m is not None:
            self.setPiece(int(m.row), int(m.col), self.color)
            self.history.append(m)
            self.flip_color()
            self.refresh_win()
        return m

    #removes a move from the
    def undoMove(self):
        m = self.history.pop()
        self.removePiece(m.row, m.col)
        self.flip_color()
        return m

    def printB(self):
        line = "-"
        for i in range(self.row_count + 1):
            line += "----"

        print(" ", end="")
        for i in range(self.col_count): print(" " + str(i) + "  ", end="")
        print("")
        for i in range(self.row_count):
            print("| ", end="")
            for j in range(self.col_count):
                val = " "
                if self.board[i][j].value == 1:
                    val = "R"
                elif self.board[i][j].value == 2:
                    val = "B"

                print(val + " | ", end=""),

            print("\n" + line)

    def copy(self):
        newBoard = Board()
        for i in range(self.row_count):
            for j in range(self.col_count):
                newBoard.board[i][j] = self.board[i][j]
        return newBoard

    def getNextMoves(self):
        nextMoves = []
        if self.win_color is Color.EMPTY: # i.e. no one has won yet
            for i in range(self.col_count):
                move = self.getMove(i)
                if move is not None:
                    nextMoves.append(move)

        return nextMoves



