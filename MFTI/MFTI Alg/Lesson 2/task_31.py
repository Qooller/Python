#!/usr/bin/python3

from pyrob.api import *


# def level():
#    while wall_is_on_the_left() == True:
#        if wall_is_on_the_left() == True:
#            while wall_is_on_the_right() == False:
#                move_right()

#        else:
#            move_left()
#        if wall_is_beneath() == False:
#            while wall_is_above() == False:
#                move_down()


@task(delay=0.01)
def task_8_30():
    i = 0
    while wall_is_on_the_left() == False:
        if wall_is_beneath() == False:
            while wall_is_beneath() == False:
                move_down()
                i = 0
        else:
            move_left()

        if wall_is_on_the_left() == True and i > 1:
            break
        if wall_is_on_the_left() == True:
                while wall_is_on_the_right() == False:
                    move_right()
                    if wall_is_beneath() == False:
                        while wall_is_beneath() == False:
                            move_down()
                            i = 0
                i += 1


if __name__ == '__main__':
    run_tasks()
