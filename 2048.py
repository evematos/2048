#By @coding.eve

from turtle import *
from random import randint

title("2048")
gz = 176
N = 4
bc = gz * N 
tracer(False) 
bgcolor("gray")
ht()
up()
speed(0)
shape("square")
shapesize(8) 

grid = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]

maxx = 2
steps = 0
tj = Turtle()
tj.speed(0)
tj.up()
tj.ht()
tj.color("white")
tj.goto(-bc / 2, bc / 2 + 20)
tj.write("Contagem de passos: {} | valor máximo：{}".format(steps, maxx), font=("", 20, ""))

COLORS = {
    0: "white",
    2: "yellow",
    4: "orange",
    8: "pink",
    16: "red",
    32: "lightblue",
    64: "lightgreen",
    128: "green",
    256: "purple",
    512: "cyan",
    1024: "silver",
    2048: "gold"
}


def draw_grid():
    global steps
    global maxx
    tj.clear()
    tj.write("             Contagem de passos: {} | valor máximo：{}".format(steps, maxx), font=("", 20, ""))
    steps += 1
    clear()
    for row in range(N):
        for col in range(N):
            goto(-bc / 2 + gz / 2 + col * gz, bc / 2 - gz / 2 - row * gz)
            color(COLORS[grid[row][col]])
            stamp()
            sety(bc / 2 - gz / 2 - row * gz - 30)
            color("black")
            if grid[row][col] > 0:
                write(grid[row][col], font=("", 50, ""), align="center")
    
            if grid[row][col] > maxx:
                maxx = grid[row][col]

    update()
    if maxx == 2048:
        goto(0, 0)
        color("red")
        write("vitória do jogo", font=("", 100, ""), align="center")


def can_add():
    for i in range(N):
        for j in range(N):
            if grid[i][j] == 0:
                return True
    return False


def generate_random():

    if can_add():
        added = False
    
        while not added:
            i = randint(0, N - 1)
            j = randint(0, N - 1)
            if grid[i][j] == 0:
                grid[i][j] = 2
                added = True

generate_random()
draw_grid()

def up():

    for col in range(N):
        for row in range(1, N):
            value = grid[row][col]
            r = row
            while r > 0 and grid[r - 1][col] == 0:
                r = r - 1
            if r - 1 >= 0 and grid[r - 1][col] == value:
                r = r - 1
            if r != row:
                grid[r][col] += value
                grid[row][col] = 0 

    generate_random()
    draw_grid()

def down():
    for col in range(N):
        for row in range(N - 2, -1, -1):
            value = grid[row][col]
            r = row
            while r < N - 1 and grid[r + 1][col] == 0:
                r = r + 1
            if r + 1 < N and grid[r + 1][col] == value:
                r = r + 1
            if r != row:
                grid[r][col] += value
                grid[row][col] = 0
    generate_random()
    draw_grid()

def left():
    for row in range(N):
        for col in range(1, N):
            value = grid[row][col]
            c = col
            while c > 0 and grid[row][c - 1] == 0:
                c = c - 1
            if c - 1 >= 0 and grid[row][c - 1] == value:
                c = c - 1
            if c != col:
                grid[row][c] += value
                grid[row][col] = 0
    generate_random()
    draw_grid()

def right():
    for row in range(N):
        for col in range(N - 2, -1, -1):
            value = grid[row][col]
            c = col
            while c < N - 1 and grid[row][c + 1] == 0:
                c = c + 1
            if c + 1 < N and grid[row][c + 1] == value:
                c = c + 1
            if c != col:
                grid[row][c] += value
                grid[row][col] = 0
    generate_random()
    draw_grid()

onkeypress(up, "Up")  
onkeypress(down, "Down")  
onkeypress(left, "Left")  
onkeypress(right, "Right")  
listen()  

done()

#By @coding.eve