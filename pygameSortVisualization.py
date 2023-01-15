import pygame as pg

# screen size
width = 1200
height = 800
screen = pg.display.set_mode((width,height))
# initialize pygame and screen
pg.init()

#function to draw a single bar
def draw_bar(arr, i, color = pg.Color('Cyan')):
    w, h = screen.get_size()
    n = len(arr)
    bar_w = w / n
    bar_h = h // n * arr[i]
    x = i * bar_w
    y = h - bar_h
    pg.draw.rect(screen, color, pg.Rect(x, y, bar_w, bar_h))

# function to visualize an entire array using a bar chart
def draw_bars(arr, sel, cmp, piv):
    screen.fill(pg.Color('Black'))
    if type(sel) == int:
        sel=[sel]
    if type(cmp) == int:
        cmp=[cmp]
    if type(piv) == int:
        piv=[piv]
    for i in range(len(arr)):
        if i in sel:
            draw_bar(arr, i, pg.Color('Red'))
        elif i in cmp:
            draw_bar(arr, i, pg.Color('Orange'))
        elif i in piv:
            draw_bar(arr, i, pg.Color('Green'))
        else:
            draw_bar(arr, i)

#function to visualize and refresh screen
CHANGE_PERIOD = 1000
def display_flip(arr, sel=-1, cmp=-1, piv=-1, time = CHANGE_PERIOD):
    draw_bars(arr, sel, cmp, piv)
    pg.display.flip()
    pg.time.wait(time)

#function to stop screen
def end_screen():
    close = False
    while close == False:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                close = True
        pg.time.wait(1000)

#function to check sort result
def check_sort(arr):
    for i in range(len(arr)):
        if i<len(arr)-1 and arr[i]>arr[i+1]: #wrong order
            display_flip(arr, i, i+1) #highlight error
            end_screen() #stop the screen
        display_flip(arr, piv = i, time = 200)

DEFAULT_ARR_SIZE = 10