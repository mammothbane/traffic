from traffic.puzzle import Puzzle
from traffic.strategy.ids import IDS

p = Puzzle('examples/simple.json')
ids = IDS(p)
ids.start()

for i in range(3):
    p = Puzzle('examples/%s.json' % (i + 1))
    ids = IDS(p)

    ids.start()
