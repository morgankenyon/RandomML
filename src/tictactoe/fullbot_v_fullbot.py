from ttt.utils import Player
from ttt.game import Game
from ttt.full_bot import FullBot

def main():
    xbot = FullBot(Player.x)
    obot = FullBot(Player.o)
    game = Game(1)
    game.simulate(xbot, obot, True)

if __name__ == '__main__':
    main()