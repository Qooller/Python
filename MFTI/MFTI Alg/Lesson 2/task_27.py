#!/usr/bin/python3

from pyrob.api import *


@task
def task_7_5():
    i = 0
    move_right()
    while wall_is_on_the_right() == False:
        fill_cell()
        for j in range(1+i):
            move_right()
            if wall_is_on_the_right() == True:
                break
        i += 1


if __name__ == '__main__':
    run_tasks()
