import pytest
from .board import Board
from .player import Player
from .invincibot import InvinciBot


def test_column_win():
    b = Board()
    xbot = InvinciBot(Player.x)
    b.make_move(0,0, Player.x)
    b.make_move(1,0, Player.o)
    b.make_move(0,1, Player.x)
    b.make_move(1,1, Player.o)
    move = xbot.select_move(b)
    assert move == [0,2]

def test_row_win():
    b = Board()
    xbot = InvinciBot(Player.x)
    b.make_move(0,0, Player.x)
    b.make_move(0,2, Player.o)
    b.make_move(1,0, Player.x)
    b.make_move(0,1, Player.o)
    move = xbot.select_move(b)
    assert move == [2,0]

def test_back_diag_win():
    b = Board()
    xbot = InvinciBot(Player.x)
    b.make_move(0,0, Player.x)
    b.make_move(0,2, Player.o)
    b.make_move(1,1, Player.x)
    b.make_move(0,1, Player.o)
    move = xbot.select_move(b)
    assert move == [2,2]

def test_forward_diag_win():
    b = Board()
    xbot = InvinciBot(Player.x)
    b.make_move(2,0, Player.x)
    b.make_move(1,2, Player.o)
    b.make_move(1,1, Player.x)
    b.make_move(0,1, Player.o)
    move = xbot.select_move(b)
    assert move == [0,2]


