from traffic.config import Config
from traffic.strategy.ids import IDS

c = Config('examples/simple.json')
ids = IDS(c)
ids.start()

for i in range(3):
    c = Config('examples/%s.json' % (i + 1))
    ids = IDS(c)
    ids.start()
