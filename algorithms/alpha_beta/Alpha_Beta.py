from Config import DEPTH

import chess
def find_move(board):
 
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