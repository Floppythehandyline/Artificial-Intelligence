import pandas as pd
import heapq
import time

# ===== Load maze =====
dt = pd.read_csv('AStar.csv', header=None).to_numpy()
ROWS, COLS = dt.shape

# ===== Find goal =====
for r in range(ROWS):
    for c in range(COLS):
        if dt[r, c] == 3:
            GOAL = (r, c)

# ===== Heuristic (Manhattan) =====
def h(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

# ===== Reconstruct path =====
def reconstruct_path(came_from, current):
    path = [current]
    while current in came_from:
        current = came_from[current]
        path.append(current)
    return path[::-1]

# ===== A* =====
def AStar(start):
    open_set = []
    heapq.heappush(open_set, (0, start))

    came_from = {}

    g_score = {start: 0}
    f_score = {start: h(start, GOAL)}

    closed_set = set()

    while open_set:
        _, current = heapq.heappop(open_set)

        if current == GOAL:
            print("🎯 Found target!")
            return reconstruct_path(came_from, current)

        closed_set.add(current)

        r, c = current
        for dr, dc in [(0,1),(1,0),(0,-1),(-1,0)]:
            nr, nc = r + dr, c + dc
            neighbor = (nr, nc)

            # ขอบเขต
            if not (0 <= nr < ROWS and 0 <= nc < COLS):
                continue
            # กำแพง
            if dt[nr, nc] == 1:
                continue
            # เคยปิดแล้ว
            if neighbor in closed_set:
                continue

            tentative_g = g_score[current] + 1

            if neighbor not in g_score or tentative_g < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g
                f_score[neighbor] = tentative_g + h(neighbor, GOAL)
                heapq.heappush(open_set, (f_score[neighbor], neighbor))

    print("❌ No path found")
    return None
start = (6, 0)
path = AStar(start)

if path:
    for r, c in path:
        if dt[r, c] == 0:
            dt[r, c] = -1
        print(dt)
        time.sleep(0.3)
