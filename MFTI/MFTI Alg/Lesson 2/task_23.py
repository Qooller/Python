#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_6_6():
    i = 0
    j = 0
    while True:
        while wall_is_on_the_right() == False:
            move_right()
            i += 1
            if wall_is_above() == False:
                while wall_is_above() == False:
                    move_up()
                    j += 1
                    fill_cell()
                move_down(j)
                j = 0
        move_left(i)
        if wall_is_beneath() == False and wall_is_above() == False:
            break
        i = 0


if __name__ == '__main__':
    run_tasks()
