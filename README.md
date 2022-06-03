# Betta: a new chess AI
Welcome to Betta! This is a chess agent built to test the performance of different evaluation functions. Here's how to get started:

To run: you'll need to have Python and the python-chess module installed (run pip install chess to install python-chess). Clone this repository (in your terminal, type "git clone https://github.com/mifu67/chess-ai.git") and navigate to the folder in your terminal (if it's on your desktop, for instance, type "cd desktop/chess-ai"). Then, type "python (or python3) play-chess.py."

Pick your color and pick your evaluation function by following the prompts in the terminal. Here's what they do:
1. simple: sums up the pieces for each side according to their weighted values and returns computer sum - player sum
2. symm: does what simple does and additionally accounts for mobility and check status
3. placement: evaluates based on piece placement
4. combined: symm + placement (does everything, basically)

A couple notes:
- There could be a bug for you in the endgame where the program crashes when victory is near, due to a bug in the python-chess module. Rest assured that you were probably about to win.
- You can change the depth in minimax.py if you're feeling adventurous, but it'll get very slow at depths above 3.
- The board will always be shown from white's perspective, so apologies if you're playing black.
