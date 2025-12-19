from collections import deque
import pandas as pd
import time

dt = pd.read_csv('Maze_15x15_complex.csv', header=None).to_numpy()
dt[7,1] = 22   # กำหนดจุดเริ่มต้น
dt[1,12] = 33  # กำหนดเป้าหมาย
ROWS, COLS = dt.shape

def BFS(start_r, start_c):
    q = deque()
    q.append((start_r, start_c))

    while q:
        r, c = q.popleft()
        # กำหนดขอบเขต
        if r < 0 or r >= ROWS or c < 0 or c >= COLS:
            continue
        # กันเดินข้ามกำแพงหรือเดินย้อนหลัง
        if dt[r, c] == 1 or dt[r, c] == -10:
            continue
        # ตรวจสอบเป้าหมาย
        if dt[r, c] == 33:
            print("Found target!")
            return True

        dt[r, c] = -10
        print(dt)
        time.sleep(0.5)

        q.append((r, c+1))  # ขวา
        q.append((r+1, c))  # ล่าง
        q.append((r-1, c))  # บน
        q.append((r, c-1))  # ซ้าย

    print("Target not found")
    return False


BFS(7, 1)
