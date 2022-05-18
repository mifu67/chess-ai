import chess
import random
from minimax import MinimaxAgent

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
        self.minimaxagent = MinimaxAgent()
    
    # print out the board
    def display(self):
        print(self.board)
        print("")

    # make a move:
    def move(self, is_player):
        legal_moves = self.board.legal_moves
        if is_player:
            move = self.get_move()
            self.board.push(move)
        else:
            # Joseph: your minimax will go here
            move_list = list(legal_moves)
            move = random.choice(move_list)
            print("Computer makes move:", self.board.san(move))
            self.board.push(move)
        self.display()

    # doesn't handle promotions yet... I think? It might 
    def get_move(self):
        # get a move
        move_input = input("Please enter your move in standard algebraic notation. Type 'help' for examples: ")
        if move_input.strip() == "help":
            print("e4, Nf3, Qxb4, bxc6, 0-0, Nfd2")
        while True:
            try:
                move = self.board.parse_san(move_input.strip())
                break
            except ValueError:
                move_input = input("Oops, that input was illegal. Please try again. ")
        print(self.board.san(move))
        return move
    
    def is_end(self):
        if self.board.is_game_over():   
            # Will need to clean this up
            print(self.board.outcome())
            return True
        # else
        return False

    

