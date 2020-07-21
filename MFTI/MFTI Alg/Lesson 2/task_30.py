#!/usr/bin/python3

from pyrob.api import *

def circul(m):
    for i in range(1,m):
        move_down()
        if i == m-1:
            continue
        fill_cell()
    for i in range(1, m):
        move_left()
        if i == m-1:
            continue
        fill_cell()
    for i in range(1,m):
        move_up()
        if i == m-1:
            continue
        fill_cell()
    for i in range(1, m):
        move_right()
        if i == m-1:
            continue
        fill_cell()


@task(delay=0.05)
def task_9_3():
    n = 1
    tmp = 0
    while wall_is_on_the_right() == False:
        move_right()
        n += 1
    tmp = n
    while n != 1:
        circul(n)
        move_down()
        move_left()
        n = n-2
        if n == 1:
            for j in range(int((tmp - 1)/2)):
                move_down()
                move_left()
        if wall_is_beneath() == True and wall_is_on_the_left() == True:
            break





if __name__ == '__main__':
    run_tasks()
