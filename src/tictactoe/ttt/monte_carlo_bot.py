import random
import copy

class MonteCarloStats():
    def __init__(self):
        self.games = 0
        self.wins = 0
        self.losses = 0
        self.ties = 0
    
    def one_tie(self):
        self.ties = self.ties + 1
        self.games = self.games + 1

    def one_loss(self):
        self.losses = self.losses + 1
        self.games = self.games + 1

    def one_win(self):
        self.wins = self.wins + 1
        self.games = self.games + 1


class MonteCarloSearch():
    def __init__(self, board, player, num_of_rollouts):
        self.board = board
        self.player = player
        self.num_of_rollouts = num_of_rollouts

    def search(self):
        stats = MonteCarloStats()

        for _ in range(self.num_of_rollouts):
            newboard = copy.deepcopy(self.board)
            current_turn = self.player

            while True:
                winner = newboard.has_winner()
                if (winner == self.player):
                    #return Choice(board.last_move(), 10 - depth, depth)
                    stats.one_win()
                    break
                elif (winner == self.player.other):
                    #return Choice(board.last_move(), -10 + depth, depth)
                    stats.one_loss()
                    break
                elif (len(newboard.moves) == 9):
                    #return Choice(board.last_move(), 0, depth)
                    stats.one_tie()
                    break
                
                
                candidates = newboard.get_legal_moves()
                random_choice = random.choice(candidates)
                newboard.make_move(random_choice[0],random_choice[1], current_turn)

                current_turn = current_turn.other
        return stats

# class MonteCarloBot():
#     def __init__(self, player, depth, num_of_rollouts):
#         self.player = player
#         self.depth = depth
#         self.num_of_rollouts = num_of_rollouts
#         self.wins = 0
#         self.ties = 0
#         self.losses = 0
#         self.games = 0



#     def select_move(self, board):
#         # resetting MC Search tracking
#         self.wins = 0
#         self.ties = 0
#         self.losses = 0
#         self.games = 0
#         candidates = board.get_legal_moves()
#         return random.choice(candidates)

#     def 