import random
from math import sin, cos

WIDTH  = 500
HEIGHT = 310

x, y = WIDTH / 2, HEIGHT / 2

pm              = 40
paddle1         = Actor('paddle')
paddle1.center  = pm, HEIGHT / 2
paddle2         = Actor('paddle')
paddle2.center  = WIDTH - pm, HEIGHT / 2
ball            = Actor('ball')
ball.center     = x, y
divider         = Actor('divider')
divider.center  = WIDTH / 2, HEIGHT / 2
direction       = random.randint(0, 360)
print(direction)

def draw():
    screen.fill((0, 0, 0))
    divider.draw()
    ball.draw()
    paddle1.draw()
    paddle2.draw()

def update():
    global x, y, direction
    for pos in range(paddle1.topright[1], paddle1.bottomright[1]):
        if ball.collidepoint(paddle1.topright[0], pos):
            direction += 180
            x += (sin(direction))
            y += (cos(direction))
            ball.center = x, y
    for pos in range(paddle2.topleft[1], paddle2.bottomleft[1]):
        if ball.collidepoint(paddle2.topleft[0], pos):
            direction += 180
            x += (sin(direction))
            y += (cos(direction))
            ball.center = x, y
    if ball.midtop[1] == 0 or ball.midbottom[1] == HEIGHT:
        direction += 180
        x += (sin(direction))
        y += (cos(direction))
    elif ball.midleft[0] == 0 or ball.midright[0] == WIDTH:
        direction += 180
        x += (sin(direction))
        y += (cos(direction))
        x, y = WIDTH / 2, HEIGHT / 2
    else:
        x += (sin(direction))
        y += (cos(direction))
    ball.center = x, y
    if ball.center[1] > paddle2.center[1]:
        paddle2.center = WIDTH - pm, paddle2.center[1] + 1
    elif ball.center[1] < paddle2.center[1]:
        paddle2.center = WIDTH - pm, paddle2.center[1] - 1

def on_mouse_move(pos):
    paddle1.center = pm, pos[1]
