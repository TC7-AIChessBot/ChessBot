# %%
import chess
import chess.engine
import os

# %%
os.system('chmod +x ./algorithms/stockfish/stockfish_14.1_linux_x64/stockfish_14.1_linux_x64')
engine = chess.engine.SimpleEngine.popen_uci(r"./algorithms/stockfish/stockfish_14.1_linux_x64/stockfish_14.1_linux_x64")


# %%
def find_move(board):
    result = engine.play(board.board, chess.engine.Limit(time=1))
    return result.move



