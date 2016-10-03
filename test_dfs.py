from traffic.dfs import DFS
from traffic.puzzle import Puzzle

for i in range(3):
    p = Puzzle('examples/%s.json' % (i + 1))
    dfs = DFS(p)

    dfs.start()
