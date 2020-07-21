#!/usr/bin/python3

from pyrob.api import *


@task
def task_5_10():
    i = 0

    while  True:
        fill_cell()
        while wall_is_on_the_right() == False:
            move_right()
            fill_cell()
            i += 1
        if wall_is_beneath() == True and wall_is_on_the_left() == True and wall_is_on_the_right() == True:
            break
        move_left(i)
        if wall_is_beneath() == True and wall_is_on_the_left() == True:
            break
        move_down()
        i = 0






if __name__ == '__main__':
    run_tasks()
