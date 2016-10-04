from traffic.bfs import BFS
from traffic.puzzle import Puzzle

# Test BFS against the 'simple' 4x4 example only
# as it can't reasonably handle anything more complex.

p = Puzzle('examples/simple.json')
bfs = BFS(p)
bfs.start()
