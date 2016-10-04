from traffic.bfs import BFS
from traffic.puzzle import Puzzle

p = Puzzle('examples/simple.json')
bfs = BFS(p)
bfs.start()

for i in range(3):
    p = Puzzle('examples/%s.json' % (i + 1))
    bfs = BFS(p)

    bfs.start()
