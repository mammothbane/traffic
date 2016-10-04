import argparse

from traffic.puzzle import Puzzle
from traffic.strategy import strats


parser = argparse.ArgumentParser(description='Solve a traffic puzzle.')
parser.add_argument('file', metavar='FILE', help='json problem definition file')
parser.add_argument('strategy', metavar='STRATEGY', help='search strategy to use')
args = parser.parse_args()

puzzle = Puzzle(args.file)
strategy = strats[args.strategy.lower()]

strategy(puzzle).start()

