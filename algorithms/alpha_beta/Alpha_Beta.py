from Config import DEPTH
# from threading import Thread
# import threading
# from copy import deepcopy as dcopy

def alpha_beta_pruning(board, depth, color, alpha, beta):

    moves = board.legal_moves()

    if color:
        new_beta = -999999
        for move in moves:
            board.push(move)
            if depth==1: fitness = board.fit()
            else:        fitness = alpha_beta_pruning(board, depth-1, False, alpha, beta)
            board.pop()
            if fitness>beta: return new_beta
            alpha = max(alpha,fitness)
            new_beta = max(fitness,new_beta)
        return new_beta

    else:
        new_alpha = 999999
        for move in moves:
            board.push(move)
            if depth==1: fitness = board.fit()
            else:        fitness = alpha_beta_pruning(board, depth-1, True, alpha, beta)
            board.pop()
            if fitness<alpha: return new_alpha
            beta = min(beta,fitness)
            new_alpha = min(fitness,new_alpha)
        return new_alpha


# def find_move(board, move):
#     if (move !='nomove'):
#         board.push(move)
#     chosen_move = None
#     moves = board.legal_moves()

#     if board.turn():
#         max_fit = -1000000
#         for move in moves:
#             board.push(move)
#             move_fit = alpha_beta_pruning(board, DEPTH-1, board.turn(), -99999, 99999)
#             if move_fit>max_fit:
#                 max_fit = move_fit
#                 chosen_move = move
#             board.pop()
#         return chosen_move

#     else:
#         min_fit = 1000000
#         for move in moves:
#             board.push(move)
#             move_fit = alpha_beta_pruning(board, DEPTH-1, board.turn(), -99999, 99999)
#             if move_fit<min_fit:
#                 min_fit = move_fit
#                 chosen_move = move
#             board.pop()
#         return chosen_move
import chess
def find_move(board,move):
    if (move !='nomove'):
        board.push(move)
    maximize = board.turn == chess.WHITE
    best_move = -float("inf")
    if not maximize: 
        best_move = float("inf")

    moves = board.legal_moves()
    best_move_found = None
    for move in moves:
        if (move !='nomove'):    
            board.push(move)   
        #value = alpha_beta_pruning(board, DEPTH-1, board.turn(), -float("inf"), float("inf"))
        value=minimax(DEPTH-1,board,-float("inf"),float("inf"),not maximize)
        board.pop()
        if maximize and value >= best_move:
            best_move = value
            best_move_found = move
        elif not maximize and value <= best_move:
            best_move = value
            best_move_found = move

    return best_move_found


def minimax(depth,board,alpha,beta, is_maximising_player) :
    if depth == 0:
        return board.evaluate_board()*(board.turn()*2-1)
    moves=board.legal_moves()
    if is_maximising_player:
        bestMove = -float("inf")
        for move in moves:
            board.push(move)
            bestMove=max(bestMove,minimax(depth-1,board,alpha,beta, not is_maximising_player))
            board.pop()
            alpha=max(alpha,bestMove)
            if beta <=alpha:
                return bestMove
        return bestMove
    else:
        bestMove = float("inf")
        for move in moves:
            board.push(move)
            bestMove=min(bestMove,minimax(depth-1,board,alpha,beta, not is_maximising_player))
            board.pop()
            beta=min(beta,bestMove)
            if beta <=alpha:
                return bestMove
        return bestMove
