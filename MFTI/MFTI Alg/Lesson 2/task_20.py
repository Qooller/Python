#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.05)
def task_4_3():
    move_right()
    for i in range(12):
        for j in range(27):
            if i % 2 == 0:
                fill_cell()
                move_right()
            elif i % 2 == 1:
                fill_cell()
                move_left()
        if i % 2 == 0:
            move_down()
            move_left()
        elif i % 2 == 1:
            move_down()
            move_right()


if __name__ == '__main__':
    run_tasks()
