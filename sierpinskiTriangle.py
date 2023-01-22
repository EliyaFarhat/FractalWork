'''
import random
import matplotlib.pyplot as plt

x = []
y = []
x.append(0)
y.append(0)
pc = 0
lc = 0
curr = 0

for z in range(150000):

    choice = random.randint(1,100)

    if choice == 1:
        x.append(0)
        y.append(0.16 * (y[curr]))
    if choice >= 2 and choice <= 86:
        x.append(0.85 * (x[curr]) + 0.04 * (y[curr]))
        y.append(-0.04 * (x[curr]) + 0.85 * (y[curr]) + 1.6)
    if choice >= 94 and choice <= 100:
        x.append(-0.15 * (x[curr]) + 0.28 * (y[curr]))
        y.append(0.26 * (x[curr]) + 0.24 * (y[curr]) + 0.44)
    if choice >= 87 and choice <= 93:
        x.append(0.2 * (x[curr]) - 0.26 * (y[curr]))
        y.append(0.23 * (x[curr]) + 0.22 * (y[curr]) + 1.6)
    curr += 1

plt.scatter(x, y, s = 0.2, edgecolor= 'green')
plt.show()
'''
import pygame
import math
import sys
import random
pygame.init()

# constants
SCREEN_H = 1000
SCREEN_W = 1000
RANGE = math.pi/6
HALF_RANGE = RANGE/2
WHITE = (255, 255, 255)

# initialize window
win = pygame.display.set_mode((SCREEN_H, SCREEN_H))
pygame.display.set_caption('Sierpinski Triangle')

clock = pygame.time.Clock()


width = SCREEN_W/120
height = SCREEN_H
bn = 27
dt = 6
length = 280
dens = 2.5
REC_LIM = 9
MARGIN = 90
TRI_POINTS_BASE = [(MARGIN, SCREEN_H - MARGIN),
                   (SCREEN_W/2, MARGIN),
                   (SCREEN_W - MARGIN, SCREEN_H - MARGIN)]

def drawTri(points, limit, colour, to):
    if limit <= 0:
        return
    #r = colour[0]
    #g = colour[1]
    #b = colour[2]
    """
    if colour[0] == to[0] and colour[1] < to[1] and colour[2] < to[2]:
        g += bn
        b += bn

    elif colour[0] < to[0] and colour[1] < to[1] and colour[2] < to[2]:
        r += bn
        g += bn
        b += bn
    elif colour[0] > to[0] and colour[1] < to[1] and colour[2] < to[2]:
        r -= bn
        g += bn
        b += bn
    elif colour[0] == to[0] and colour[1] == to[1] and colour[2] < to[2]:
        b += bn

    elif colour[0] == to[0] and colour[1] == to[1] and colour[2] > to[2]:
        b-=bn
    elif colour[0] == to[0] and colour[1] < to[1] and colour[2] == to[2]:
        g += bn
    elif colour[0] == to[0] and colour[1] < to[1] and colour[2] < to[2]:
        g += bn
        b += bn
    elif colour[0] == to[0] and colour[1] > to[1] and colour[2] == to[2]:
        g -= bn
    elif colour[0] == to[0] and colour[1] > to[1] and colour[2] > to[2]:
        b -= bn
        g -= bn
    elif colour[0] == to[0] and colour[1] > to[1] and colour[2] < to[2]:
        g -= bn
        b += bn
    elif colour[0] == to[0] and colour[1] < to[1] and colour[2] > to[2]:
        g += bn
        b -= bn
    elif colour[0] < to[0] and colour[1] == to[1] and colour[2] == to[2]:
        r+=bn
    elif colour[0] < to[0] and colour[1] == to[1] and colour[2] < to[2]:
        r+=bn
        b+=bn
    elif colour[0] > to[0] and colour[1] == to[1] and colour[2] == to[2]:
        r-=bn
    elif colour[0] > to[0] and colour[1] > to[1] and colour[2] == to[2]:
        r-=bn
        g-=bn
    elif colour[0] > to[0] and colour[1] > to[1] and colour[2] > to[2]:
        r-=bn
        g-=bn
        b-=bn
    elif colour[0] > to[0] and colour[1] < to[1] and colour[2] == to[2]:
        r-=bn
        g+=bn
    elif colour[0] > to[0] and colour[1] > to[1] and colour[2] < to[2]:
        r -= bn
        g -= bn
        b += bn
    elif colour[0] > to[0] and colour[1] == to[1] and colour[2] < to[2]:
        r-=bn
        b+=bn
    elif colour[0] < to[0] and colour[1] > to[1] and colour[2] < to[2]:
        r+=bn
        g-=bn
        b+=bn
    elif colour[0] > to[0] and colour[1] < to[1] and colour[2] > to[2]:
        r -=bn
        g+=bn
        b-=bn

    elif colour[0] > to[0] and colour[1] == to[1] and colour[2] > to[2]:
        r-=bn
        b-=bn
    elif colour[0] < to[0] and colour[1] > to[1] and colour[2] < to[2]:
        r+=bn
        g-=bn
        b+=bn
    elif colour[0] < to[0] and colour[1] > to[1] and colour[2] == to[2]:
        r+=bn
        g-=bn

    elif colour[0] < to[0] and colour[1] > to[1] and colour[2] > to[2]:
        r+=bn
        g-=bn
        b-=bn
    elif colour[0] < to[0] and colour[1] == to[1] and colour[2] > to[2]:
        r+=bn
        b-=bn
    elif colour[0] < to[0] and colour[1] < to[1] and colour[2] > to[2]:
        r+=bn
        g+=bn
        b-=bn
    elif colour[0] < to[0] and colour[1] < to[1] and colour[2] == to[2]:
        r+=bn
        g+=bn

    if len(colour) < 3 or len(colour) > 3:
        return "INVALID COLOUR VALUES"
    if colour[0] > 255:
        colour[0] = 255
    if colour[1] > 255:
        colour[1] = 255
    if colour[2] > 255:
        colour[2] = 255
    if colour[0] < 0:
        colour[0] = 0
    if colour[1] < 0:
        colour[1] = 0
    if colour[2] < 0:
        colour[2] = 0
    if colour[0] >= (to[0] - bn) and colour[0] <= (to[0] + bn):
        colour[0] = to[0]
    if colour[1] >= (to[1] - bn) and colour[1] <= (to[1] + bn):
        colour[1] = to[1]
    if colour[2] >= (to[2] - bn) and colour[2] <= (to[2] + bn):
        colour[2] = to[2]
    """
    # Uncomment for a mess :p
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    pygame.draw.line(win, (r,g,b), points[0], points[1])
    pygame.draw.line(win, (r,g,b), points[1], points[2])
    pygame.draw.line(win, (r,g,b), points[2], points[0])

    A = points[0]
    B = points[1]
    C = points[2]

    AB = ((A[0] + B[0])/2, (A[1] + B[1])/2)
    AC = ((A[0] + C[0]) / 2, (A[1] + C[1]) / 2)
    BC = ((C[0] + B[0]) / 2, (C[1] + B[1]) / 2)
    drawTri([A, AB, AC], limit - 1, [r, g, b], to)
    drawTri([AB, B, BC], limit - 1, [r, g, b], to)
    drawTri([AC, BC, C], limit - 1, [r, g, b], to)









while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
    win.fill((0,0,0))
    drawTri(TRI_POINTS_BASE, REC_LIM, [255,0,0], [0,0,255])






    pygame.display.update()

