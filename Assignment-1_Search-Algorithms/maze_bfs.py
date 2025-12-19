from manim import *
import pandas as pd
from collections import deque

class MazeBFS(Scene):
    def construct(self):
        # Load maze (0=path,1=wall,3=target)
        maze = pd.read_csv("MazeR.csv", header=None).to_numpy()
        rows, cols = maze.shape
        cell_size = 0.6

        # Draw grid
        grid = VGroup()
        cells = {}
        for r in range(rows):
            for c in range(cols):
                color = WHITE
                if maze[r, c] == 1:
                    color = GREY
                elif maze[r, c] == 3:
                    color = RED

                sq = Square(side_length=cell_size)
                sq.set_fill(color, opacity=0.8)
                sq.set_stroke(BLACK, 1)
                sq.move_to(
                    RIGHT * (c - cols / 2) * cell_size +
                    UP * (rows / 2 - r) * cell_size
                )
                grid.add(sq)
                cells[(r, c)] = sq

        self.play(Create(grid))
        self.wait(0.5)

        # BFS
        start = (7, 1)
        queue = deque([start])
        visited = set()

        while queue:
            r, c = queue.popleft()
            if (r, c) in visited:
                continue
            visited.add((r, c))

            # Animate visit
            if maze[r, c] == 0:
                self.play(cells[(r, c)].animate.set_fill(BLUE, opacity=0.8), run_time=0.2)
            if maze[r, c] == 3:
                self.play(cells[(r, c)].animate.set_fill(YELLOW, opacity=1), run_time=0.3)
                break

            # Neighbors (R D U L)
            for dr, dc in [(0,1),(1,0),(-1,0),(0,-1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    if maze[nr, nc] != 1 and (nr, nc) not in visited:
                        queue.append((nr, nc))

        self.wait(1)
