from flask import (Flask, render_template, request)
import sys
from algorithms.Game import Game

app = Flask(__name__, template_folder='view', static_url_path='/static')

game = Game()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/newgame', methods = ["POST"])
def newgame():
    data = request.get_json()
    game.new_game(data['color'] == 'white', data['level'])
    print(data)
    return {'status': 'ok'}

@app.route('/undo', methods = ["POST"])
def undo():
    game.undo_moves()
    return {'status': 'ok'}

@app.route('/getmove', methods = ["POST"])
def getmove():
    data = request.get_json()
    print(data['from'], data['to'], data['promotion'])
    move = game.get_move(data['from'], data['to'], data['promotion'])
    game.board.push(move)
    if (len(move.uci()) == 5):
        return {"from": move.uci()[0:2], "to": move.uci()[2:4], "promotion": move.uci()[4:5]}
    else:
        return {"from": move.uci()[0:2], "to": move.uci()[2:4]}