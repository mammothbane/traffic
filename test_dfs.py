from traffic.dfs import DFS
from traffic.puzzle import Puzzle

p = Puzzle('examples/simple.json')
dfs = DFS(p)
dfs.start()

for i in range(3):
    p = Puzzle('examples/%s.json' % (i + 1))
    dfs = DFS(p)

    dfs.start()
