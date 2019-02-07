#!/usr/bin/python

import sys
import re

path = "input.txt"

def day3():
    grid = [[' ' for j in range(1000)] for i in range(1000)]
    for line in open(path):
        id, x, y, lenx, leny = [int(s) for s in re.findall('\d+', line )]
        for i in range(leny):
            for j in range(lenx):
                if grid[x+j][y+i] == ' ':
                    grid[x+j][y+i] = '.'
                elif grid[x+j][y+i] == '.':
                    grid[x+j][y+i] = 'X'
    print(sum(row.count('X') for row in grid))

def day3_2():
    grid = [[[] for j in range(1000)] for i in range(1000)]
    control = []
    for line in open(path):
        id, x, y, lenx, leny = [int(s) for s in re.findall('\d+', line )]
        for i in range(leny):
            for j in range(lenx):
                grid[x+j][y+i].append(id)
        control.append(id)
    for y in range(1000):
        for x in range(1000):
            if len(grid[x][y])>1:
                for item in grid[x][y]:
                    if item in control: control.remove(item)
    print(control)
if __name__ == "__main__":
    day3()
    day3_2()
