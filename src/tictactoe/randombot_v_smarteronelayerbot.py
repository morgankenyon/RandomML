from ttt.utils import Player
from ttt.game import Game
from ttt.random_bot import RandomBot
from ttt.smarter_one_layer_bot import SmarterOneLayerBot

def main():
    xbot = RandomBot(Player.x)
    obot = SmarterOneLayerBot(Player.o)
    game = Game(100)
    game.simulate(xbot, obot)

if __name__ == '__main__':
    main()