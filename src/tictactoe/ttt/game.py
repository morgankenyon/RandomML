from .board import Board
from .player import Player

class Game():
    def __init__(self, num_of_games):
        self.num_of_games = num_of_games
        self.x_wins = 0
        self.o_wins = 0
        self.ties = 0
    
    def simulate(self, xbot, obot, print_game = False):
        for _ in range(self.num_of_games):
            board = Board()
            current_turn = Player.x
            winner = None
            for i in range(9):
                choice = []
                if (current_turn == xbot.player):
                    choice = xbot.select_move(board)
                else:
                    choice = obot.select_move(board)
                board.make_move(choice[0], choice[1], current_turn)

                winner = board.has_winner()

                if print_game:
                    board.print()
                if (winner != None):
                    #print ("Congrats " + str(winner))
                    break
                elif (i == 8):
                    #print ("It's a tie!")
                    break
                current_turn = current_turn.other
            if (winner == Player.x):
                self.x_wins = self.x_wins + 1
            elif (winner == Player.o):
                self.o_wins = self.o_wins + 1
            else:
                self.ties = self.ties + 1
        
        print ("x wins: " + str(self.x_wins))
        print ("o wins: " + str(self.o_wins))
        print ("ties: " + str(self.ties))