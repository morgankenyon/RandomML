import pytest
from .board import Board
from .player import Player
from .monte_carlo_bot import MonteCarloSearch

def test_easy_monte_carlo_search():
    b = Board()
    b.make_move(0,0, Player.x)
    b.make_move(1,0, Player.o)
    b.make_move(0,1, Player.x)
    b.make_move(1,2, Player.o)
    b.make_move(1,1, Player.x)
    b.make_move(2,1, Player.o)
    b.make_move(2,2, Player.x)
    b.make_move(2,0, Player.o)
    #xbot = MonteCarloBot(Player.x, 2, 10)
    #move = xbot.select_move(b)
    #assert move == [0,2]
    mcSearch = MonteCarloSearch(b, Player.x, 100)
    stats = mcSearch.search()
    assert stats.games == 100
    assert stats.wins == 100
    assert stats.losses == 0
    assert stats.ties == 0


def test_medium_monte_carlo_search():
    b = Board()
    b.make_move(0,0, Player.x)
    b.make_move(1,0, Player.o)
    b.make_move(0,1, Player.x)
    b.make_move(1,2, Player.o)
    b.make_move(1,1, Player.x)
    b.make_move(2,1, Player.o)
    #randomize board a bit, x always wins no matter what o does
    mcSearch = MonteCarloSearch(b, Player.x, 100)
    stats = mcSearch.search()
    assert stats.games == 100
    assert stats.wins == 100
