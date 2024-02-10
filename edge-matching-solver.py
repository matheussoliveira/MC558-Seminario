"""
Edge Matching Puzzle Formulation for the PuLP Modeller

-- Decision Variables --
tiles: binary representing if the tile with ID is positioned at (x, y)
colored: there are four side of each tile and one color representing each side

-- Constraints --
1. Each tile appears once.
2. In each position there is only one tile.
3. Colors between shared side of adjacent tiles must be the same.

"""
from pulp import *

BOARD_SIZE = 2

# Color of pieces
COLORS = range(0, 2)
SIDE = range(0, 4)

# Coord and up side color
x = y = range(0, BOARD_SIZE)

board = [[[0, 1, 0, 1] for _ in x] for _ in y]
print(board)

# ID
i = BOARD_SIZE * BOARD_SIZE
ID = range(1, i+1)

prob = LpProblem("edgeMatchingPuzzle", LpMaximize)

colored = LpVariable.dicts("Color", (ID, SIDE, COLORS), cat="Binary")

tiles = LpVariable.dicts("Tile", (x, y, ID), cat="Binary")

print(tiles[0][0][1])

for i in x:
    for j in y:
        print(tiles[i][j])

# 1. Each tile appears once.
for k in ID:
    prob += lpSum(tiles[i][j][k] for i in x for j in y) == 1

# 2. In each position there is only one tile.
for i in x:
    for j in y:
        prob += lpSum(tiles[i][j][k] for k in ID) == 1

# TODO 3. Colors between shared side of adjacent tiles must be the same.

# Solving the problem
prob.solve()

# Printing the solution
for i in x:
    for j in y:
        for k in ID:
            if value(tiles[i][j][k]) == 1:
                print("Tile at ({},{}) with ID {}".format(i, j, k))