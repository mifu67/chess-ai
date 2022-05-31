import chess
import random
from minimax import MinimaxAgent
from eval import Eval

PIECES = {
    "pawn": chess.PAWN,
    "knight": chess.KNIGHT, 
    "bishop": chess.BISHOP,
    "rook": chess.ROOK,
    "queen": chess.QUEEN,
    "king": chess.KING
}

class Chessboard:
    def __init__(self, player_color):
        self.board = chess.Board()
        self.minimaxagent = MinimaxAgent(player_color, self.board)
        self.player_color = player_color
    
    # print out the board
    def display(self):
        display = self.render(self.board)
        print(display)
        # print(self.board)
        print("")
    
    # Attribution: adapted from https://github.com/healeycodes/andoma/blob/main/ui.py
    def render(self, board: chess.Board) -> str:
        """
        Print a side-relative chess board with special chess characters.
        Currently only works if you're playing white, oops
        """
        board_string = list(str(board))
        # admittedly this looks a little odd on dark mode...
        uni_pieces = {
            "R": "♖",
            "N": "♘",
            "B": "♗",
            "Q": "♕",
            "K": "♔",
            "P": "♙",
            "r": "♜",
            "n": "♞",
            "b": "♝",
            "q": "♛",
            "k": "♚",
            "p": "♟",
            ".": "·",
        }
        for idx, char in enumerate(board_string):
            if char in uni_pieces:
                board_string[idx] = uni_pieces[char]
        ranks = ["1", "2", "3", "4", "5", "6", "7", "8"]
        # if self.player_color == chess.BLACK:
            # ranks = ["8", "7", "6", "5", "4", "3", "2", "1"]
        display = []
        for rank in "".join(board_string).split("\n"):
            display.append(f"  {ranks.pop()} {rank}")
        # if board.turn == chess.BLACK:
            # display.reverse()
        files = "    a b c d e f g h"
        # if self.player_color == chess.BLACK:
            # files = "    h g f e d c b a"
        display.append(files)
        return "\n" + "\n".join(display)

    # make a move:
    def move(self, is_player):

        if is_player:
            move = self.get_move()
            self.board.push(move)
        else:
            move = self.minimaxagent.get_move()

            print("Computer makes move:", self.board.san(move))
            self.board.push(move)
            
        self.display()

    def get_move(self):
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

    

