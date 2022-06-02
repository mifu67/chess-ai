import chess
from eval import Eval
import math

# minimax agent with alpha-beta pruning
class MinimaxAgent:
    """
      Returns the minimax action using self.depth and self.evaluationFunction
    """
    def __init__(self, player_color, board, eval, quiesce):
        self.depth = 2
        self.board = board
        self.isComputer = True
        self.player_color = player_color
        self.evals = Eval(board)
        self.eval = eval
        self.quiesce_on = quiesce
    
    # order moves so that alpha-beta search is more likely to be effective
    def order_moves(self, movelist):
        for i in range(len(movelist)):
            if self.board.is_capture(movelist[i]):
                movelist.insert(0, movelist.pop(i))
        return movelist

    # pseudocode source: https://www.researchgate.net/figure/Abstract-Pseudo-Code-Version-for-Quiescence-Search-Forward-Pruning-technique-completes_fig6_262672371
    # to prevent the horizon effect, search until the position becomes "quiet" and there are no 
    # captures available (slightly modified to limit depth so that evaluation doesn't stall)
    def quiesce(self, alpha, beta, board, depth):
        if self.eval == "simple":
            eval = self.evals.simple_eval(self.player_color)
        elif self.eval == "placement":
            eval = self.evals.placement_eval(self.player_color)
        elif self.eval == "symm":
            eval = self.evals.symm_eval(self.player_color)
        elif self.eval == "attack":
            eval = self.evals.attacker_eval(self.player_color)
        elif self.eval == "combined":
            eval = self.evals.combined_eval(self.player_color)

        # depth-limited quiescense 
        if depth == 0:
            return eval

        if eval >= beta:
            return beta
        if alpha < eval:
            alpha = eval
        
        for move in board.legal_moves:
            if board.is_capture(move):
                board.push(move)
                score = -self.quiesce(-beta, -alpha, board, depth - 1)
                board.pop()
            
                if score >= beta:
                    return beta
                if score > alpha:
                    alpha = score
        return alpha


    def get_move(self):
        def alphaBeta(board, isComputer, currDepth, alpha, beta):
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

            # we've bottomed out, so call the eval function/quiesce
            elif currDepth == 0:
                if self.quiesce_on:
                    return self.quiesce(alpha, beta, board, 3)
                eval = 0
                if self.eval == "simple":
                    eval = self.evals.simple_eval(self.player_color)
                elif self.eval == "placement":
                    eval = self.evals.placement_eval(self.player_color)
                elif self.eval == "symm":
                    eval = self.evals.symm_eval(self.player_color)
                elif self.eval == "attack":
                    eval = self.evals.attacker_eval(self.player_color)
                elif self.eval == "combined":
                    eval = self.evals.combined_eval(self.player_color)
                return eval


            # minimax
            else:
                legalMoves = self.order_moves(list(board.legal_moves))
                if isComputer:
                    maxValue = -math.inf
                    for action in legalMoves:
                        board.push(action)
                        value = alphaBeta(board, not isComputer, currDepth - 1, alpha, beta)
                        board.pop()

                        maxValue = max(maxValue, value)
                        if maxValue >= beta:
                            break
                        alpha = max(alpha, maxValue)
                    return maxValue

                else:
                    minValue = math.inf
                    for action in legalMoves:
                        board.push(action)
                        value= alphaBeta(board, not isComputer, currDepth - 1, alpha,beta)
                        board.pop()

                        minValue = min(minValue, value)
                        if minValue <= alpha:
                            break
                        beta = min(beta, minValue)
                    return minValue

        legalMoves = self.order_moves(list(self.board.legal_moves))
        maxAction = ""
        maxValue = -math.inf
        alpha = -math.inf
        beta = math.inf
        for action in legalMoves:
            self.board.push(action)
            value = alphaBeta(self.board, not self.isComputer, self.depth, alpha, beta)
            self.board.pop()

            if value > maxValue:
                maxAction = action
                maxValue = value
                alpha = max(alpha, maxValue)

        return maxAction
