import math

w, h = [int(i) for i in input().split()]
n = int(input()) # unused but DO NOT remove
x, y = [int(i) for i in input().split()]

x1,y1 = 0,0  # left and upper border of the grid
x2,y2 = w - 1, h - 1 # right and lower border of the grid

while True:
    bdir = input()  # the direction of the bombs from batman's current location (U, UR, R, DR, D, DL, L or UL)

    if ("U" in bdir):
        y2 = y  # updating lower border
        y = int(math.floor(y2 - (y2 - y1)/2))  # updating batman's position
    elif ("D" in bdir):
        y1 = y  # updating upper border
        y = int(math.ceil(y1 + (y2 - y1)/2))  # updating batman's position
    if ("L" in bdir):
        x2 = x  # updating right border
        x = int(math.floor(x2 - (x2 - x1)/2))  # updating batman's position
    elif ("R" in bdir):
        x1 = x  # updating left border
        x = int(math.ceil(x1 + (x2 - x1)/2))  # updating batman's position

    print(f'{x} {y}')
