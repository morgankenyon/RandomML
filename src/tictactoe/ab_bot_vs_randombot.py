from ttt.player import Player
from ttt.game import Game
from ttt.random_bot import RandomBot
from ttt.invincibot import InvinciBot
from ttt.ab_bot import AbBot
from datetime import datetime

def main():
    dateTimeObj = datetime.now()
    print(dateTimeObj)
    xbot = AbBot(Player.x)
    obot = RandomBot(Player.o)
    game = Game(15)
    print ("abbot (x) vs randombot (o)")
    game.simulate(xbot, obot)

    xbot = RandomBot(Player.x)
    obot = AbBot(Player.o)
    game = Game(15)
    print ("randombot (x) vs abbot (o)")
    game.simulate(xbot, obot)

    xbot = AbBot(Player.x)
    obot = AbBot(Player.o)
    game = Game(15)
    print ("abbot (x) vs abbot (o)")
    game.simulate(xbot, obot)
    
    dateTimeObj = datetime.now()
    print(dateTimeObj)

if __name__ == '__main__':
    main()