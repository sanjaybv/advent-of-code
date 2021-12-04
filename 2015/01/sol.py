import fileinput

lines = [line.strip() for line in fileinput.input()]

count = 0

for line in lines:
    for i, char in enumerate(line):
        if char == '(':
            count += 1
        else:
            count -= 1
            if count == -1:
                print("basement @", i)

print(count)
