import chess
import random

PIECES = {
    "pawn": chess.PAWN,
    "knight": chess.KNIGHT, 
    "bishop": chess.BISHOP,
    "rook": chess.ROOK,
    "queen": chess.QUEEN,
    "king": chess.KING
}

# Joseph: you may want to make a minimax class, in which case you would pass it in here
# Daniela: we may want to make an eval class from which we can pull eval functions?
class Chessboard:
    def __init__(self):
        self.player_index = 0
        self.board = chess.Board()
    
    def display(self):
        print(self.board)
        print("")

    def move(self, is_player):
        legal_moves = self.board.legal_moves
        if is_player:
            move = self.get_move()
            while move not in legal_moves:
                print("Illegal move! Please try again.")
                move = self.get_move()
            self.board.push(move)
        else:
            # Joseph: your minimax will go here
            move_list = list(legal_moves)
            move = random.choice(move_list)
            self.board.push(move)
            print("Computer makes move:", move)
        self.display()

    # doesn't handle promotions yet... I think? It might 
    def get_move(self):
        # get a move
        move_info = input("Please enter your move in this format: (piece old_square new_square) ")
        move_info_list = move_info.split()
        while len(move_info_list) != 3:
            move_info = input("Invalid request. Please try again.")
            move_info_list = move_info.split()
        move = chess.Move.from_uci(move_info_list[1] + move_info_list[2])
        print(move)
        return move


    

