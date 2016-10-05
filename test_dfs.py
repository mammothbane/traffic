from traffic.config import Config
from traffic.strategy.dfs import DFS

c = Config('examples/simple.json')
dfs = DFS(c)
dfs.start()

for i in range(3):
    c = Config('examples/%s.json' % (i + 1))
    dfs = DFS(c)
    dfs.start()
