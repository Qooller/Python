#!/usr/bin/python3

from pyrob.api import *


@task
def task_2_1():
    move_down(2)
    for i in range(3):
        move_right()
        fill_cell()
    move_left()
    move_down()
    for i in range(2):
        fill_cell()
        move_up()
    fill_cell()
    move_left()


if __name__ == '__main__':
    run_tasks()
