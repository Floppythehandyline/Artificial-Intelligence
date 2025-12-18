import pandas as pd
import time
from collections import deque
dt = pd.read_csv('AStar.csv', header=None).to_numpy()

ROWS, COLS = dt.shape

for r in range(ROWS):
    for c in range(COLS):
        if dt[r][c] == 3:
            GOAL = (r, c)
            
# Manhattan distance
def h(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def AStar(r, c):
 
    q = deque()
    q.append((start_r, start_c))

    while q:
        r, c = q.popleft()

        if r < 0 or r >= ROWS or c < 0 or c >= COLS:
            continue

        if dt[r, c] == 1 or dt[r, c] == -1:
            continue

        if dt[r, c] == 3:
            print("Found target!")
            return True

        dt[r, c] = -1
        print(dt)
        time.sleep(0.5)

        q.append((r, c+1))  # ขวา
        q.append((r+1, c))  # ล่าง
        q.append((r-1, c))  # บน
        q.append((r, c-1))  # ซ้าย

    print("Target not found")
    return False
start_row = 6
start_col = 0

# AStar(start_row, start_col)
