from traffic.puzzle import Puzzle
from traffic.bfs import BFS

p = Puzzle('examples/1.json')
bfs = BFS(p)

bfs.start()
