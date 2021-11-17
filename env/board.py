import chess
import chess.svg
import numpy as np

class ChessBoard:

    def __init__(self):
        self.env = chess.Board()
        self.mapped = {
        'P': 1,     # White Pawn
        'p': -1,    # Black Pawn
        'N': 2,     # White Knight
        'n': -2,    # Black Knight
        'B': 3,     # White Bishop
        'b': -3,    # Black Bishop
        'R': 4,     # White Rook
        'r': -4,    # Black Rook
        'Q': 5,     # White Queen
        'q': -5,    # Black Queen
        'K': 6,     # White King
        'k': -6     # Black King
        }

    def convert_state_to_int(self):
        epd_string = self.env.epd()
        list_int = np.empty((0, ))
        for i in epd_string:
            if i == " ":
                list_int = list_int.reshape((8, 8))
                return list_int
            elif i != "/":
                if i in self.mapped:
                    list_int = np.append(list_int, self.mapped[i])
                else:
                    for counter in range(0, int(i)):
                        list_int = np.append(list_int, 0)
        list_int = list_int.reshape((8, 8))
        return list_int


    # state, action, reward
    def state(self):
        return self.env

    def legal_moves(self):
        return list(self.env.legal_moves)

    def action(self, move: chess.Move or str):
        if type(move) == chess.Move:
            if self.env.is_legal(move):
                return self.env.push(move)
            else:
                raise ValueError

        if type(move) == str:
            return self.env.push_san(move)

    def undo(self):
        return self.env.pop()

    # end game
    '''
    NOTE : 
    use  self.env.outcome() to find draw or end;
    chess.Termination() to set conditions? 
    '''
    def is_draw(self):
        '''
        1. Stalemate is a situation in the game of chess where the player whose turn it is to move
        is not in check but has no legal move. The rules of chess provide that when stalemate occurs, 
        the game ends as a draw.

        2. While playing Chess, a Draw is declared when a player has made the same moves, or is about
        to make the same move, five times in a row – since the player cannot make any progress. For example, 
        if a player’s King is threatened by another piece and moves to the same square five times in a row 
        in order to escape – a fiveFold Repetition Draw is called.

        3. The 75-Move Rule of Draw is a strange one – it states that if both players haven’t made any progress
        in 75 moves – the game is declared a Draw. If both players haven’t captured any of the other player’s 
        pieces or moved their pawns in 75 moves – a 75-Move Draw is declared.

        4. An Insufficient Material Draw is called in Chess when neither player has enough pieces left on the 
        board so that they can Check-Mate the other player.
        '''

        if self.env.is_stalemate():
            print("statlemate")
            return True
        if self.env.is_fivefold_repetition():
            print("fivefold repetition")
            return True
        if self.env.is_seventyfive_moves():
            print("75 moves")
            return True
        if self.env.is_insufficient_material():
            print("Insufficient Material")
            return True
        
        return False

    def is_checkmate(self):
        # If There is checkmate then it will be TRUE else FALSE.It will be a boolean value.
        return self.env.is_checkmate()

    def is_check(self):
        return self.env.is_check()


    
