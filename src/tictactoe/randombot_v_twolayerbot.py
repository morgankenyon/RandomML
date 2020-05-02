from ttt.player import Player
from ttt.game import Game
from ttt.random_bot import RandomBot
from ttt.two_layer_bot import TwoLayerBot

def main():
    xbot = RandomBot(Player.x)
    obot = TwoLayerBot(Player.o)
    game = Game(1000)
    print ("randombot (x) vs twolayerbot (o)")
    game.simulate(xbot, obot)

    xbot = TwoLayerBot(Player.x)
    obot = RandomBot(Player.o)
    game = Game(1000)
    print ("twolayerbot (x) vs randombot (o)")
    game.simulate(xbot, obot)

    xbot = TwoLayerBot(Player.x)
    obot = TwoLayerBot(Player.o)
    game = Game(1000)
    print ("twolayerbot (x) vs twolayerbot (o)")
    game.simulate(xbot, obot)

if __name__ == '__main__':
    main()