from stockfish import Stockfish
from genfen import GenerateFen
import chess
from minimax import MinimaxAgent
import os


class GenMoveStockFish:
    def __init__(self, directory):
        self.directory = directory
        self.accuracy = 0
        
    """
    testMinimax

    Param: numMovesGen- int number of top moves to generate with StockFish

    Tests minimax move prediction against StockFish. StockFish will generate numMovesGen top moves
    to compare to minimax's prediction. Outputs the percentage correct for all fen board arrangements.
    Returns float percentage of moves minimax guesses correctly from numMovesGen top moves predicted by StockFish
    """
    def testMinimax(self, numMovesGen):
        stockfish = Stockfish(r'C:\Users\Daniela Uribe\Documents\Stanford\CS221\stockfish-11-win\Windows\stockfish_20011801_x64.exe')

        total_fen = 0
        moves_matched = 0

        for fileName in os.listdir(self.directory):
            filePath = os.path.join(self.directory, fileName)
            if os.path.isfile(filePath):
                with open(filePath) as pgn_file:
                    lines = pgn_file.readlines()
                    for fen in lines:
                        total_fen += 1

                        fen_split = fen.split(' ') 
                        # Create chess board with fen
                        minimax_board = chess.Board(fen.strip())
                        # Predict next move with minimax
                        player_color = chess.WHITE if fen_split[-5] == 'w' else chess.BLACK
                        print(player_color)
                        minimax_agent = MinimaxAgent(player_color, minimax_board)
                        minimax_move = minimax_agent.get_move()
                        print("minimax_move " + str(minimax_move))

                        stockfish.set_fen_position(fen.strip())
                        best_n_moves = stockfish.get_top_moves(numMovesGen)

                        for move in best_n_moves:
                            print("stockfish move = " + str(move))
                            if move['Move'] == minimax_move:
                                moves_matched += 1

        return "Accuracy: {percent}%".format(percent = float(moves_matched/total_fen * 100))
        
                        


def main():
    genMoves = GenMoveStockFish("fenData")
    print(genMoves.testMinimax(3))
    


if __name__ == "__main__":
    main()