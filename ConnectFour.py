from Board import Board
from Color import Color
from Player import Player
from Evaluator import Evaluator

# this is a console text version of connect four

board = Board()
board.printB()
AI_one = Player(3)
AI_two = Player(5)

run_game = True
while run_game:
    #prompt for move
    #player_move = input('move: ')

    if input is "quit" :
        run_game = False
    else:
        try:
            col = 0 #int(player_move)

            if not 0 <= col < board.col_count:
                raise ValueError
            else:
                #board.makeMove(col)
                AI_one_move = AI_one.get_best_move(board, Evaluator())
                if AI_one_move is None:
                    run_game = False
                    board.printB()
                    print("It's a tie!")
                    break
                board.makeMove(AI_one_move.col)

                if Evaluator().check_four_4s(board) is Color.RED :
                    run_game = False
                    board.printB()
                    print("You Win!")
                    break
                board.printB()

                AI_two_move = AI_two.get_best_move(board, Evaluator())
                board.makeMove(AI_two_move.col)

                if Evaluator().check_four_4s(board) is Color.BLACK :
                    run_game = False
                    board.printB()
                    print("You Lose!")
                    break
                board.printB()

        except ValueError:
            print("invalid move")



