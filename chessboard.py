import chess


class Chessboard:
    def __init__(self):
        self.player_index = 0

    def run(self):
        # initialize the board
        board = chess.Board(chess.STARTING_BOARD_FEN)
        print(board)

