import pytest
from .ttt.board import Board
from .ttt.utils import Player

def test_row_win():
    b = Board(3)
    b.make_move(0,0, Player.x)
    b.make_move(0,1, Player.x)
    b.make_move(0,2, Player.x)
    assert b.haswinner() == Player.x

def test_col_win():
    b = Board(3)
    b.make_move(0,0, Player.x)
    b.make_move(1,0, Player.x)
    b.make_move(2,0, Player.x)
    assert b.haswinner() == Player.x

def test_back_diagonal_win():
    b = Board(3)
    b.make_move(0,0, Player.x)
    b.make_move(1,1, Player.x)
    b.make_move(2,2, Player.x)
    assert b.haswinner() == Player.x

def test_forward_diagonal_win():
    b = Board(3)
    b.make_move(0,2, Player.x)
    b.make_move(1,1, Player.x)
    b.make_move(2,0, Player.x)
    assert b.haswinner() == Player.x

def test_last_move():
    b = Board(3)
    b.make_move(0,2, Player.x)
    b.make_move(1,1, Player.o)
    last_move = b.last_move()
    assert len(b.moves) == 2
    assert last_move[0] == 1
    assert last_move[1] == 1

def test_make_move_throws_when_spot_occupied():
    b = Board(3)
    b.make_move(0,2, Player.x)
    b.make_move(1,1, Player.o)
    with pytest.raises(Exception):
        assert b.make_move(0,2, Player.x)

def test_is_space_empty():
    b = Board(3)
    is_empty = b.is_space_empty(0,0)
    assert is_empty == True

def test_is_space_occupied():
    b = Board(3)
    b.make_move(0,2, Player.x)
    is_empty = b.is_space_empty(0,2)
    assert is_empty == False
