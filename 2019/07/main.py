from fileinput import input as f_input
from copy import copy
from operator import add, mul, lt, eq
from itertools import permutations, chain

def params(array, start, n):
    param_mode = array[start] // 100
    for i in range(start+1, start+1+n):
        yield array[i] if param_mode % 10 else array[array[i]]
        param_mode //= 10

def run(array, inputs):
    operations = { 
        1: (add, 2, 1, False), 
        2: (mul, 2, 1, False), 
        3: (None, 0, 1, False),
        4: (None, 1, 0, False),
        5: (lambda x, y: y if x else None, 2, 0, True),
        6: (lambda x, y: None if x else y, 2, 0, True),
        7: (lt, 2, 1, False), 
        8: (eq, 2, 1, False), 
    }

    i = 0
    while True:
        op_code = array[i] % 100

        if op_code == 99:
            return

        if op_code not in operations:
            raise(Exception("unexpected opcode {} at i={}".format(op_code, i)))

        op, n_in, n_out, is_jump = operations[op_code]
        args = list(params(array, i, n_in))

        if op_code == 3:
            intake = next(inputs, None)
            if intake is None:
                return
            array[array[i+1]] = intake

        elif op_code == 4:
            yield args[0]

        else:
            val = op(*args)
            if n_out and not is_jump:
                array[array[i+n_in+1]] = val

        i = val if is_jump and val != None else i + n_in + n_out + 1

def amplify(array, settings):
    for perm in permutations(settings):
        first = [0]

        one = run(copy(array), chain(iter([perm[0]]), iter(first)))
        two = run(copy(array), chain(iter([perm[1]]), one))
        three = run(copy(array), chain(iter([perm[2]]), two))
        four = run(copy(array), chain(iter([perm[3]]), three))
        five = run(copy(array), chain(iter([perm[4]]), four))

        for num in five:
            yield num
            first.append(num)

array = list(map(int, f_input()[0].split(",")))
print(max(amplify(array, range(5))))
print(max(amplify(array, range(5, 10))))
