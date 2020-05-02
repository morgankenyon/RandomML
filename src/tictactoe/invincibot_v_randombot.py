from ttt.player import Player
from ttt.game import Game
from ttt.random_bot import RandomBot
from ttt.invincibot import InvinciBot

def main():
    xbot = InvinciBot(Player.x)
    obot = RandomBot(Player.o)
    game = Game(1)
    game.simulate(xbot, obot, False)

if __name__ == '__main__':
    main()