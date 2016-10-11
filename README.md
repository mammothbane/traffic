## Installation
Requires Python 3. No external dependencies.

## Usage
In general, call into main.py to solve a specific problem:

    python main.py FILE STRATEGY [--heuristic HEURISTIC].

where `FILE` is a JSON-formatted specification file, `STRATEGY` is one of `BFS`, `DFS`, `IDS`, and `ASTAR`, and `HEURISTIC` is a valid heuristic (`car_available_moves`, `manhattan`, `max`, `cars_in_between`, or `available_moves_extended`).

The problem specification files follow a straightforward format, and examples are provided.

To run each of the numbered examples with bfs, for example, one could run:

    python main.py examples/{1, 2, 3}.json BFS
