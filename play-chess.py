from chessboard import Chessboard
import chess



# the chess game lives here
def main():
    # get the player's color
    white = True
    black = False
    val = input("Welcome to chess! Type 'white' to play white and 'black' to play black. ")
    while True:
        if val == 'white': 
            print("Okay, you have the white pieces!")
            break
        elif val == 'black':
            print("Okay, you have the black pieces!")
            white = False
            black = True
            break
        else:
            val = input("Invalid input: please type 'white' or 'black'. ")
    eval = input("Enter and evaluation function: simple, symm, placement, attack, or combined. ")
    while True:
        if eval != "simple" and eval != "symm" and eval != "placement" and eval != "combined" and eval != "attack":
            eval = input("Please enter a valid evaluation function.")
        else:
            break
    quiesce = False
    quiesce_val = input("Do you want to enable quiescence search? Type 'yes' or 'no'. ")
    while True:
        if quiesce_val == 'yes':
            quiesce = True
            break
        if quiesce_val == 'no':
            break
        else:
            quiesce_val = input("Please enter 'yes' or 'no'. ")
    print("Let's get started!")
    print("")

    player_color = chess.WHITE if white else chess.BLACK
    board = Chessboard(player_color, eval, quiesce)
    board.display()

    # off to the races! 
    while True:
        board.move(white)
        if board.is_end(): break
        board.move(black)
        if board.is_end(): break

if __name__ == "__main__":
    main()
