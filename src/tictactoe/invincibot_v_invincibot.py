from ttt.player import Player
from ttt.game import Game
from ttt.invincibot import InvinciBot

def main():
    xbot = InvinciBot(Player.x)
    obot = InvinciBot(Player.o)
    game = Game(1)
    game.simulate(xbot, obot, True)

if __name__ == '__main__':
    main()