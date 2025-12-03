import time

def turn(op, val):
    sign = 1 if op[0] == 'R' else -1
    return (val + sign * int(op[1:])) % 100

def turn_batch(ops, init):
    val = init
    res = 0
    for op in ops:
        val = turn(op, val)
        if val == 0:
            res += 1
    return res

if __name__ == "__main__":
    with open("in/1.txt") as f:
        lines = f.read().splitlines()
    
    ts = time.time()
    res = turn_batch(lines, 50)
    te = time.time()
    print(f"Result: {res} in {te - ts:.6f} seconds")