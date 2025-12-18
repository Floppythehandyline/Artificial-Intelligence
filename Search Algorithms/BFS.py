from collections import deque
import pandas as pd
import time

dt = pd.read_csv('MazeR.csv', header=None).to_numpy()
ROWS, COLS = dt.shape

def BFS(start_r, start_c):
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


BFS(7, 1)
