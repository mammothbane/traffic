from traffic.config import Config
from traffic.strategy.dfs import DFS

# just a proof of concept, that dfs does actually work. the full 6x6 examples
# are a bit too much for DFS to reasonably explore.

c = Config('examples/simple.json')
dfs = DFS(c)
dfs.start()

