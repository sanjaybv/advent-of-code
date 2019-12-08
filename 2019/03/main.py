def read_lines():
    lines = [[], []]
    with open('input.txt') as input_file:
        for i, line in enumerate(input_file):
            lines[i] = line.strip().split(",")
    return lines

def get_points(line):
    coords = []
    i = 0
    j = 0
    for ins in line:
        d = ins[0]
        l = int(ins[1:])
        while l > 0:
            if d == 'U':
                j += 1
            if d == 'R':
                i += 1
            if d == 'D':
                j -= 1
            if d == 'L':
                i -= 1
            
            coords.append((i, j))
            l -= 1
    return coords

def key(t):
    return "{}:{}".format(*t)

def main():
    lines = read_lines()

    a_map = {}
    a_points = get_points(lines[0])
    for i, t in enumerate(a_points):
        a_map[key(t)] = i + 1
    
    closest = 0
    first = 0
    b_points = get_points(lines[1])
    for i, t in enumerate(b_points):
        if key(t) in a_map:
            j = a_map[key(t)]
            if not first or i + 1 + j < first:
                first = i + 1 + j
            if not closest or sum(map(abs, t)) < closest:
                closest = sum(map(abs, t))

    print(closest)
    print(first)

if __name__ == "__main__":
    main()
