import enum
import copy
import collections
import random

# Work in Progress

class Player(enum.Enum):
    x = 1
    o = 2

    @property
    def other(self):
        return Player.x if self == Player.o else Player.o


MARKER_TO_CHAR = {
    None: ' . ',
    Player.x: ' x ',
    Player.o: ' o ',
}

Point = collections.namedtuple('Point', 'value row col')

    
    #print ('Winner:' + str(board.haswinner()))



class Board():
    def __init__(self, dimension):
        self.dimension = dimension
        self.grid = [ [ None for y in range (dimension) ] for x in range (dimension ) ]
        self.moves = []
        #self.player_turn = Player.x

    def haswinner(self):
        uniquediags = set()
        for i in range(self.dimension):
            uniquerows = list(dict.fromkeys(self.grid[i]))
            if (len(uniquerows) == 1 and uniquerows[0] != None):
                return uniquerows[0]

            uniquecolumns = set()
            for j in range(self.dimension):
                uniquecolumns.add(self.grid[j][i])
                if (i == j):
                    uniquediags.add(self.grid[j][i])
            if (len(uniquecolumns) == 1):
                value = uniquecolumns.pop()
                if (value != None):
                    return value

        if (len(uniquediags) == 1):
            value = uniquediags.pop()
            if (value != None):
                return value
        return None

    def make_move(self, row, col, player):
        if (self.grid[row][col] is None):
            self.grid[row][col] = player
            self.moves.append([row,col])
        else:
            raise Exception("Attempting to move onto already occupied space")

    def last_move(self):
        return self.moves[-1]

    def print(self):
        print()
        for row in range(self.dimension):
            line = []
            for col in range(self.dimension):            
                line.append(MARKER_TO_CHAR[self.grid[row][col]])
            print('%s' % (''.join(line)))
                
    def __deepcopy__(self, memodict={}):
        dp = Board(self.dimension)
        dp.grid = copy.deepcopy(self.grid) 
        dp.moves = copy.deepcopy(self.moves)
        return dp       

# class BoringBot():
#     def __init__(self, player):
#         self.player = player

#     def minimax(self, board, is_max, current_player):
#         winner = board.haswinner()
#         if (winner == self.player):
#             return Choice(board.last_move(), 1)
#         elif (winner == self.player.other):
#             return Choice(board.last_move(), -1)
#         elif (len(board.moves) == 9):
#             return Choice(board.last_move(), 0)

#         candidate_choices = []
#         for row in range(board.dimension):
#             for col in range(board.dimension):
#                 if (board.grid[row][col] is None):
#                     newboard = copy.deepcopy(board)
#                     newboard.make_move(row, col, current_player)
#                     candidate_choices.append(self.minimax(newboard, not is_max, current_player.other))
        
#         max_choice = None
#         min_choice = None
#         tie_choice = None
#         for i in range(len(candidate_choices)):
#             choice = candidate_choices[i]
#             if (choice.value == 1 and max_choice is None):
#                 max_choice = choice
            
#             if (choice.value == 0 and tie_choice is None):
#                 tie_choice = choice

#             if (choice.value == -1 and min_choice is None):
#                 min_choice = choice

#         if (is_max):
#             if (max_choice is not None):
#                 return max_choice
#             elif (min_choice is not None):
#                 return min_choice
#             return tie_choice      
#         else:
#             if (min_choice is not None):
#                 return min_choice
#             elif (max_choice is not None):
#                 return max_choice
#             return tie_choice


#     def select_move(self, board):
#         choice = self.minimax(board, True, self.player)
#         print (choice)
#         return choice.move

class Game():
    def __init__(self, num_of_games):
        self.num_of_games = num_of_games
        self.x_wins = 0
        self.o_wins = 0
        self.ties = 0
    
    def simulate(self, xbot, obot):
        for _ in range(self.num_of_games):
            board = Board(3)
            current_turn = Player.x
            winner = None
            for i in range(9):
                choice = []
                if (current_turn == xbot.player):
                    choice = xbot.select_move(board)
                else:
                    choice = obot.select_move(board)
                #board.moves.append(choice)
                #board.grid[choice[0]][choice[1]] = current_turn
                board.make_move(choice[0], choice[1], current_turn)

                winner = board.haswinner()
                board.print()
                if (winner != None):
                    print ("Congrats " + str(winner))
                    #print ("You won in " + str(i + 1) + " moves")
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



# xbot = RandomBot(Player.x)
# obot = SmarterOneLayerBot(Player.o)
# game = Game(10)
# game.simulate(xbot, obot)

# xbot = RandomBot(Player.x)
# obot = BoringBot(Player.o)
# game = Game(1)
# game.simulate(xbot, obot)

# xbot = RandomBot(Player.x)
# obot = InvincibleBot(Player.o)
# board = Board(3)
# board.make_move(0,1, Player.x)
# board.make_move(0,0, Player.o)
# board.make_move(2,1, Player.x)
# obot.select_move(board)
# board.print()
# board.grid[0][1] = Player.x
# board.moves.append([0,0])
# board.grid[1][0] = Player.o
# board.moves.append([1,1])
# board.grid[0][1] = Player.x
# board.moves.append([0,0])
# board.grid[1][1] = Player.o
# board.moves.append([1,1])
# board.grid[2][2] = Player.x
# board.moves.append([2,2])
# board.grid[2][0] = Player.o
# board.moves.append([2,0])
#current_turn = Player.x
#for i in range(7):
#    if (current_turn == Player.x):
#        move = xbot.select_move(board)
#    else:
#        move = obot.select_move(board)
#    board.make_move(move[0], move[1], current_turn)
#    winner = board.haswinner()
#    print(board)
#    current_turn = current_turn.other

# x wins
xbot = BoringBot(Player.x)
xboard = Board(3)
xboard.make_move(0,1, Player.x)
xboard.make_move(0,0, Player.o)
xboard.make_move(2,1, Player.x)
xboard.make_move(1,0, Player.o)
xboard.make_move(1,1, Player.x)
xboard.print()
xbot.select_move(xboard)

# o wins
xbot = BoringBot(Player.x)
oboard = Board(3)
oboard.make_move(0,1, Player.x)
oboard.make_move(0,0, Player.o)
oboard.make_move(2,1, Player.x)
oboard.make_move(1,0, Player.o)
oboard.make_move(1,2, Player.x)
oboard.make_move(2,0, Player.o)
oboard.print()
xbot.select_move(oboard)

# tie
xbot = BoringBot(Player.x)
tboard = Board(3)
tboard.make_move(0,1, Player.x)
tboard.make_move(0,0, Player.o)
tboard.make_move(1,0, Player.x)
tboard.make_move(1,1, Player.o)
tboard.make_move(2,2, Player.x)
tboard.make_move(2,0, Player.o)
tboard.make_move(0,2, Player.x)
tboard.make_move(1,2, Player.o)
tboard.make_move(2,1, Player.x)
tboard.print()
xbot.select_move(tboard)

# two leve win
xbot = BoringBot(Player.x)
tlb = Board(3)
tlb.make_move(0,0, Player.x)