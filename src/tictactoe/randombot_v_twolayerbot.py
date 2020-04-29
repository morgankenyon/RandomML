from ttt.utils import Player
from ttt.game import Game
from ttt.random_bot import RandomBot
from ttt.two_layer_bot import TwoLayerBot

def main():
    xbot = RandomBot(Player.x)
    obot = TwoLayerBot(Player.o)
    game = Game(100)
    game.simulate(xbot, obot)

if __name__ == '__main__':
    main()