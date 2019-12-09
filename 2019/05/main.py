from fileinput import input
from copy import copy
from operator import add, mul

def params(array, start, n):
    param_mode = array[start] // 100
    for i in range(start+1, start+1+n):
        yield array[i] if param_mode % 10 else array[array[i]]
        param_mode //= 10

def run(array):
    i = 0
    while True:
        op = array[i] % 100
        param_mode = array[i] // 100
        if op == 1:
            array[array[i+3]] = add(*params(array, i, 2))
            i += 4
        elif op == 2:
            array[array[i+3]] = mul(*params(array, i, 2))
            i += 4
        elif op == 3:
            print("in: 1 at {}".format(array[i+1]))
            array[array[i+1]] = 1
            i += 2
        elif op == 4:
            x = params(array, i, 1)
            print("out: {} at {}".format(*x, i))
            i += 2
        elif op == 99:
            return
        else:
            raise(Exception("unexpected opcode {} at i={}".format(op, i)))

array = map(int, input()[0].split(","))
run(list(array))
