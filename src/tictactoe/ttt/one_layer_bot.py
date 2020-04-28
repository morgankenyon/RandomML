import random
import copy

class OneLayerBot():
    def __init__(self, player):
        self.player = player

    def select_move(self, board):
        candidates = []
        for row in range(board.dimension):
            for col in range(board.dimension):
                if (board.grid[row][col] is None):
                    newboard = copy.deepcopy(board)
                    newboard.grid[row][col] = self.player
                    candidates.append([row,col])
                    if (newboard.haswinner() == self.player):
                        return [row,col]
        return random.choice(candidates)