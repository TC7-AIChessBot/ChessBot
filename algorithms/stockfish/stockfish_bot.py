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
    engine = chess.engine.SimpleEngine.popen_uci(r"./algorithms/stockfish/stockfish_14.1_win_32bit.exe")
elif platform == "win64":
    engine = chess.engine.SimpleEngine.popen_uci(r"./algorithms/stockfish/stockfish_14.1_win_x64.exe")
elif platform == "darwin":
    try:
        engine = chess.engine.SimpleEngine.popen_uci(r"./algorithms/stockfish/stockfish-arm64")
    except:
        try: 
            engine = chess.engine.SimpleEngine.popen_uci(r"./algorithms/stockfish/stockfish-x86-64-bmi2")
        except:
            print("Don't support this OS for level 3")
else:
    print("Don't support this OS for level 3")


# %%
def find_move(board):
    result = engine.play(board.board, chess.engine.Limit(time=1))
    return result.move



