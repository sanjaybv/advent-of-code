start, end = 367479, 893698

def is_inc(num):
    num = str(num)
    return all(x <= y for x, y in zip(num[:-1], num[1:]))

def has_same_adj(num):
    num = str(num)
    return any(x == y for x, y in zip(num[:-1], num[1:]))

def has_only_adj(num):
    num = str(num)
    state = 0
    for x, y in zip(num[:-1], num[1:]):
        if x == y:
            state += 1
        else:
            if state == 1:
                return True
            state = 0

    return state == 1

print(sum(is_inc(x) and has_same_adj(x) for x in range(start, end+1)))
print(sum(is_inc(x) and has_only_adj(x) for x in range(start, end+1)))
