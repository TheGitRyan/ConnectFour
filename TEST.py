from Board import Board
from Evaluator import Evaluator
from Player import Player

board = Board()
player = Player(4)
eva = Evaluator()

board.makeMove(3) # red
board.makeMove(3) # yellow
board.makeMove(6) # red
board.makeMove(3) # yellow
board.makeMove(5) # red
#board.makeMove(3) # yellow
#board.makeMove(4) # red wins 4 in a row 4 -> 7 in bottom row

#print(board.win_color)

move = player.get_best_move(board,eva)

board.printB()

print(move)


