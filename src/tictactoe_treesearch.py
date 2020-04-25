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

def generate_valid_boards(board, player, maximizer, depth):
    winner = board.haswinner()
    if (winner != None):
        if winner == maximizer:
            return 1
        else:
            return -1

    if (depth == 0):
        return 0

    
    value = None
    for row in range(board.dimension):
        for col in range(board.dimension):
            if (board.grid[row][col] is None):
                newboard = copy.deepcopy(board)
                newboard.grid[row][col] = player
                print(newboard)
                value = generate_valid_boards(newboard, player.other, maximizer, depth - 1)
                if (player == maximizer and value == 1):
                    return value
                elif (player != maximizer and value == -1):
                    return value
    return value
    #return boardStates

class MoveValue():
    def __init__(self, move, value, depth):
        self.move = move
        self.value = value
        self.depth = depth

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
        self.grid[row][col] = player
        self.moves.append([row,col])

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
    
class RandomBot():
    def __init__(self, player):
        self.player = player

    def select_move(self, board):
        candidates = []
        for row in range(board.dimension):
            for col in range(board.dimension):
                if (board.grid[row][col] is None):
                    candidates.append([row,col])
        return random.choice(candidates)

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

class SmarterOneLayerBot():
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

class InvincibleBot():
    def __init__(self, player):
        self.player = player

    def tree_search(self, board, is_max, depth):
        winner = board.haswinner()
        if (winner == self.player):
            return MoveValue(board.moves[-1], 1, depth)
        elif (winner == self.player.other):
            return MoveValue(board.moves[-1], -1, depth)
        elif (winner == None and len(board.moves) == 9):
            return MoveValue(board.moves[-1], 0, depth)

        # tie_move = None
        # losing_move = None
        move_values = []
        for row in range(board.dimension):
            for col in range(board.dimension):
                if (board.grid[row][col] is None):
                    newboard = copy.deepcopy(board)
                    newboard.grid[row][col] = self.player
                    newboard.moves.append([row,col])

                    move_values.append(self.tree_search(newboard, not is_max, depth + 1))
                    # if (move_value.value == 1 and is_max):
                    #     return MoveValue([row,col], move_value.value)
                    # elif (move_value.value == -1 and not is_max):
                    #     return MoveValue([row,col], move_value.value)
                    # elif (move_value.value == 0):
                    #     tie_move = MoveValue([row,col], 0)
                    # elif (is_max):
                    #     losing_move = MoveValue([row,col], -1)
                    # elif (not is_max):
                    #     losing_move = MoveValue([row,col], 1)
        
        #for i in range(len(move_values)):

        
        return random.choice(move_values)

    def explore_layer(self, board, turn):
        new_boards = []
        for row in range(board.dimension):
            for col in range(board.dimension):
                if (board.grid[row][col] is None):
                    newboard = copy.deepcopy(board)
                    newboard.make_move(row, col, turn)
                    new_boards.append(newboard)
        return new_boards

    def bfs(self, board):
        depth = 1
        current_layer = [board]
        turn = self.player
        for i in range(depth):
            layer_boards = []
            for i in range(len(current_layer)):
                layer_boards.extend(self.explore_layer(current_layer[i], turn))
            
            for i in range(len(layer_boards)):
                layer_board = 
            current_layer = layer_boards
        for i in range(len(current_layer)):
            current_layer[i].print()
        
            
    def select_move(self, board):
        #mv = self.tree_search(board, True, 0)
        self.bfs(board)
        #return mv.move


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
                board.moves.append(choice)
                board.grid[choice[0]][choice[1]] = current_turn

                winner = board.haswinner()
                print(board)
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


#xbot = RandomBot(Player.x)
#obot = SmarterOneLayerBot(Player.o)
#game = Game(10)
#game.simulate(xbot, obot)



xbot = RandomBot(Player.x)
obot = InvincibleBot(Player.o)
board = Board(3)
board.make_move(0,1, Player.x)
board.make_move(0,0, Player.o)
board.make_move(2,1, Player.x)
obot.select_move(board)
board.print()
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
