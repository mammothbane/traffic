from traffic.bfs import BFS
from traffic.puzzle import Puzzle

for i in range(3):
    p = Puzzle('examples/%s.json' % (i + 1))
    bfs = BFS(p)

    bfs.start()
