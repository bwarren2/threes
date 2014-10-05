===============================
threes
===============================

.. image:: https://badge.fury.io/py/threes.png
    :target: http://badge.fury.io/py/threes

.. image:: https://travis-ci.org/bwarren2/threes.png?branch=master
        :target: https://travis-ci.org/bwarren2/threes

.. image:: https://pypip.in/d/threes/badge.png
        :target: https://pypi.python.org/pypi/threes


## Implementing the tile merge game

Installing the game:

    pip install threes

## Playing the game:

In a python shell:

    from threes import threes

    threes.new_game()

## Rules


(0) Shift the tiles on the board with w/s/a/d.  Each shift is one space.  If a tile would be shifted into another tile, the former tile can be merged into the latter if either:

* One tile is a 1 and the other a 2
* Both tiles have the same value.

(1) The new card always comes in "from" the direction that you pushed. So if you move pieces upwards, then the new card appears in the bottom row.

(2) The new card can only appear in a row/column if something in that column moved. For instance, if the board looks like (X is card, -- is empty, and nothing can merge):
X -- X X
-- X X X
-- -- -- X
-- -- -- --
and you push right, the new card must appear in the top row. because only the X in the top left corner moves at all. if you push left, it could come in any of the top three. If you push down, it could show up at the top of any of the four columns.

(3) The game uses a "bag system" to ensure that you get a relatively even mix of cards. The new cards are drawn from a bag which initially has twelve cards in it: four 1s, four 2s, and four 3s. Once the bag is depleted, a new twelve cards are put back in. This forms the stream of "basic cards."

(4) You're told whether the new card will be a 1, a 2, a 3, or "+" (plus), which is a card that exceeds 3.

(5a) The plus cards begin to appear after the highest card on the board is at least 48.
(5b) Once you're eligible for plus cards to appear, each card has a one in 21 chance of being a plus. The plus cards are inserted into the stream -- they don't overwrite anything, they just postpone them.


(5c) The value of the "+" card is uniformly chosen at random from all ranks above three, starting three below what you've seen.
To illustrate, if the high card on the board is a 48, then the plus is guaranteed to be a 6 (and will never be a 12 or 24). If the high card on the board is 768, the value of a + card could be anything in {6, 12, 24, 48, 96} (the three highest ranks which are not valid choices are 192, 384, and 768). Each of these would occur 20% of the time.

(6a) To the best of my ability to tell, the initial board state comes from beginning with an empty board, then making nine random moves. The rule (2) is not enforced for these moves (the new card can appear anywhere from where you pushed, it doesn't care about what's on the board already).
(6b) The initial board state is rejected if anything merged during those nine moves -- you always begin with exactly nine cards on the board.
(6c) The cards for the first nine moves are drawn from the first bag. So, as an example, the initial board may be
1 -- -- 1
-- -- -- 2
1 1 -- 3
2 -- 2 3
which involves four 1s, three 2s, and two 3s. You then know that the next three tiles will be {2, 3, 3} in some order, completing the first set of twelve.

(7) Scoring. When no more moves are possible, each card on the board is assigned a point value. Ones and twos are worth zero, and a card with value 3 * 2^n is worth 3^(n+1). In other words,
a 3 is worth 3
a 6 is worth 9
a 12 is worth 27
a 24 is worth 81
and so on.

* Free software: BSD license
* Documentation: http://threes.readthedocs.org.

Features
--------

* TODO
