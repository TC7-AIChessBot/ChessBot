import chess
import chess.svg
from env import board as board

from flask import Flask, render_template, redirect, request

app = Flask(__name__)
board = board.ChessBoard()

def lastMove():
    try:
        lastMove = 'lastMove=' + board.env.peek().__str__()
        return lastMove
    except:
        return ''

def check_square():
    if board.is_check():
        return 'check=' + chess.square_name(board.env.king(board.env.turn))
    return ''


def getUrl():
    return 'https://backscattering.de/web-boardimage/board.svg?fen={}&{}&{}'.format(board.env.fen().split()[0], lastMove(), check_square())

@app.route('/', methods = ['POST', 'GET'])
def play():
    if request.method == 'POST':
        try:
            move = request.form['move']
            board.action(move)
            print(board.is_checkmate())
            return render_template('chess.html', err=False, url=getUrl())
        except:
            return render_template('chess.html', err=True, url=getUrl())

    else:
        return render_template('chess.html', err=False, url=getUrl())


app.run(debug=True)