import chess

PIECES = [
    chess.PAWN,
    chess.KNIGHT,
    chess.BISHOP,
    chess.ROOK,
    chess.QUEEN,
    chess.KING
]


class Eval:

    def __init__(self, input_board):
        self.board = input_board
        # Weighted according to chess.com
        self.pieces_weights = [10, 30, 30, 50, 90, 900]


    # Param:: player_color - chess.COLOR of player, either chess.WHITE or chess.BLACK
    def simple_eval(self, player_color):
        my_count = 0
        opp_count = 0
        for i in range(len(PIECES)):
            my_count += self.pieces_weights[i] * len(self.board.pieces(PIECES[i], player_color))
            opp_count += self.pieces_weights[i] * len(self.board.pieces(PIECES[i], not player_color))
        return my_count - opp_count


