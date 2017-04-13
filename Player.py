from math import inf


class Player:
    look_ahead_depth = 3

    def __init__(self, level):
        self.look_ahead_depth = level

    def get_best_move(self, board, evaluator):
        m = self.alphabeta(board, evaluator, self.look_ahead_depth, -inf, inf)
        return m.move

    def alphabeta(self, board, evaluator, depth, alpha, beta):
        if depth == 0:
            m = BestMove(evaluator.evaluateBoard(board))
            return m
        else:
            next_moves = board.getNextMoves()
            if not next_moves:
                if board.color is board.win_color:
                    return BestMove(inf)
                else:
                    return BestMove(-inf)

        best_move = BestMove(-inf)
        for move in next_moves:
            board.makeMove(move.col)
            next = self.alphabeta(board, evaluator, depth - 1, -beta, -alpha)
            next.negate()
            next.move = move
            board.undoMove()

            if next.val > alpha:
                alpha = next.val
                best_move.val = next.val
                best_move.move = move

            if alpha >= beta:
                return best_move

        return best_move

    def minimax(self, board, evaluator, depth):
        if depth == 0:
            return BestMove(evaluator.evaluateBoard(board))

        next_moves = board.getNextMoves()

        best_move = BestMove(-inf)
        for move in next_moves:
            board.makeMove(move.col)
            next = self.minimax(board, evaluator, depth - 1)
            next.negate()
            next.move = move
            board.undoMove()
            if next is not None and next.val >= best_move.val:
                best_move.val = next.val
                best_move.move = move

        return best_move


class BestMove:
    move = None
    val = None

    def __init__(self, val):
        self.val = val

    def negate(self):
        self.val = -self.val
