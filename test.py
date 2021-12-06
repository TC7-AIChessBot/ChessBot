import chess

board = chess.Board()

print(list(board.legal_moves)[0].uci())

