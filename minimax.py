import chess
from eval import Eval

# minimax agent with alpha-beta pruning

#computer is 0, player is 1
class MinimaxAgent():
    """
      Returns the minimax action using self.depth and self.evaluationFunction
    """
    def __init__(self):
        self.isComputer = True
        #todo figure out a way to grab the player's color
        self.playerColor = chess.WHITE
        #self.evaluation_function = Eval.simple_eval(self, chess.WHITE)

    def get_move(self, board):
        def alphaBeta(board, isComputer, currDepth, alpha, beta):
            #todo figure out a way to check if chessboard is at the end
            if Chessboard.is_end():
                return Eval.evaluation_function(board, self.playerColor)
            elif currDepth == 0:
                return Eval.evaluation_function(board, self.playerColor)
            else:
                legalMoves = board.legal_moves
                if self.isComputer:
                    policy = ""
                    maxValue = -math.inf
                    for action in legalMoves:
                        consideredValue = alphaBeta(board.generateSuccessor(0, action), not isComputer, currDepth, alpha, beta)[0]
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
                        consideredValue = alphaBeta(board.generateSuccessor(1, action), not isComputer, currDepth, alpha,beta)[0]
                        if consideredValue < minValue:
                            value = consideredValue
                            policy = action
                        beta = min(beta, value)
                        if beta <= alpha:
                            return (value, policy)
                    # return the value and policy for the player
                    return (value, policy)

        depth = 3
        value, action = alphaBeta(board, True, depth, -float("inf"), float("inf"))
        print(value)
        return action
