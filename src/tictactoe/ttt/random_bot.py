import random

class RandomBot():
    def __init__(self, player):
        self.player = player

    def select_move(self, board):
        candidates = board.get_legal_moves()
        return random.choice(candidates)