import pandas as pd
import numpy as np


dt = pd.read_csv('MazeR.csv', header=None).to_numpy()
dt[7,1] = -1
ROW = 7
COL = 1
def DFA():
    pass
def BFS():
    pass
def AStar():
    pass
while True:
    print(dt)
    direction = input("Enter the directions (8:U, 2:D, 4:L, 6:R): ")
    if direction == 'U' or direction == '8':
            ROW -= 1
    elif direction == 'D' or direction == '2':
            ROW += 1
    elif direction == 'L' or direction == '4':
            COL -= 1
    elif direction == 'R' or direction == '6':
            COL += 1
    else:
        print("Invalid direction!")
        continue    
    
    
    if dt[ROW, COL] == 1 or dt[ROW,COL] == -1:
        print("Can't move at that")
        if direction == 'U' or direction == '8':
            ROW += 1
        elif direction == 'D' or direction == '2':
            ROW -= 1
        elif direction == 'L' or direction == '4':
            COL += 1
        elif direction == 'R' or direction == '6':
            COL -= 1
        continue
    elif dt[ROW,COL] == 3:
        print("See you, my boy.")
        break
    else:
        dt[ROW, COL] =  -1
    # print(dt)