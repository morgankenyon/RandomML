import random
import copy

class TwoLayerBot():
    def __init__(self, player):
        self.player = player

    def select_move(self, board):
        candidates = []
        winning_move = None
        losing_move = None
        for row in range(board.dimension):
            for col in range(board.dimension):
                if (board.grid[row][col] is None):
                    newboard = copy.deepcopy(board)
                    newboard.grid[row][col] = self.player
                    candidates.append([row,col])

                    #check if self wins
                    if (newboard.haswinner() == self.player):
                        winning_move = [row,col]
                    
                    #check if other wins
                    newboard.grid[row][col] = self.player.other
                    if (newboard.haswinner() == self.player.other):
                        losing_move = [row,col]
        if (winning_move != None):
            return winning_move
        elif (losing_move != None):
            return losing_move
        return random.choice(candidates)