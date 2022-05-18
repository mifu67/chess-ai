import chess
from eval import Eval

# todo: potentially add board?
# minimax agent with alpha-beta pruning

#computer is 0, player is 1
class MinimaxAgent():

    """
      Returns the minimax action using self.depth and self.evaluationFunction
    """
    def __init__(self):
        self.isComputer = True
        self.evaluation_function = lambda: 1

    def get_move(self, board):
        def alphaBeta(board, isComputer, currDepth, alpha, beta):
            if board.is_end():
                return self.evaluation_function(board)
            elif currDepth == 0:
                return self.evaluation_function(board)
            else:

            legalMoves = board.legal_moves
            if self.isComputer:
                policy = ""
                maxValue = -math.inf
                for action in legalMoves:
                    consideredValue = alphaBeta(board.generateSuccessor(0, action), not isComputer, currDepth, alpha, beta)
                    if consideredValue > maxValue:
                        value = consideredValue
                        policy = action
                    alpha = max(alpha, value)
                    if beta <= alpha:
                        return (value, policy)
                #return the value and policy for the computer
                return (value, policy)

            else:
                policy = ""
                minValue = math.inf
                for action in legalMoves:
                    consideredValue = alphaBeta(board.generateSuccessor(1, action), not isComputer, currDepth, alpha,beta)
                    if consideredValue < minValue:
                        value = consideredValue
                        policy = action
                    beta = min(beta, value)
                    if beta <= alpha:
                        return (value, policy)
                # return the value and policy for the player
                return (value, policy)

        depth = 3
        value, action = alphaBeta(board, isComputer = True, depth, -float("inf"), float("inf"))
        print(value)
        return action
