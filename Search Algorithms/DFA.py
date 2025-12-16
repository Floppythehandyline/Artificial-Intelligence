import pandas as pd
import numpy as np

dt = pd.read_csv('MazeR.csv', header=None).to_numpy()
dt[7,1] = 2 
ROW = 7
COL = 1
while True:
    print(dt)
    direction = input("Enter the directions (8:U, 2:D, 4:L, 6:R): ")
    if direction == 'U':
            ROW -= 1
    elif direction == 'D':
            ROW += 1
    elif direction == 'L':
            COL -= 1
    elif direction == 'R':
            COL += 1
    else:
        print("Invalid direction!")
        continue    
    if dt[ROW, COL] == 1:
        print("Hit a wall!")
        continue
    else:
        dt[ROW, COL] =  4
    # print(dt)