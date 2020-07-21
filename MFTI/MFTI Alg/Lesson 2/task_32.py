#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.1)
def task_8_18():
    i = 0
    j = 0
    while True:
        while wall_is_on_the_right() == False:
            if wall_is_beneath() == True and wall_is_above() == True:
                fill_cell()
                i += 1
            move_right()
            if wall_is_beneath() == False and wall_is_above() == False:
                break
            if wall_is_above() == False:
                while wall_is_above() == False:
                    move_up()
                    j += 1
                    if cell_is_filled() == False:
                        fill_cell()
                        i += 1
                move_down(j)
                j = 0

        print(i)
        if wall_is_beneath() == False and wall_is_above() == False:
            break




if __name__ == '__main__':
    run_tasks()
