import fileinput

numbers = [int(line.strip()) for line in fileinput.input()]

for n1 in numbers:
    for n2 in numbers:
        if n1 + n2 == 2020:
            print(n1 * n2)

for n1 in numbers:
    for n2 in numbers:
        for n3 in numbers:
            if n1 + n2 + n3 == 2020:
                print(n1 * n2 * n3)
