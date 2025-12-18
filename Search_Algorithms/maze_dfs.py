from manim import *
import pandas as pd

# ================== LOAD MAZE ==================
dt = pd.read_csv("MazeR.csv", header=None).to_numpy()
ROWS, COLS = dt.shape

# ================== DFS (เก็บ path) ==================
path = []

def DFS(r, c):
    if r < 0 or r >= ROWS or c < 0 or c >= COLS:
        return False
    if dt[r, c] == 1 or dt[r, c] == -1:
        return False

    path.append((r, c))

    if dt[r, c] == 3:
        return True

    dt[r, c] = -1

    return (
        DFS(r, c+1) or
        DFS(r+1, c) or
        DFS(r-1, c) or
        DFS(r, c-1)
    )

DFS(7, 1)

# ================== MANIM ==================
CELL = 0.6

class MazeDFS(Scene):
    def construct(self):
        grid = VGroup()
        rects = {}

        for r in range(ROWS):
            for c in range(COLS):
                color = WHITE
                if dt[r][c] == 1:
                    color = BLACK
                elif dt[r][c] == 3:
                    color = RED

                rect = Square(
                    side_length=CELL,
                    fill_color=color,
                    fill_opacity=0.8,
                    stroke_color=GRAY
                )

                rect.move_to(RIGHT * c * CELL + DOWN * r * CELL)
                rects[(r, c)] = rect
                grid.add(rect)

        grid.center()
        self.play(Create(grid))

        # Animate DFS path
        for r, c in path:
            self.play(
                rects[(r, c)].animate.set_fill(BLUE),
                run_time=0.2
            )

        self.wait(1)
