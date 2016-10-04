from traffic.config import Config
from traffic.heuristic.cars_in_between import CarsInBetween
from traffic.strategy.astar import AStar

h = CarsInBetween

c = Config('examples/simple.json')
a = AStar(c, h)
a.start()

for i in range(3):
    c = Config('examples/%s.json' % (i + 1))
    a = AStar(c, h)
    a.start()
