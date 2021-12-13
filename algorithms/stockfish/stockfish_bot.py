# %%
import chess
import chess.engine
import os
from sys import platform as platform

# %%
if platform == "linux" or platform == "linux2":
    os.system('chmod +x ./algorithms/stockfish/stockfish_14.1_linux_x64')
    engine = chess.engine.SimpleEngine.popen_uci(r"./algorithms/stockfish/stockfish_14.1_linux_x64")
elif platform == "win32":
    os.system('chmod +x ./algorithms/stockfish/stockfish_14.1_win_32bit.exe')
    engine = chess.engine.SimpleEngine.popen_uci(r"./algorithms/stockfish/stockfish_14.1_win_32bit.exe")
elif platform == "win64":
    os.system('chmod +x ./algorithms/stockfish/stockfish_14.1_win_x64.exe')
    engine = chess.engine.SimpleEngine.popen_uci(r"./algorithms/stockfish/stockfish_14.1_win_x64.exe")
# elif platform == "darwin":
#     # MAC OS X

# %%
def find_move(board):
    result = engine.play(board.board, chess.engine.Limit(time=1))
    return result.move



