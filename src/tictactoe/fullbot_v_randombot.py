from ttt.utils import Player
from ttt.game import Game
from ttt.two_layer_bot import TwoLayerBot
from ttt.full_bot import FullBot

def main():
    xbot = FullBot(Player.x)
    obot = TwoLayerBot(Player.o)
    game = Game(5)
    game.simulate(xbot, obot, True)

if __name__ == '__main__':
    main()