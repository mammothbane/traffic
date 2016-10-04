import argparse

from traffic.config import Config
from traffic.heuristic import heuristics
from traffic.strategy import strats


parser = argparse.ArgumentParser(description='Solve a traffic puzzle.')
parser.add_argument('file', metavar='FILE', help='json problem definition file')
parser.add_argument('strategy', metavar='STRATEGY', help='search strategy to use')
parser.add_argument('--heuristic', metavar='HEURISTIC', help='heuristic to use (specify when using A*)')
args = parser.parse_args()

config = Config(args.file)
strategy = strats[args.strategy.lower()]

if args.strategy.lower() == 'astar':
    h = heuristics[args.heuristic]
    strategy(config, h).start()
else:
    strategy(config).start()

