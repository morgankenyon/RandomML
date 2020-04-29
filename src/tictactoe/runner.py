from ttt.full_bot import FullBot
from ttt.board import Board
from ttt.utils import Player

def main():

    b = Board(3)
    xbot = FullBot(Player.x)
    b.make_move(0,0, Player.x)
    b.make_move(0,2, Player.o)
    b.make_move(1,1, Player.x)
    b.make_move(0,1, Player.o)
    move = xbot.select_move(b)
    assert move == [2,2]

if __name__ == '__main__':
    main()