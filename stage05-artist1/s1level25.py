"""Stage 5: Puzzle 2 of 10

Now, draw a square. NOTE: tell the artist to use your favorite color pen
by assigning a color to the `artist.color` variable.

"""

import sys
sys.path.append('..')
import codestudio
artist = codestudio.load('s1level25')
a = artist

artist.color = 'red'
artist.move_forward(100)
artist.rt()
artist.move_forward(100)
artist.turn_right(90)
artist.move_forward(100)
artist.turn_right(90)
artist.move_forward(100)
artist.check()
