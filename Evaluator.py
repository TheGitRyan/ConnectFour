from Color import Color
import math

class Evaluator:
    """Evaluator that evaluates a board in Connect Four"""

    evaluationBoard = [[3, 4, 5, 7, 5, 4, 3],
                       [4, 6, 8, 10, 8, 6, 4],
                       [5, 8, 11, 13, 11, 8, 5],
                       [5, 8, 11, 13, 11, 8, 5],
                       [4, 6, 8, 10, 8, 6, 4],
                       [3, 4, 5, 7, 5, 4, 3]]

    def evaluateBoard(self, board):
        adjust = 138
        b = board
        sum = 0

        #If there is a four in a row determine who wins, these are represented by
        #mathematical infinity and negative infinity
        four_color = self.check_four_4s(board)
        if four_color is not Color.EMPTY:
            if four_color is board.color:
                return math.inf #this color just won the game
            elif four_color is not board.color:
                return -math.inf #this color just lost the game

        for i in range(b.row_count):
            for j in range(b.col_count):
                if b.pieceAt(i,j) is Color.BLACK :
                    sum += self.evaluationBoard[i][j]
                elif b.pieceAt(i,j) is Color.RED :
                    sum -= self.evaluationBoard[i][j]

        return adjust + sum

    def check_four_4s(self, board):
        b = board
        result_color = Color.EMPTY
        for i in range(b.row_count):
            for j in range(b.col_count):
                j = b.col_count - j

                result_color = self.check_up(i, j, board)
                if result_color != Color.EMPTY: return result_color

                result_color = self.check_down(i, j, board)
                if result_color != Color.EMPTY: return result_color

                result_color = self.check_left(i, j, board)
                if result_color != Color.EMPTY: return result_color

                result_color = self.check_right(i, j, board)
                if result_color != Color.EMPTY: return result_color

                result_color = self.check_up_left(i, j, board)
                if result_color != Color.EMPTY: return result_color

                result_color = self.check_up_right(i, j, board)
                if result_color != Color.EMPTY: return result_color

                result_color = self.check_down_right(i, j, board)
                if result_color != Color.EMPTY: return result_color

                result_color = self.check_down_left(i, j, board)
                if result_color != Color.EMPTY: return result_color

        return result_color

    def check_up(self, i, j, board):
        """Checks whether there is a four in a row in the upward"""
        color = board.pieceAt(i, j)

        row = True
        for k in range(4):
            row &= board.pieceAt(i-k, j) is color

        if row:
            return color
        else:
            return Color.EMPTY

    def check_down(self, i, j, board):
        """Checks whether there is a four in a row in the downward"""
        color = board.pieceAt(i, j)

        row = True
        for k in range(4):
            row &= board.pieceAt(i+k, j) is color

        if row:
            return color
        else:
            return Color.EMPTY

    def check_right(self, i, j, board):
        """Checks whether there is a four in a row in the rightward"""
        color = board.pieceAt(i, j)

        row = True
        for k in range(4):
            row &= board.pieceAt(i, j+k) is color

        if row:
            return color
        else:
            return Color.EMPTY

    def check_left(self, i, j, board):
        """Checks whether there is a four in a row in the leftward"""
        color = board.pieceAt(i, j)

        row = True
        for k in range(4):
            row &= board.pieceAt(i, j-k) is color

        if row:
            return color
        else:
            return Color.EMPTY

    def check_up_left(self, i, j, board):
        """Checks whether there is a four in a row in the upward left diagonal"""
        color = board.pieceAt(i, j)

        row = True
        for k in range(4):
            row &= board.pieceAt(i-k, j-k) is color

        if row:
            return color
        else:
            return Color.EMPTY

    def check_up_right(self, i, j, board):
        """Checks whether there is a four in a row in the upward right diagonal"""
        color = board.pieceAt(i, j)

        row = True
        for k in range(4):
            row &= board.pieceAt(i-k,j+k) is color

        if row:
            return color
        else:
            return Color.EMPTY

    def check_down_right(self, i, j, board):
        """Checks whether there is a four in a row in the downward right diagonal"""
        color = board.pieceAt(i, j)

        row = True
        for k in range(4):
            row &= board.pieceAt(i+k, j+k) is color

        if row:
            return color
        else:
            return Color.EMPTY

    def check_down_left(self, i, j, board):
        """Checks whether there is a four in a row in the downward left diagonal"""
        color = board.pieceAt(i, j)

        row = True
        for k in range(4):
            row &= board.pieceAt(i+k, j-k) is color

        if row:
            return color
        else:
            return Color.EMPTY
