from traffic.ids import IDS
from traffic.puzzle import Puzzle

for i in range(3):
    p = Puzzle('examples/%s.json' % (i + 1))
    ids = IDS(p)

    ids.start()
