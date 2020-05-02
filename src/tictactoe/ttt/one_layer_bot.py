import random
import copy

class OneLayerBot():
    def __init__(self, player):
        self.player = player

    def select_move(self, board):
        candidates = board.get_legal_moves()
        for i in range(len(candidates)):
            row = candidates[i][0]
            col = candidates[i][1]
            newboard = copy.deepcopy(board)
            newboard.make_move(row, col, self.player)
            if (newboard.haswinner() == self.player):
                return [row,col]
        return random.choice(candidates)