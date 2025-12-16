import pandas as pd
import time

dt = pd.read_csv('MazeR.csv', header=None).to_numpy()

ROWS, COLS = dt.shape

def DFS(r, c):
 
    if r < 0 or r >= ROWS or c < 0 or c >= COLS:
        return False

    if dt[r, c] == 1 or dt[r, c] == -1:
        return False

    if dt[r, c] == 3:
        print("🎯 Found target!")
        return True

    dt[r, c] = -1
    print(dt)
    time.sleep(0.5)

    if (DFS(r, c+1) or
        DFS(r+1, c) or
        DFS(r-1, c) or
        DFS(r, c-1)):
        return True

    return False
start_row = 7
start_col = 1

DFS(start_row, start_col)
