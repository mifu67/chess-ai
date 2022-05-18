from chessboard import Chessboard


# the chess game lives here
def main():
    board = Chessboard()
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
    print("")
    board.display()

    # off to the races! 
    while True:
        board.move(white)
        if board.is_end(): break
        board.move(black)
        if board.is_end(): break

if __name__ == "__main__":
    main()
