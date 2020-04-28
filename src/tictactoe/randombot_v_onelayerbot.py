from ttt.utils import Player
from ttt.game import Game
from ttt.random_bot import RandomBot
from ttt.one_layer_bot import OneLayerBot

def main():
    xbot = RandomBot(Player.x)
    obot = OneLayerBot(Player.o)
    game = Game(100)
    game.simulate(xbot, obot)

if __name__ == '__main__':
    main()