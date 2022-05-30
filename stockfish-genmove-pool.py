import multiprocessing
from stockfish import Stockfish
from genfen import GenerateFen
import chess
from minimax import MinimaxAgent
import os


class GenMoveStockFish:
    def __init__(self, directory):
        self.directory = directory
        self.fileNames = []
        self.accuracy = 0
        self.numMovesGen = 30
        self.listFolders()
        
    def listFolders(self):
         for fileName in os.listdir(self.directory):
            filePath = os.path.join(self.directory, fileName)
            self.fileNames.append(filePath)

    """
    testMinimax

    Param: numMovesGen- int number of top moves to generate with StockFish

    Tests minimax move prediction against StockFish. StockFish will generate numMovesGen top moves
    to compare to minimax's prediction. Outputs the percentage correct for all fen board arrangements.
    Returns float percentage of moves minimax guesses correctly from numMovesGen top moves predicted by StockFish
    """
    def testMinimax(self, filePath):
        stockfish = Stockfish()

        #stockfish.set_depth(2)


        total_fen = 0
        moves_matched = [0] * int(self.numMovesGen / 2)

        if os.path.isfile(filePath):
            with open(filePath) as pgn_file:
                lines = pgn_file.readlines()
                for fen in lines:
                    total_fen += 1
                    print("Fen count {}".format(total_fen))
                    fen_split = fen.split(' ') 
                    # Create chess board with fen
                    minimax_board = chess.Board(fen.strip())
                    # Predict next move with minimax
                    player_color = chess.BLACK if fen_split[-5] == 'w' else chess.WHITE
                    # Gen minimax move
                    minimax_agent = MinimaxAgent(player_color, minimax_board)
                    minimax_move = minimax_agent.get_move()
                    #print("minimax_move " + str(minimax_move))
                    #print("minimax_move " + minimax_board.san(minimax_move))

                    #Gen top moves Stockfish
                    stockfish.set_fen_position(fen.strip())
                    best_n_moves = stockfish.get_top_moves(self.numMovesGen)

                    #print(len(best_n_moves))

                    # Extract match counts within top moves
                    move_found = False
                    for i in range(2, self.numMovesGen + 1, 2):
                        if move_found:
                            moves_matched[int((i-1)/2)] += 1
                            continue
                        for j in range (i-2, i):
                            if j < len(best_n_moves):
                                if str(best_n_moves[j]['Move']) == str(minimax_move):
                                   
                                    moves_matched[int((j)/2)] += 1
                                    move_found = True
                                    break
                        
                                    
        return (moves_matched)
        
                        


def main():
    genMoves = GenMoveStockFish("fenData")
        
    print("Testing numMovesGen = {num}".format(num = genMoves.numMovesGen))

    pool = multiprocessing.Pool()
    result = []
    try:
        result = pool.map(genMoves.testMinimax, genMoves.fileNames)
    except KeyboardInterrupt:
        pool.terminate()
        pool.join()

    total_moves_matched = [0] * int(genMoves.numMovesGen / 2)
    final_fen_total = 300
    
    for i in range(len(total_moves_matched)):
        for move_counts in result:
            total_moves_matched[i] += move_counts[i]
    
    for  i in range(len(total_moves_matched)):
        print("Moves Generated: {moves}".format(moves = (i+1)*2))
        print("Accuracy: {percent}%".format(percent = float(total_moves_matched[i]/final_fen_total * 100)) if final_fen_total else "Fen Total is zero")
    

if __name__ == "__main__":
    main()