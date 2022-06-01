from stockfish import Stockfish
import os

NUM_MOVES = 30 

def main():
    stockfish = Stockfish(r"C:\Users\Daniela Uribe\Documents\Stanford\CS221\stockfish-11-win\Windows\stockfish_20011801_x64.exe")
    directory = "fenData"
    
    with open('stockfish-moves.txt', 'a') as f:
        f.write("test")
    f.close()

    for file_name in os.listdir(directory):
        file_path = os.path.join(directory, file_name)
        if os.path.isfile(file_path):
            with open(file_path) as pgn_file:
                lines = pgn_file.readlines()

                for fen in lines:
                    stockfish.set_fen_position(fen.strip())
                    best_n_moves = stockfish.get_top_moves(NUM_MOVES)
                    moves_string = ""

                    for move in best_n_moves:
                        moves_string += move['Move'] + " "
                    print(moves_string)
                    moves_string += '\n'

                    
                    with open('stockfish-moves.txt', 'a') as f:
                        f.write(moves_string)

                        
if __name__ == "__main__":
    main()