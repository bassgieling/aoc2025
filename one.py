import time

def turn_naive(op, val):
    sign = 1 if op[0] == 'R' else -1
    return (val + sign * int(op[1:])) % 100

def turn_batch_exact(ops, init):
    val = init
    res = 0
    for op in ops:
        val = turn_naive(op, val)
        if val == 0:
            res += 1
    return res

def turn(op, val, res):
    sign = 1 if op[0] == 'R' else -1
    amount = int(op[1:])
    dist = (100 - sign * val) % 100 # distance to 0 in the given direction
    res += 1 if amount >= dist and dist != 0 else 0 # passed 0 once
    res += abs(amount - dist) // 100 # add how many full cycles we do after passing 0
    val = (val + sign * amount) % 100 # final value
    return val, res

def turn_batch(ops, init):
    val = init
    res = 0
    for op in ops:
        val, res = turn(op, val, res)
    return val, res

if __name__ == "__main__":
    with open("in/1.txt") as f:
        lines = f.read().splitlines()
    
    # PART 1
    ts = time.time()
    res = turn_batch_exact(lines, 50)
    te = time.time()
    print(f"Result: {res} in {te - ts:.6f} seconds")

    # PART 2
    ts = time.time()
    num, zeroes = turn_batch(lines, 50)
    te = time.time()
    print(f"Final number: {num}\n" + \
          f"Times passed 0: {zeroes}\n" + \
          f"Computed in {te - ts:.6f} seconds")
    