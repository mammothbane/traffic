from traffic.config import Config
from traffic.strategy.ids import IDS

# similarly to DFS, this is just to demonstrate that IDS does in fact work.

p = Config('examples/simple.json')
ids = IDS(p)
ids.start()

