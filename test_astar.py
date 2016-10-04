from traffic.config import Config
from traffic.heuristic.manhattan import Manhattan
from traffic.strategy.astar import AStar

c = Config('examples/simple.json')
a = AStar(c, Manhattan)
a.start()

for i in range(3):
    c = Config('examples/%s.json' % (i + 1))
    a = AStar(c, Manhattan)
    a.start()
