import chess
from eval import Eval

# todo: potentially add board? 
# minimax agent with alpha-beta pruning

#computer is 0, player is 1
class MinimaxAgent():
    
    """
      Returns the minimax action using self.depth and self.evaluationFunction
    """
    def get_move(self, board):

        def alphaBeta(board, currPlayer, currDepth, alpha, beta):
            legalMoves = board.legal_moves

            #if loss neg infinity, if win, infinity

            if currDepth == 0:
                return self.evaluationFunction(board)

            #the computer aims to maximize
            if currPlayer = "computer":

            #the human aims to minimize
            if currPlayer = "human":


            # this needs to change
            nextDepth = currDepth - 1 if currPlayer == "black" else currDepth

    
        
            minValue = math.inf
            for action in legalMoves:
                succ = gameState.generateSuccessor(currIndex, action)
                minValue = min(minValue, alphaBeta(succ, nextIndex, nextDepth, alpha, beta))
                if minValue <= alpha:
                    break
                beta = min(beta, minValue)
            return minValue

        legalMoves = gameState.getLegalActions(self.index)
        maxAction = ""
        maxValue = -math.inf
        alpha = -math.inf
        beta = math.inf
        for action in legalMoves:
            value = alphaBeta(gameState.generateSuccessor(self.index, action), self.index + 1, self.depth, alpha, beta)
            if value > maxValue:
                maxAction = action
                maxValue = value
                alpha = max(alpha, maxValue)
        # print("alpha-beta value:", maxValue)



        return action
