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


@task
def task_2_2():
    move_down(2)
    for j in range(4):
        krest()
        move_right(3)
        move_down()
    krest()
    move_left()


if __name__ == '__main__':
    run_tasks()
