from traffic.config import Config
from traffic.strategy.bfs import BFS

p = Config('examples/simple.json')
bfs = BFS(p)
bfs.start()

for i in range(3):
    p = Config('examples/%s.json' % (i + 1))
    bfs = BFS(p)
    bfs.start()
