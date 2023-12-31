import fileinput as fi


def check(s):
    if sum([1 for ch in s if ch in "aeiou"]) < 3:
        return 0
    if sum([1 for a, b in zip(s[:-1], s[1:]) if a == b]) < 1:
        return 0
    if sum([1 for bad in ["ab", "cd", "pq", "xy"] if bad in s]) > 0:
        return 0
    return 1


def check_again(s):
    if (
        sum(
            [
                1
                for i in range(len(s) - 1)
                if s[i : i + 2] in s[:i] or s[i : i + 2] in s[i + 2 :]
            ]
        )
        < 1
    ):
        return 0
    if sum([1 for i in range(len(s) - 2) if s[i] == s[i + 2]]) < 1:
        return 0

    return 1


inp = [li.strip() for li in fi.input()]

c = sum([check(i) for i in inp])
print(c)

ca = sum([check_again(i) for i in inp])
print(ca)
