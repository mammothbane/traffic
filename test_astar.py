from traffic.config import Config
from traffic.heuristic.car_available_moves import CarAvailableMoves
from traffic.strategy.astar import AStar

h = CarAvailableMoves

c = Config('examples/simple.json')
a = AStar(c, h)
a.start()

for i in range(3):
    c = Config('examples/%s.json' % (i + 1))
    a = AStar(c, h)
    a.start()
