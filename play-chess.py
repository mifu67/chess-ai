from chessboard import Chessboard
import chess

# the chess game lives here
def main():
    board = Chessboard()
    # get the player's color
    agent_index = 0
    opp_index = 1
    val = input("Welcome to chess! Press '0' for white and '1' for black. ")
    while True:
        if val == '0': 
            print("Okay, you have the white pieces! ")
            break
        elif val == '1':
            print("Okay, you have the black pieces! ")
            agent_index = 1
            opp_index = 0
            break
        else:
            val = input("Invalid input: please type '0' or '1'. ")
    print("")
    board.display()

    # doesn't currently handle checkmate
    while True:
        if agent_index == 0:
            board.move(is_player=True)
            board.move(is_player=True) # this will be false but I'm moving both sides for debugging purposes
        else:
            board.move(is_player=True) # this will be false but I'm moving both sides for debugging purposes
            board.move(is_player=True)

if __name__ == "__main__":
    main()
