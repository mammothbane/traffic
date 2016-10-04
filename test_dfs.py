from traffic.puzzle import Puzzle
from traffic.strategy.dfs import DFS

p = Puzzle('examples/simple.json')
dfs = DFS(p)
dfs.start()

for i in range(3):
    p = Puzzle('examples/%s.json' % (i + 1))
    dfs = DFS(p)

    dfs.start()
