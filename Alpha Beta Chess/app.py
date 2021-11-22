from flask import Flask, render_template, request, redirect
from flask.helpers import url_for
from MyChessBoard import MyChessBoard
from Alpha_Beta import find_move

app = Flask(__name__)
board = MyChessBoard()

@app.route('/')
@app.route('/newgame')
def index():
    board.newgame()
    return render_template('index.html')


@app.route('/play/<color>', methods = ['POST', 'GET'])
def play(color):
    if request.method == 'POST':
        try:
            # if (board.turn() and color=='BLACK') or (not board.turn() and color=='WHITE'):
            #     board.push(find_move(board))

            move = request.form['move']
            board.board.push_san(move)
            if board.board.is_checkmate(): return redirect(url_for('index'))

            if (board.turn() and color=='BLACK') or (not board.turn() and color=='WHITE'):
                board.push(find_move(board))

            return render_template('play.html', err=False, url=board.get_img_url())
        except:
            return render_template('play.html', err=True, url=board.get_img_url())
    else:
        if (board.turn() and color=='BLACK') or (not board.turn() and color=='WHITE'):
                board.push(find_move(board))
        return render_template('play.html', err=False, url=board.get_img_url())