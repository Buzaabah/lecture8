"""
File: pyramid.py
----------------
YOUR DESCRIPTION HERE
"""


import tkinter
import time
import random
import math
import numpy as np
import matplotlib.pyplot as plt

CANVAS_WIDTH = 600      # Width of drawing canvas in pixels
CANVAS_HEIGHT = 600     # Height of drawing canvas in pixels
BALL_SIZE = 70

def main():
    canvas = make_canvas(CANVAS_WIDTH, CANVAS_HEIGHT, 'Bouncing Ball')
    start_y = 0

    ball = canvas.create_oval(0, start_y, BALL_SIZE, BALL_SIZE, fill='blue', outline='blue')
    change_x = 3
    change_y = 5
    while True:
        # update world
        canvas.move(ball, change_x, change_y)
        if hit_bottom_wall(canvas, ball):
            change_y *= -1

        if hit_left_wall(canvas, ball):
            change_x *= -1

        canvas.update()

        # pause
        time.sleep(1/50.)


def hit_bottom_wall(canvas, ball):
    ball_top_y = get_top_y(canvas, ball)
    return ball_top_y > CANVAS_HEIGHT - BALL_SIZE

def hit_left_wall(canvas, ball):
    ball_left_x = get_left_x(canvas, ball)
    return  ball_left_x > CANVAS_WIDTH - BALL_SIZE
######## These helper methods use "lists" ###########
### Which is a concept you will learn Monday ###########

def get_left_x(canvas, object):
    return canvas.coords(object)[0]

def get_top_y(canvas, object):
    return canvas.coords(object)[1]


######## DO NOT MODIFY ANY CODE BELOW THIS LINE ###########

# This function is provided to you and should not be modified.
# It creates a window that contains a drawing canvas that you
# will use to make your drawings.
def make_canvas(width, height, title):
    """
    DO NOT MODIFY
    Creates and returns a drawing canvas
    of the given int size with a blue border,
    ready for drawing.
    """
    top = tkinter.Tk()
    top.minsize(width=width, height=height)
    top.title(title)
    canvas = tkinter.Canvas(top, width=width + 1, height=height + 1)
    canvas.pack()
    return canvas




if __name__ == '__main__':
    main()
