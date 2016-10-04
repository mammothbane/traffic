import argparse

from traffic.bfs import BFS
from traffic.dfs import DFS
from traffic.ids import IDS
from traffic.puzzle import Puzzle


parser = argparse.ArgumentParser(description='Solve a traffic puzzle.')
parser.add_argument('file', metavar='FILE', help='json problem definition file')
parser.add_argument('strategy', metavar='STRATEGY', help='search strategy to use')
args = parser.parse_args()

puzzle = Puzzle(args.file)
strategy = {
    'bfs': BFS,
    'ids': IDS,
    'dfs': DFS
}[args.strategy.lower()]

strategy(puzzle).start()

