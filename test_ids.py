from traffic.puzzle import Puzzle
from traffic.strategy.ids import IDS

# similarly to DFS, this is just to demonstrate that IDS does in fact work.

p = Puzzle('examples/simple.json')
ids = IDS(p)
ids.start()

