from ttt.player import Player
from ttt.game import Game
from ttt.invincibot import InvinciBot
from ttt.ab_bot import AbBot
from datetime import datetime

def main():
    dateTimeObj = datetime.now()
    print(dateTimeObj)
    xbot = AbBot(Player.x)
    obot = InvinciBot(Player.o)
    game = Game(15)
    print ("abbot (x) vs invincibot (o)")
    game.simulate(xbot, obot)

    xbot = InvinciBot(Player.x)
    obot = AbBot(Player.o)
    game = Game(15)
    print ("invincibot (x) vs abbot (o)")
    game.simulate(xbot, obot)

    
    dateTimeObj = datetime.now()
    print(dateTimeObj)

if __name__ == '__main__':
    main()