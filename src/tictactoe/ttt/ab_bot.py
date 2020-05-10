import copy

class Choice():
    def __init__(self, move, value, depth):
        self.move = move
        self.value = value
        self.depth = depth

    def __str__(self):
        return (str(self.move) + ": " + str(self.value))

class AbBot():
    def __init__(self, player):
        self.player = player
    
    def alpha_beta_search(self, board, is_max, current_player, depth, alpha, beta):
        # if board has a winner or is a tie
        # return with appropriate values
        winner = board.has_winner()
        if (winner == self.player):
            return Choice(board.last_move(), 10 - depth, depth)
        elif (winner == self.player.other):
            return Choice(board.last_move(), -10 + depth, depth)
        elif (len(board.moves) == 9):
            return Choice(board.last_move(), 0, depth)

        candidates = board.get_legal_moves()        
        max_choice = None
        min_choice = None
        for i in range(len(candidates)):
            row = candidates[i][0]
            col = candidates[i][1]
            newboard = copy.deepcopy(board)
            newboard.make_move(row, col, current_player)
            result = self.alpha_beta_search(newboard, not is_max, current_player.other, depth +1, alpha, beta)
            result.move = newboard.last_move()

            if (is_max):
                alpha = max(result.value, alpha)
                if (alpha >= beta):
                    return result

                if (max_choice is None or result.value > max_choice.value):
                    max_choice = result
            else:
                beta = min(result.value, beta)
                if (alpha >= beta):
                    return result
                
                if (min_choice is None or result.value < min_choice.value):
                    min_choice = result

        if (is_max):
            return max_choice
        else:
            return min_choice

    def select_move(self, board):
        choice = self.alpha_beta_search(board, True, self.player, 0, -100, 100)
        return choice.move