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


def find_move(board, move):
    board.push(move)
    chosen_move = None
    moves = board.legal_moves()

    if board.turn():
        max_fit = -1000000
        for move in moves:
            board.push(move)
            move_fit = alpha_beta_pruning(board, DEPTH-1, board.turn(), -99999, 99999)
            if move_fit>max_fit:
                max_fit = move_fit
                chosen_move = move
            board.pop()
        return chosen_move

    else:
        min_fit = 1000000
        for move in moves:
            board.push(move)
            move_fit = alpha_beta_pruning(board, DEPTH-1, board.turn(), -99999, 99999)
            if move_fit<min_fit:
                min_fit = move_fit
                chosen_move = move
            board.pop()
        return chosen_move



# ---------  USE THREAD ----------------------> chua hoan thanh
# def mini_thread(board, moves, i, list):
#     print('on-thread')
#     board.push(moves[i])
#     move_fit = minimax(board, DEPTH-1, board.turn(), -99999, 99999)
#     list[i]=move_fit


# def find_move(board):
#     print('in-function')
#     chosen_move = None
#     moves = board.legal_moves()
#     moves_length = moves.count()
#     list = [0]*50
#     thread_list = [0]*50

#     if board.turn():
#         max_fit = -1000000
#         for i in range(moves_length):
#             thread_list[i] = threading.Thread(target=mini_thread, args=(dcopy(board), moves, i, list))
#             thread_list[i].start()
#         for i in range(moves_length):
#             thread_list[i].join()

#         print('out-thread')        
#         for i in range(moves_length):
#             if max_fit<list[i]:
#                 max_fit = list[i]
#                 chosen_move = moves[i]
        
#         return chosen_move

#     else:
#         min_fit = 1000000
#         for i in range(moves_length):
#             thread_list[i] = threading.Thread(target=mini_thread, args=(dcopy(board), moves, i, list))
#             thread_list[i].start()
#         for i in range(moves_length):
#             thread_list[i].join()
#         print('out-thread') 
#         for i in range(moves_length):
#             if min_fit>list[i]:
#                 min_fit = list[i]
#                 chosen_move = moves[i]
        
#         return chosen_move