from .astar import AStar
from .bfs import BFS
from .dfs import DFS
from .ids import IDS

strats = {
    'dfs': DFS,
    'bfs': BFS,
    'ids': IDS,
    'astar': AStar,
}
