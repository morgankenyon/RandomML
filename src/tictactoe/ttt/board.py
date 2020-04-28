import copy
from .utils import MARKER_TO_CHAR

class Board():
    def __init__(self, dimension):
        self.dimension = dimension
        self.grid = [ [ None for y in range (dimension) ] for x in range (dimension ) ]
        self.moves = []

    def haswinner(self):
        backwards_diag = set()
        forwards_diag = set()
        for i in range(self.dimension):
            uniquerows = list(dict.fromkeys(self.grid[i]))
            if (len(uniquerows) == 1 and uniquerows[0] != None):
                return uniquerows[0]

            uniquecolumns = set()
            for j in range(self.dimension):
                uniquecolumns.add(self.grid[j][i])
                if (i == j):
                    backwards_diag.add(self.grid[j][i])

                if (i == 1 and j == 1):
                    forwards_diag.add(self.grid[j][i])
                elif (i == 2 and j == 0):
                    forwards_diag.add(self.grid[j][i])
                elif (i == 0 and j == 2):
                    forwards_diag.add(self.grid[j][i])
            if (len(uniquecolumns) == 1):
                value = uniquecolumns.pop()
                if (value != None):
                    return value

        if (len(backwards_diag) == 1):
            value = backwards_diag.pop()
            if (value != None):
                return value
        elif (len(forwards_diag) == 1):            
            value = forwards_diag.pop()
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

    def is_space_empty(self, row, col):
        return self.grid[row][col] is None

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