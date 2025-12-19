import pandas as pd
import time

dt = pd.read_csv('MazeR.csv', header=None).to_numpy()
dt[7,1] = 22   # กำหนดจุดเริ่มต้น
dt[1,12] = 33  # กำหนดเป้าหมาย
ROWS, COLS = dt.shape

def DFS(r, c):
 
    # กำหนดขอบเขต
    if r < 0 or r >= ROWS or c < 0 or c >= COLS:
        return False
    # กันเดินข้ามกำแพงหรือเดินย้อนหลัง
    if dt[r, c] == 1 or dt[r, c] == -10:
        return False
    # ตรวจสอบเป้าหมาย
    if dt[r, c] == 33:
        print("Found target!")
        return True

    dt[r, c] = -10
    print(dt)
    time.sleep(0.5)

    if (DFS(r, c+1) or # ขวา
        DFS(r+1, c) or # ล่าง
        DFS(r-1, c) or # บน
        DFS(r, c-1)):  # ซ้าย
        return True

    return False
start_row = 7
start_col = 1

DFS(start_row, start_col)
