#from .Config import DEPTH

import chess
def find_move(board):
    if board.count_pieces()>7: DEPTH= 3
    else: DEPTH=5
    
    print('Số quân: {}, độ sâu: {}'.format(board.count_pieces, DEPTH))
    
    score_color = board.turn()
    maximize = board.turn == chess.WHITE
    best_move = -float("inf")
    if not maximize: 
        best_move = float("inf")

    moves = board.legal_moves()
    best_move_found = None
    for move in moves:
        if (move !='nomove'):    
            board.push(move)   
        value=alpha_beta_pruning(DEPTH-1,board,-float("inf"),float("inf"),not maximize, score_color)
        board.pop()
        if maximize and value >= best_move:
            best_move = value
            best_move_found = move
        elif not maximize and value <= best_move:
            best_move = value
            best_move_found = move

    return best_move_found


def alpha_beta_pruning(depth,board,alpha,beta, is_maximising_player, score_color) :
    if depth == 0:
        return - board.evaluate_board()* (score_color * 2 - 1)
    moves=board.legal_moves()
    if is_maximising_player:
        bestMove = -float("inf")
        for move in moves:
            board.push(move)
            bestMove=max(bestMove,alpha_beta_pruning(depth-1,board,alpha,beta, not is_maximising_player, score_color))
            board.pop()
            alpha=max(alpha,bestMove)
            if beta <=alpha:
                return bestMove
        return bestMove
    else:
        bestMove = float("inf")
        for move in moves:
            board.push(move)
            bestMove=min(bestMove,alpha_beta_pruning(depth-1,board,alpha,beta, not is_maximising_player, score_color))
            board.pop()
            beta=min(beta,bestMove)
            if beta <=alpha:
                return bestMove
        return bestMove