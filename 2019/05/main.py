from fileinput import input as f_input
from copy import copy
from operator import add, mul, lt, eq
from functools import partial

def params(array, start, n):
    param_mode = array[start] // 100
    for i in range(start+1, start+1+n):
        yield array[i] if param_mode % 10 else array[array[i]]
        param_mode //= 10
        
operations = { 
    1: (add, 2, 1, False), 
    2: (mul, 2, 1, False), 
    3: (partial(lambda x: int(input(x)), "enter id: "), 0, 1, False),
    4: (print, 1, 0, False),
    5: (lambda x, y: y if x else None, 2, 0, True),
    6: (lambda x, y: None if x else y, 2, 0, True),
    7: (lt, 2, 1, False), 
    8: (eq, 2, 1, False), 
}

def run(array):
    i = 0
    while True:
        op_code = array[i] % 100
        if op_code == 99:
            return
        elif op_code in operations:
            op, n_in, n_out, is_jump = operations[op_code]
            val = op(*params(array, i, n_in))
            if n_out and not is_jump:
                array[array[i+n_in+1]] = val
            i = val if is_jump and val != None else i + n_in + n_out + 1
        else:
            raise(Exception("unexpected opcode {} at i={}".format(op_code, i)))

array = map(int, f_input()[0].split(","))
run(list(array))
