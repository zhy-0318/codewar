import random
import numpy
import sys


def block(x, y, block_list):
    num = block_list[x][y]
    block_list[x][y] = 9
    if x-1 >= 0 and block_list[x-1][y] == num:
        block(x - 1, y, block_list)
        block_list[x - 1][y] = 9
    if x+1 < 5 and block_list[x+1][y] == num:
        block(x + 1, y, block_list)
        block_list[x + 1][y] = 9
    if y-1 >= 0 and block_list[x][y-1] == num:
        block(x, y - 1, block_list)
        block_list[x][y - 1] = 9
    if y+1 < 5 and block_list[x][y+1] == num:
        block(x, y + 1, block_list)
        block_list[x][y + 1] = 9


if __name__ == "__main__":
    sys.setrecursionlimit(10000)
    size = 5
    block_list = numpy.zeros((size, size))
    for x in range(0, size):
        for y in range(0, size):
            block_list[x][y] = random.randint(0, 2)
    for i in block_list:
        print(i)
    x = random.randint(0, size - 1)
    y = random.randint(0, size - 1)
    print("破坏" + str(x) + "," + str(y) + "处的方块，并连锁破坏")
    block(x, y, block_list)
    for i in block_list:
        print(i)