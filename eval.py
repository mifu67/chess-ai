import chess

PIECES = [
    chess.PAWN,
    chess.KNIGHT,
    chess.BISHOP, 
    chess.ROOK, 
    chess.QUEEN, 
    chess.KING
    ]
        

class Eval():
    def __init__(self, input_board):
        self.board = input_board
        self.pieces_weights = [1, 1, 1, 1, 1, 1]
    
    # Param:: player_color - chess.COLOR of player, either chess.WHITE or chess.BLACK
    def simple_eval(self, player_color):
        count = 0
        for i in range(len(PIECES)):
            count += self.pieces_weights[i] * len(self.board.pieces(PIECES[i], player_color))
        return count

    


# Potential Features:
# detect if in check


