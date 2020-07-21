#!/usr/bin/python3

from pyrob.api import *

def krest():
    fill_cell()
    for i in range(2):
        move_right()
        fill_cell()
    move_left()
    move_down()
    for i in range(2):
        fill_cell()
        move_up()
    fill_cell()


@task(delay=0.02)
def task_2_4():
    for i in range(4):
        move_down()
        for j in range(9):
            krest()
            move_right(3)
            move_down()
        krest()
        move_left(37)
        move_down(4)
    move_down()
    for j in range(9):
        krest()
        move_right(3)
        move_down()
    krest()
    move_left(37)

if __name__ == '__main__':
    run_tasks()
