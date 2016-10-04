from traffic.ids import IDS
from traffic.puzzle import Puzzle

p = Puzzle('examples/simple.json')
ids = IDS(p)
ids.start()

for i in range(3):
    p = Puzzle('examples/%s.json' % (i + 1))
    ids = IDS(p)

    ids.start()
