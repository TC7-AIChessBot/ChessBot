import chess
import chess.svg
from flask import Flask, render_template, redirect, request

app = Flask(__name__)
board = chess.Board()

def lastMove():
    try:
        lastMove = 'lastMove=' + board.peek().__str__()
        return lastMove
    except:
        return ''

def check_square():
    if board.is_check():
        return 'check=' + chess.square_name(board.king(board.turn))
    return ''

def getUrl():
    return 'https://backscattering.de/web-boardimage/board.svg?fen={}&{}&{}'.format(board.fen().split()[0], lastMove(), check_square())

@app.route('/', methods = ['POST', 'GET'])
def play():
    if request.method == 'POST':
        try:
            move = request.form['move']
            board.push_san(move)
            print(board.is_checkmate())
            return render_template('chess.html', err=False, url=getUrl())
        except:
            return render_template('chess.html', err=True, url=getUrl())

    else:
        return render_template('chess.html', err=False, url=getUrl())


app.run(debug=True)