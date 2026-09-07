# Dreidel Game Simulator

A command-line simulation of the traditional dreidel coin game, built in Python
using object-oriented design. Multiple players take turns spinning a dreidel,
betting and eating coins, until a winner is determined.

## How to Run

Make sure all files are in the same folder, then run:

```
python dreidel_game.py
```

You'll be prompted to enter the number of players (2-5), then each player's
name and dreidel color. The game will run for a random number of rounds
(3-10), printing a summary after each round.

## Rules

Each player starts with 8 coins and antes one coin into a central pot to
begin the game.

On each turn, a player may first choose to "eat" (bank) some of their coins
before spinning. Eaten coins count toward their final score and can't be
lost afterward. If they still have coins left, they ante one more coin and
spin their dreidel. The side that lands face up determines what happens:

| Side  | Result                                  |
|-------|------------------------------------------|
| Gimel | Player takes the entire pot               |
| Hey   | Player takes half the pot (rounded down)  |
| Shin  | Player adds one coin to the pot           |
| Nun   | Nothing happens                           |

If the pot ever drops below 2 coins, every active player antes again to
refill it.

A player who runs out of coins is eliminated and sits out the rest of the
game.

The game ends after the randomly chosen number of rounds, or early if only
one player remains active.

**Winner:** the winner is whichever player is still active (not eliminated)
and has eaten the most coins overall. If everyone is eliminated, there is no
winner.

## Project Structure

- `dreidel_game.py` — the `Game` class; coordinates rounds, turns, and
  determines the winner
- `player.py` — the `Player` class; tracks each player's coins, eaten coins,
  and dreidel
- `dreidel.py` — the `Dreidel` class; represents a single dreidel that can be
  spun to land on shin, gimel, hey, or nun
- `pot.py` — the `Pot` class; tracks the shared pot of coins and handles
  payouts

## Built With

- Python 3
- Object-oriented design: encapsulation across four collaborating classes
  (`Game`, `Player`, `Dreidel`, `Pot`)
