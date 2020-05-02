from ttt.player import Player
from ttt.game import Game
from ttt.random_bot import RandomBot
from ttt.one_layer_bot import OneLayerBot

def main():
    xbot = RandomBot(Player.x)
    obot = OneLayerBot(Player.o)
    game = Game(1000)
    print ("randombot (x) vs onelayerbot (o)")
    game.simulate(xbot, obot)

    xbot = OneLayerBot(Player.x)
    obot = RandomBot(Player.o)
    game = Game(1000)
    print ("onelayerbot (x) vs randombot (o)")
    game.simulate(xbot, obot)

    xbot = OneLayerBot(Player.x)
    obot = OneLayerBot(Player.o)
    game = Game(1000)
    print ("onelayerbot (x) vs onelayerbot (o)")
    game.simulate(xbot, obot)

if __name__ == '__main__':
    main()