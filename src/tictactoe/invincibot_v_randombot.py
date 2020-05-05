from ttt.player import Player
from ttt.game import Game
from ttt.random_bot import RandomBot
from ttt.invincibot import InvinciBot
from datetime import datetime

def main():
    dateTimeObj = datetime.now()
    print(dateTimeObj)
    xbot = InvinciBot(Player.x)
    obot = RandomBot(Player.o)
    game = Game(15)
    print ("invincibot (x) vs randombot (o)")
    game.simulate(xbot, obot)

    xbot = RandomBot(Player.x)
    obot = InvinciBot(Player.o)
    game = Game(15)
    print ("randombot (x) vs invincibot (o)")
    game.simulate(xbot, obot)

    xbot = InvinciBot(Player.x)
    obot = InvinciBot(Player.o)
    game = Game(15)
    print ("invincibot (x) vs invincibot (o)")
    game.simulate(xbot, obot)

    
    dateTimeObj = datetime.now()
    print(dateTimeObj)

if __name__ == '__main__':
    main()