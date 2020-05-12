## Tic Tac Toe

This folder holds all code related to my tic-tac-toe programming. 

* random_bot.py - makes random moves
* one_layer_bot.py - searches one move into the future, will always pick a winning move if one is available, otherwise plays randomly.
* two_layer_bot.py - searches two moves into the future, picks a winning move or blocks an opponent from winning, otherwise plays randomly.
* invincibot.py - uses minimax search to always choose the optimal move, never loses but slow.
* ab_bot.py - uses alpha-beta pruning to speed up finding optimal move, improves search over invincibot.py by ~95%.

I've also written several blog posts explaining each of these bots in detail.

* [Implementing Minimax Tree Search](https://thesharperdev.com/implementing-minimax-tree-search/)
* [Coding a Perfect Tic-Tac-Toe Bot!](https://thesharperdev.com/coding-the-perfect-tic-tac-toe-bot/)
* [Optimizing our Perfect Tic-Tac-Toe Bot](https://thesharperdev.com/optimizing-our-perfect-tic-tac-toe-bot/)

