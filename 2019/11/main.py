from fileinput import input as f_input
from itertools import repeat

class IntCode(object):
    def __init__(self, memory):
        self.memory = memory
        self.ip = 0 # Instruction pointer
        self.rel_base = 0 # Relative base
        self.inputs = () # inputs is assumed to be a generator

        self.ops = {
                1: self.add,
                2: self.mul,
                3: self.input,
                4: self.output,
                5: self.jump_if_true,
                6: self.jump_if_false,
                7: self.less_than,
                8: self.equals,
                9: self.adj_rel_base,
            }
        
    def param(self, n, want_pos=False):
        digits = self.memory[self.ip] // 100 
        mode = digits // (10 ** n) % 10
        param_pos = self.ip + n + 1
        self.extend(param_pos)

        if mode == 0: # Positional mode
            pos = self.memory[param_pos]
        elif mode == 1: # Absolute mode
            pos = param_pos
        elif mode == 2: # Relative mode
            pos = self.rel_base+self.memory[param_pos]
        else:
            raise(Exception("unexpected param mode {} at ip {}".format(mode, self.ip)))

        self.extend(pos)
        return pos if want_pos else self.memory[pos]
    
    def extend(self, pos):
        if pos >= len(self.memory):
            self.memory.extend([0] * (pos-len(self.memory)+1))

    def add(self):
        self.memory[self.param(2, True)] = self.param(0) + self.param(1)
        self.ip += 4

    def mul(self):
        self.memory[self.param(2, True)] = self.param(0) * self.param(1)
        self.ip += 4

    def input(self):
        self.memory[self.param(0, True)] = next(self.inputs)
        self.ip += 2

    def output(self):
        p = self.param(0)
        self.ip += 2
        return p

    def jump_if_true(self):
        if self.param(0):
            self.ip = self.param(1)
        else:
            self.ip += 3

    def jump_if_false(self):
        if not self.param(0):
            self.ip = self.param(1)
        else:
            self.ip += 3

    def less_than(self):
        self.memory[self.param(2, True)] = int(self.param(0) < self.param(1))
        self.ip += 4

    def equals(self):
        self.memory[self.param(2, True)] = int(self.param(0) == self.param(1))
        self.ip += 4

    def adj_rel_base(self):
        self.rel_base += self.param(0)
        self.ip += 2

    def run(self, inputs):
        self.inputs = inputs
        while True:
            self.extend(self.ip)
            op_code = self.memory[self.ip] % 100
            if op_code == 99:
                # ...and, we're done.
                return

            if op_code not in self.ops:
                raise(Exception("unexpected opcode {} at ip {}".format(op_code, self.ip)))
            
            out = self.ops[op_code]()
            if out is not None:
                yield out

class PaintingRobot(object):
    def __init__(self, memory):
        self.memory = memory

        self.dir = 0
        self.x, self.y = 0, 0
        self.panels = {}

        self.dir_delta = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    def repeat_color(self):
        while True:
            yield self.panels.get(self.pos(), 0)

    def pos(self):
        return (self.x, self.y)

    def move(self):
        dx, dy = self.dir_delta[self.dir]
        self.x += dx
        self.y += dy

    def run(self):
        ic = IntCode(self.memory)
        output = ic.run(self.repeat_color())
        while True:
            try:
                self.panels[self.pos()] = next(output) # Get color
                self.dir += 1 if next(output) else -1 # Get direction
                self.dir %= 4
                self.move()

            except StopIteration:
                return len(self.panels)

def main():
    array = list(map(int, f_input()[0].split(",")))

    program = PaintingRobot(array)
    print(program.run())

if __name__ == "__main__":
    main()
