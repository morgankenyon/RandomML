#from ttt.full_bot import FullBot
from ttt.board import Board
from ttt.player import Player
from ttt.monte_carlo_bot import MonteCarloSearch

def main():

    b = Board()
    b.make_move(0,0, Player.x)
    b.make_move(1,0, Player.o)
    b.make_move(0,1, Player.x)
    b.make_move(1,2, Player.o)
    b.make_move(1,1, Player.x)
    b.make_move(2,1, Player.o)
    
    
    #mcSearch = MonteCarloSearch(b, Player.x, 100)
    #stats = mcSearch.search()
    #b.make_move(2,2, Player.x)
    #b.make_move(2,0, Player.o)
    b.print()
    #b.make_move(1,1, Player.x)
    #b.make_move(0,1, Player.o)
    #move = xbot.select_move(b)
    #assert move == [2,2]

if __name__ == '__main__':
    main()