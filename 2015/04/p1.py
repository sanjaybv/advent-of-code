import fileinput
import hashlib

if __name__ == "__main__":
    lines = [line.strip() for line in fileinput.input()]
    cur_hash = ""
    cur_num = -1
    while not cur_hash.startswith("000000"):
        cur_num += 1
        cur_hash = hashlib.md5(bytearray(lines[0]+str(cur_num),
            "utf-8")).hexdigest()
    print(cur_num)

