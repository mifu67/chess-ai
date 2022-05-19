import chess

PIECES = [
    chess.PAWN,
    chess.KNIGHT,
    chess.BISHOP,
    chess.ROOK,
    chess.QUEEN,
    chess.KING
]

pst_pawn = [0,   0,   0,   0,   0,   0,   0,   0,
            78,  83,  86,  73, 102,  82,  85,  90,
             7,  29,  21,  44,  40,  31,  44,   7,
           -17,  16,  -2,  15,  14,   0,  15, -13,
           -26,   3,  10,   9,   6,   1,   0, -23,
           -22,   9,   5, -11, -10,  -2,   3, -19,
           -31,   8,  -7, -37, -36, -14,   3, -31,
             0,   0,   0,   0,   0,   0,   0,   0
]

pst_knight = [-66, -53, -75, -75, -10, -55, -58, -70,
            -3,  -6, 100, -36,   4,  62,  -4, -14,
            10,  67,   1,  74,  73,  27,  62,  -2,
            24,  24,  45,  37,  33,  41,  25,  17,
            -1,   5,  31,  21,  22,  35,   2,   0,
           -18,  10,  13,  22,  18,  15,  11, -14,
           -23, -15,   2,   0,   2,   0, -23, -20,
           -74, -23, -26, -24, -19, -35, -22, -69
]

pst_bishop= [-59, -78, -82, -76, -23,-107, -37, -50,
           -11,  20,  35, -42, -39,  31,   2, -22,
            -9,  39, -32,  41,  52, -10,  28, -14,
            25,  17,  20,  34,  26,  25,  15,  10,
            13,  10,  17,  23,  17,  16,   0,   7,
            14,  25,  24,  15,   8,  25,  20,  15,
            19,  20,  11,   6,   7,   6,  20,  16,
            -7,   2, -15, -12, -14, -15, -10, -10
]

pst_rook = [35,  29,  33,   4,  37,  33,  56,  50,
            55,  29,  56,  67,  55,  62,  34,  60,
            19,  35,  28,  33,  45,  27,  25,  15,
             0,   5,  16,  13,  18,  -4,  -9,  -6,
           -28, -35, -16, -21, -13, -29, -46, -30,
           -42, -28, -42, -25, -25, -35, -26, -46,
           -53, -38, -31, -26, -29, -43, -44, -53,
           -30, -24, -18,   5,  -2, -18, -31, -32
]

pst_queen = [6,   1,  -8,-104,  69,  24,  88,  26,
            14,  32,  60, -10,  20,  76,  57,  24,
            -2,  43,  32,  60,  72,  63,  43,   2,
             1, -16,  22,  17,  25,  20, -13,  -6,
           -14, -15,  -2,  -5,  -1, -10, -20, -22,
           -30,  -6, -13, -11, -16, -11, -16, -27,
           -36, -18,   0, -19, -15, -15, -21, -38,
           -39, -30, -31, -13, -31, -36, -34, -42]

pst_king = [4,  54,  47, -99, -99,  60,  83, -62,
           -32,  10,  55,  56,  56,  55,  10,   3,
           -62,  12, -57,  44, -67,  28,  37, -31,
           -55,  50,  11,  -4, -19,  13,   0, -49,
           -55, -43, -52, -28, -51, -47,  -8, -50,
           -47, -42, -43, -79, -64, -32, -29, -32,
            -4,   3, -14, -50, -57, -18,  13,   4,
            17,  30,  -3, -14,   6,  -1,  40,  18
]


flip = [
  56, 57, 58, 59, 60, 61, 62, 63,
  48, 49, 50, 51, 52, 53, 54, 55,
  40, 41, 42, 43, 44, 45, 46, 47,
  32, 33, 34, 35, 36, 37, 38, 39,
  24, 25, 26, 27, 28, 29, 30, 31,
  16, 17, 18, 19, 20, 21, 22, 23,
  8, 9, 10, 11, 12, 13, 14, 15,
  0, 1, 2, 3, 4, 5, 6, 7
]


class Eval:

    def __init__(self, input_board):
        self.board = input_board
        # Weighted according to chess.com
        self.pieces_weights = [10, 30, 30, 50, 90, 900]
        self.mobility_weight = 5
        self.check_weight = -10000


    # Param:: player_color - chess.COLOR of player, either chess.WHITE or chess.BLACK
    def simple_eval(self, player_color):
        my_count = 0
        opp_count = 0
        for i in range(len(PIECES)):
            my_count += self.pieces_weights[i] * len(self.board.pieces(PIECES[i], player_color))
            opp_count += self.pieces_weights[i] * len(self.board.pieces(PIECES[i], not player_color))
        return my_count - opp_count

    # Based on Claude E. Shannon's "Programming a Computer for playing Chess" 1949
    def symm_eval(self, player_color):
        # Count difference
        score = 0
        for i in range(len(PIECES)):
            score += self.pieces_weights[i] * (len(self.board.pieces(PIECES[i], player_color)) - 
                                                len(self.board.pieces(PIECES[i], not player_color)))
        # Mobility measured by number of legal moves available
        mobility = self.mobility_weight * (len(self.board.legal_moves))

        # Checks if board is currently in check
        check = self.check_weight * (1 if self.board.is_check() else 0)

        return score + mobility + check

    # Weighs pieces based on placement on board
    # From https://github.com/emdio/secondchess/blob/master/secondchess.c
    def placement_eval(self, player_color):
        score = 0
        
        for i in range(64):
            piece = self.board.piece_at(i)
            if self.board.color_at(i) == chess.WHITE:
                if piece == chess.PAWN:
                    score += pst_pawn[i]
                elif piece == chess.KNIGHT:
                    score += pst_knight[i]
                elif piece == chess.BISHOP:
                    score += pst_bishop[i]
                elif piece == chess.ROOK:
                    score += pst_rook[i]
                elif piece == chess.QUEEN:
                    score += pst_queen[i]
                elif piece == chess.KING:
                    score += pst_king[i]
            elif self.board.color_at(i) == chess.BLACK:
                if piece == chess.PAWN:
                    score -=pst_pawn[flip[i]]
                elif piece == chess.KNIGHT:
                    score -= pst_knight[flip[i]]
                elif piece == chess.BISHOP:
                    score -= pst_bishop[flip[i]]
                elif piece == chess.ROOK:
                    score -= pst_rook[flip[i]]
                elif piece == chess.QUEEN:
                    score -= pst_queen[flip[i]]
                elif piece == chess.KING:
                    score -= pst_king[flip[i]]
        return score if (player_color == chess.WHITE) else -score

        




