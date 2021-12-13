from flask import (Flask, render_template, request)
import sys
sys.path.insert(0, './algorithms/alpha_beta')
sys.path.insert(0, './algorithms/dqn')
sys.path.insert(0, './algorithms/stockfish')
from algorithms.Game import Game

app = Flask(__name__, template_folder='view', static_url_path='/static')

game = Game()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/newgame', methods = ["POST"])
def newgame():
    data = request.get_json()
    game.new_game(data['color'] == 'white')
    print(data)
    return {'status': 'ok'}

@app.route('/getmove', methods = ["POST"])
def getmove():
    data = request.get_json()
    print(data['from'], data['to'], data['promotion'])
    move = game.get_move(data['from'], data['to'], data['promotion'])
    game.board.push(move)
    return {"from": move.uci()[0:2], "to": move.uci()[2:4]}