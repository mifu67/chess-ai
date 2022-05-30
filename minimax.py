import chess
from eval import Eval
import math

# minimax agent with alpha-beta pruning
class MinimaxAgent:
    """
      Returns the minimax action using self.depth and self.evaluationFunction
    """
    def __init__(self, player_color, board):
        # setting an arbitrary number for testing
        self.depth = 3
        self.board = board
        self.isComputer = True
        self.player_color = player_color
        self.evals = Eval(board)

    def get_move(self):
        def alphaBeta(board, isComputer, currDepth, alpha, beta):
            # print("Board alpha beta:")
            # print(board)
            if board.is_game_over():
                outcome = board.outcome()
                # if the computer won
                if outcome.winner != self.player_color:
                    return math.inf
                # if the player won -> bad for computer
                elif outcome.winner == self.player_color:
                    return -math.inf
                # stalemate
                return 0

            # we've bottomed out, so call the eval function
            elif currDepth == 0:
                # print("Evaluation:", self.evals.placement_eval(self.player_color))
                return self.evals.placement_eval(self.player_color)

            # minimax
            else:
                legalMoves = list(board.legal_moves)
                if isComputer:
                    maxValue = -math.inf
                    for action in legalMoves:
                        # print("Move:", board.san(action))
                        board.push(action)
                        value = alphaBeta(board, not isComputer, currDepth - 1, alpha, beta)
                        # print("max considered:", value)
                        board.pop()
                        # print("Board after pop max:")
                        # print(board)
                        maxValue = max(maxValue, value)
                        if maxValue >= beta:
                            break
                        alpha = max(alpha, maxValue)
                        #print("alpha ", alpha)
                    return maxValue
                else:
                    minValue = math.inf
                    for action in legalMoves:
                        # print("Minimizer move:", board.san(action))
                        board.push(action)
                        value= alphaBeta(board, not isComputer, currDepth - 1, alpha,beta)
                        # print("min considered: ", value)
                        board.pop()
                        # print("Board after pop min:")
                        # print(board)
                        minValue = min(minValue, value)
                        if minValue <= alpha:
                            break
                        beta = min(beta, minValue)
                        #print("beta ", beta)
                    # print("min value:", minValue)
                    return minValue

        #beginning of get_moves
        legalMoves = self.board.legal_moves
        maxAction = ""
        maxValue = -math.inf
        alpha = -math.inf
        beta = math.inf
        for action in legalMoves:
            # print("Maximizer move:", self.board.san(action))
            self.board.push(action)
            value = alphaBeta(self.board, not self.isComputer, self.depth, alpha, beta)
            self.board.pop()
            if value > maxValue:
                maxAction = action
                # print("new max value:", value)
                maxValue = value
                # if alpha == float("inf"):
                    # print("infinite alpha found")
                # print("alpha before",  alpha)
                alpha = max(alpha, maxValue)
                # print("alpha", alpha)

        # print("maxValue ", maxValue)
        return maxAction
