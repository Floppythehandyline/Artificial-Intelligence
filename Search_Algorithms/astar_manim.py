import heapq

def astar_steps(grid, start, goal):
    ROWS, COLS = grid.shape

    def h(a, b):
        return abs(a[0]-b[0]) + abs(a[1]-b[1])

    open_set = []
    heapq.heappush(open_set, (0, start))

    came_from = {}
    g_score = {start: 0}
    closed = set()

    steps = []

    while open_set:
        _, current = heapq.heappop(open_set)

        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return steps, path[::-1]

        closed.add(current)
        steps.append(current)

        r, c = current
        for dr, dc in [(0,1),(1,0),(0,-1),(-1,0)]:
            nr, nc = r+dr, c+dc
            nxt = (nr, nc)

            if not (0 <= nr < ROWS and 0 <= nc < COLS):
                continue
            if grid[nr, nc] == 1:
                continue
            if nxt in closed:
                continue

            temp_g = g_score[current] + 1
            if nxt not in g_score or temp_g < g_score[nxt]:
                came_from[nxt] = current
                g_score[nxt] = temp_g
                f = temp_g + h(nxt, goal)
                heapq.heappush(open_set, (f, nxt))

    return steps, []
from manim import *
import pandas as pd
import numpy as np

class AStarMaze(Scene):
    def construct(self):
        grid = pd.read_csv("AStar.csv", header=None).to_numpy()
        ROWS, COLS = grid.shape

        # หา start / goal
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r,c] == 2:
                    start = (r,c)
                if grid[r,c] == 3:
                    goal = (r,c)

        steps, path = astar_steps(grid, start, goal)

        cell_size = 0.6
        cells = {}

        grid_width  = COLS * cell_size
        grid_height = ROWS * cell_size

        x_offset = -grid_width / 2 + cell_size / 2
        y_offset =  grid_height / 2 - cell_size / 2

        # วาด grid
        for r in range(ROWS):
            for c in range(COLS):
                color = WHITE
                if grid[r,c] == 1:
                    color = BLACK
                elif (r,c) == start:
                    color = BLUE
                elif (r,c) == goal:
                    color = RED

                rect = Square(
                    side_length=cell_size,
                    fill_color=color,
                    fill_opacity=1,
                    stroke_color=GRAY
                )

                rect.move_to(
                    RIGHT * (c * cell_size + x_offset) +
                    DOWN  * (r * cell_size - y_offset)
                )

                self.add(rect)
                cells[(r,c)] = rect

        self.wait(1)

        # แสดงขั้นตอนค้นหา
        for r,c in steps:
            if (r,c) != start and (r,c) != goal:
                self.play(
                    cells[(r,c)].animate.set_fill(YELLOW),
                    run_time=0.1
                )

        # แสดง path สุดท้าย
        for r,c in path:
            if (r,c) != start and (r,c) != goal:
                self.play(
                    cells[(r,c)].animate.set_fill(GREEN),
                    run_time=0.2
                )

        self.wait(2)
