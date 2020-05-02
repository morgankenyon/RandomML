import copy

class Choice():
    def __init__(self, move, value, depth):
        self.move = move
        self.value = value
        self.depth = depth

    def __str__(self):
        return (str(self.move) + ": " + str(self.value))

class FullBot():
    def __init__(self, player):
        self.player = player
        self.num_moves_explored = 0

    def minimax(self, board, is_max, current_player, depth):
        winner = board.haswinner()
        if (winner == self.player):
            return Choice(board.last_move(), 10 - depth, depth)
        elif (winner == self.player.other):
            return Choice(board.last_move(), -10 + depth, depth)
        elif (len(board.moves) == 9):
            return Choice(board.last_move(), 0, depth)
        self.num_moves_explored = self.num_moves_explored + 1

        candidate_choices = []
        for row in range(board.dimension):
            for col in range(board.dimension):
                if (board.grid[row][col] is None):
                    newboard = copy.deepcopy(board)
                    newboard.make_move(row, col, current_player)
                    result = self.minimax(newboard, not is_max, current_player.other, depth + 1)
                    result.move = newboard.last_move()
                    candidate_choices.append(result)
        
        max_choice = None
        max_value = -100
        min_choice = None
        min_value = 100
        for i in range(len(candidate_choices)):
            choice = candidate_choices[i]
            if (is_max and choice.value > max_value):
                max_choice = choice
                max_value = choice.value
            elif (not is_max and choice.value < min_value):
                min_choice = choice
                min_value = choice.value

        if (is_max):
            return max_choice
        else:
            return min_choice 


    def select_move(self, board):
        choice = self.minimax(board, True, self.player, 0)
        print (str(self.num_moves_explored) + " moves explored to find " + str(choice.value))
        self.num_moves_explored = 0
        return choice.move