import chess

PIECES = {
    "pawn": chess.PAWN,
    "knight": chess.KNIGHT, 
    "bishop": chess.BISHOP,
    "rook": chess.ROOK,
    "queen": chess.QUEEN,
    "king": chess.KING
}

class Eval():
    def __init__(self, input_board):
        self.board = chess.Board()
    
    # Param:: player_color - chess.COLOR of player, either chess.WHITE or chess.BLACK
    def simple_eval(self, player_color):
        count = 0
        for piece in PIECES.values():
            count += len(self.board.pieces(piece, player_color))
        return count

    


# Potential Features:
# detect if in check


