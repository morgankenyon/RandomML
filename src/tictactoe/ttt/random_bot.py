import random

class RandomBot():
    def __init__(self, player):
        self.player = player

    def select_move(self, board):
        candidates = []
        for row in range(board.dimension):
            for col in range(board.dimension):
                if (board.is_space_empty(row, col)):
                    candidates.append([row,col])
        return random.choice(candidates)