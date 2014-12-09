"""Stage 5: Puzzle 10 of 10

print('pancake')

"""

import sys
sys.path.append('..')
import codestudio
artist = codestudio.load('s1level33')
a = artist

artist.color = artist.random_color()
artist.width = 187
artist.move_forward(101)

artist.wait()
