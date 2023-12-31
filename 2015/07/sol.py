import fileinput as fi
import re

pattern = r"(?:(\d+)|(\w*) ?(NOT|AND|OR|LSHIFT|RSHIFT) (\w*)) -> (\w+)"
uint16mask = (1 << 16) - 1


class Circuit(object):
    def __init__(self) -> None:
        self.table = {}

    def add(self, out: str, e: Expr) -> None:
        self.table[out] = e

    def resolve(self, arg: str) -> int:
        try:
            v = int(arg)
        except ValueError:
            return self.table[arg].eval(self.table) & uint16mask
        else:
            return v & uint16mask


class Expr(object):
    def __init__(self, str_expr: str) -> None:
        m = re.match(pattern, str_expr)
        if not m:
            raise

        self.op = m.group(2)
        self.arg_a = m.group(1)
        self.arg_b = m.group(3)
        self.out = m.group(4)

        if self.op == "":
            self.op = "IDENTITY"

    def eval(self, c: Circuit):
        match self.op:
            case "IDENTITY":
                return c.resolve(self.arg_b)
            case "NOT":
                return ~c.resolve(self.arg_b)
            case "AND":
                return c.resolve(self.arg_a) & c.resolve(self.arg_b)
            case "OR":
                return c.resolve(self.arg_a) | c.resolve(self.arg_b)
            case "LSHIFT":
                return c.resolve(self.arg_a) << c.resolve(self.arg_b)
            case "RSHIFT":
                return c.resolve(self.arg_a) >> c.resolve(self.arg_b)

        raise


c = Circuit()
for line in fi.input():
    e = Expr(line.strip())
    c.add(e.out, e)

print(c.resolve("a"))
