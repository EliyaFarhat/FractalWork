import pygame
import math
import sys
pygame.init()

# constants
SCREEN_H = 1000
SCREEN_W = 1000
RANGE = math.pi/2
HALF_RANGE = RANGE/2
WHITE = (255, 255, 255)

# initialize window
win = pygame.display.set_mode((SCREEN_H, SCREEN_H))
pygame.display.set_caption('"Binary" Tree (Fractals)')

clock = pygame.time.Clock()


width = SCREEN_W/120
height = SCREEN_H
bn = 20
dt = 6
length = 280
dens = 2.5

def drawBranch(screen, x, y, length, RANGE, colour: list, to: list):
    if length <= dens:
        return
    r = colour[0]
    g = colour[1]
    b = colour[2]
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



    x2 = x - length * math.cos(RANGE)
    y2 = y - length * math.sin(RANGE)

    pygame.draw.line(win, (r, g, b), (x, y), (x2, y2), width=2)

    if colour[0] == to[0] and colour[1] < to[1] and colour[2] < to[2]:
        drawBranch(screen, x2, y2, length * 0.67, RANGE + (math.pi / dt), [r, g + bn, b + bn], to)
        drawBranch(screen, x2, y2, length * 0.67, RANGE - (math.pi / dt/2), [r, g + bn, b + bn],to)
    elif colour[0] < to[0] and colour[1] < to[1] and colour[2] < to[2]:
        drawBranch(screen, x2, y2, length * 0.67, RANGE + (math.pi / dt), [r+bn, g + bn, b + bn],to)
        drawBranch(screen, x2, y2, length * 0.67, RANGE - (math.pi / dt/2), [r+bn, g + bn, b + bn],to)
    elif colour[0] > to[0] and colour[1] < to[1] and colour[2] < to[2]:
        drawBranch(screen, x2, y2, length * 0.67, RANGE + (math.pi / dt), [r - bn, g + bn, b + bn],to)
        drawBranch(screen, x2, y2, length * 0.67, RANGE - (math.pi / dt/2), [r - bn, g + bn, b + bn],to)
    elif colour[0] == to[0] and colour[1] == to[1] and colour[2] < to[2]:
        drawBranch(screen, x2, y2, length * 0.67, RANGE + (math.pi / dt), [r, g, b + bn],to)
        drawBranch(screen, x2, y2, length * 0.67, RANGE - (math.pi / dt/2), [r, g, b + bn],to)
    elif colour[0] == to[0] and colour[1] == to[1] and colour[2] > to[2]:
        drawBranch(screen, x2, y2, length * 0.67, RANGE + (math.pi / dt), [r, g, b - bn], to)
        drawBranch(screen, x2, y2, length * 0.67, RANGE - (math.pi / dt/2), [r, g, b - bn], to)
    elif colour[0] == to[0] and colour[1] == to[1] and colour[2] == to[2]:
        drawBranch(screen, x2, y2, length * 0.67, RANGE + (math.pi / dt), [r, g, b], to)
        drawBranch(screen, x2, y2, length * 0.67, RANGE - (math.pi / dt/2), [r, g, b], to)
    elif colour[0] == to[0] and colour[1] < to[1] and colour[2] == to[2]:
        drawBranch(screen, x2, y2, length * 0.67, RANGE + (math.pi / dt), [r, g + bn, b], to)
        drawBranch(screen, x2, y2, length * 0.67, RANGE - (math.pi / dt/2), [r, g + bn, b], to)
    elif colour[0] == to[0] and colour[1] < to[1] and colour[2] < to[2]:
        drawBranch(screen, x2, y2, length * 0.67, RANGE + (math.pi / dt), [r, g + bn, b+bn], to)
        drawBranch(screen, x2, y2, length * 0.67, RANGE - (math.pi / dt/2), [r, g + bn, b+bn], to)
    elif colour[0] == to[0] and colour[1] > to[1] and colour[2] == to[2]:
        drawBranch(screen, x2, y2, length * 0.67, RANGE + (math.pi / dt), [r, g - bn, b], to)
        drawBranch(screen, x2, y2, length * 0.67, RANGE - (math.pi / dt/2), [r, g - bn, b], to)
    elif colour[0] == to[0] and colour[1] > to[1] and colour[2] > to[2]:
        drawBranch(screen, x2, y2, length * 0.67, RANGE + (math.pi / dt), [r, g - bn, b-bn], to)
        drawBranch(screen, x2, y2, length * 0.67, RANGE - (math.pi / dt/2), [r, g - bn, b-bn], to)
    elif colour[0] == to[0] and colour[1] > to[1] and colour[2] < to[2]:
        drawBranch(screen, x2, y2, length * 0.67, RANGE + (math.pi / dt), [r, g - bn, b+bn], to)
        drawBranch(screen, x2, y2, length * 0.67, RANGE - (math.pi / dt/2), [r, g - bn, b+bn], to)
    elif colour[0] == to[0] and colour[1] < to[1] and colour[2] > to[2]:
        drawBranch(screen, x2, y2, length * 0.67, RANGE + (math.pi / dt), [r, g + bn, b-bn], to)
        drawBranch(screen, x2, y2, length * 0.67, RANGE - (math.pi / dt/2), [r, g + bn, b-bn], to)
    elif colour[0] < to[0] and colour[1] == to[1] and colour[2] == to[2]:
        drawBranch(screen, x2, y2, length * 0.67, RANGE + (math.pi / dt), [r+bn, g, b], to)
        drawBranch(screen, x2, y2, length * 0.67, RANGE - (math.pi / dt/2), [r+bn, g , b], to)
    elif colour[0] < to[0] and colour[1] == to[1] and colour[2] < to[2]:
        drawBranch(screen, x2, y2, length * 0.67, RANGE + (math.pi / dt), [r+bn, g, b+bn], to)
        drawBranch(screen, x2, y2, length * 0.67, RANGE - (math.pi / dt/2), [r+bn, g, b+bn], to)
    elif colour[0] > to[0] and colour[1] == to[1] and colour[2] == to[2]:
        drawBranch(screen, x2, y2, length * 0.67, RANGE + (math.pi / dt), [r-bn, g, b], to)
        drawBranch(screen, x2, y2, length * 0.67, RANGE - (math.pi / dt/2), [r-bn, g, b], to)
    elif colour[0] > to[0] and colour[1] > to[1] and colour[2] == to[2]:
        drawBranch(screen, x2, y2, length * 0.67, RANGE + (math.pi / dt), [r-bn, g-bn, b], to)
        drawBranch(screen, x2, y2, length * 0.67, RANGE - (math.pi / dt/2), [r-bn, g-bn, b], to)
    elif colour[0] > to[0] and colour[1] > to[1] and colour[2] > to[2]:
        drawBranch(screen, x2, y2, length * 0.67, RANGE + (math.pi / dt), [r-bn, g-bn, b-bn], to)
        drawBranch(screen, x2, y2, length * 0.67, RANGE - (math.pi / dt/2), [r-bn, g-bn, b-bn], to)
    elif colour[0] > to[0] and colour[1] < to[1] and colour[2] == to[2]:
        drawBranch(screen, x2, y2, length * 0.67, RANGE + (math.pi / dt), [r-bn, g+bn, b], to)
        drawBranch(screen, x2, y2, length * 0.67, RANGE - (math.pi / dt/2), [r-bn, g+bn, b], to)
    elif colour[0] > to[0] and colour[1] > to[1] and colour[2] < to[2]:
        drawBranch(screen, x2, y2, length * 0.67, RANGE + (math.pi / dt), [r-bn, g-bn, b+bn], to)
        drawBranch(screen, x2, y2, length * 0.67, RANGE - (math.pi / dt/2), [r-bn, g-bn, b+bn], to)
    elif colour[0] > to[0] and colour[1] == to[1] and colour[2] < to[2]:
        drawBranch(screen, x2, y2, length * 0.67, RANGE + (math.pi / dt), [r-bn, g, b+bn], to)
        drawBranch(screen, x2, y2, length * 0.67, RANGE - (math.pi / dt/2), [r-bn, g, b+bn], to)
    elif colour[0] < to[0] and colour[1] > to[1] and colour[2] < to[2]:
        drawBranch(screen, x2, y2, length * 0.67, RANGE + (math.pi / dt), [r+bn, g-bn, b+bn], to)
        drawBranch(screen, x2, y2, length * 0.67, RANGE - (math.pi / dt/2), [r+bn, g-bn, b+bn], to)
    elif colour[0] > to[0] and colour[1] < to[1] and colour[2] > to[2]:
        drawBranch(screen, x2, y2, length * 0.67, RANGE + (math.pi / dt), [r-bn, g+bn, b-bn], to)
        drawBranch(screen, x2, y2, length * 0.67, RANGE - (math.pi / dt/2), [r-bn, g+bn, b-bn], to)
    elif colour[0] > to[0] and colour[1] == to[1] and colour[2] > to[2]:
        drawBranch(screen, x2, y2, length * 0.67, RANGE + (math.pi / dt), [r-bn, g, b-bn], to)
        drawBranch(screen, x2, y2, length * 0.67, RANGE - (math.pi / dt/2), [r-bn, g, b-bn], to)
    elif colour[0] < to[0] and colour[1] > to[1] and colour[2] < to[2]:
        drawBranch(screen, x2, y2, length * 0.67, RANGE + (math.pi / dt), [r+bn, g-bn, b+bn], to)
        drawBranch(screen, x2, y2, length * 0.67, RANGE - (math.pi / dt/2), [r+bn, g-bn, b+bn], to)
    elif colour[0] < to[0] and colour[1] > to[1] and colour[2] == to[2]:
        drawBranch(screen, x2, y2, length * 0.67, RANGE + (math.pi / dt), [r + bn, g - bn, b], to)
        drawBranch(screen, x2, y2, length * 0.67, RANGE - (math.pi / dt/2), [r + bn, g - bn, b], to)
    elif colour[0] < to[0] and colour[1] > to[1] and colour[2] > to[2]:
        drawBranch(screen, x2, y2, length * 0.67, RANGE + (math.pi / dt), [r + bn, g - bn, b-bn], to)
        drawBranch(screen, x2, y2, length * 0.67, RANGE - (math.pi / dt/2), [r + bn, g - bn, b-bn], to)
    elif colour[0] < to[0] and colour[1] == to[1] and colour[2] > to[2]:
        drawBranch(screen, x2, y2, length * 0.67, RANGE + (math.pi / dt), [r + bn, g, b-bn], to)
        drawBranch(screen, x2, y2, length * 0.67, RANGE - (math.pi / dt/2), [r + bn, g, b-bn], to)
    elif colour[0] < to[0] and colour[1] < to[1] and colour[2] > to[2]:
        drawBranch(screen, x2, y2, length * 0.67, RANGE + (math.pi / dt), [r + bn, g+bn, b - bn], to)
        drawBranch(screen, x2, y2, length * 0.67, RANGE - (math.pi / dt/2), [r + bn, g+bn, b - bn], to)
    elif colour[0] < to[0] and colour[1] < to[1] and colour[2] == to[2]:
        drawBranch(screen, x2, y2, length * 0.67, RANGE + (math.pi / dt), [r + bn, g+bn, b], to)
        drawBranch(screen, x2, y2, length * 0.67, RANGE - (math.pi / dt/2), [r + bn, g+bn, b], to)
import random
r = random.randint(0,255)
g = random.randint(0,255)
b = random.randint(0,255)
r1 = random.randint(0,255)
g1 = random.randint(0,255)
b1 = random.randint(0,255)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
    x1 = 396
    y1 = 615.38

    win.fill((0, 0, 0))
    r += 0.2
    g += 0.2
    b += 0.2
    if r >= 255:
        r = random.randint(0,255)
    if g >= 255:
        g = random.randint(0,255)
    if b >= 255:
        b = random.randint(0,255)
    r1 += 0.2
    g1 += 0.2
    b1 += 0.2
    if r1 >= 255:
        r1 = random.randint(0, 255)
    if g1 >= 255:
        g1 = random.randint(0, 255)
    if b1 >= 255:
        b1 = random.randint(0, 255)
    drawBranch(win, 500, 1000, length, RANGE, [r, g, b], [r1, g1, b1])


    x,y = pygame.mouse.get_pos()
    if x == 0:
        x = 1
    dt = (x/80)



    pygame.display.flip()