import numpy as np

if __name__ == "__main__":
    with open("in/2.txt") as f:
        lines = [x.strip() for x in f.read().strip().split(',')]
    
    import math

    res = 0
    for line in lines:
        start, end = [s.strip() for s in line.split('-')]
        start_i = int(start)
        end_i = int(end)
        for n in range(start_i, end_i + 1):
            k = len(str(n)) // 2
            first_k = n // 10**k
            last_k = n % 10**k
            if first_k == last_k:
                res += n
    print(f"PART 1: {res}")

    def divisors(k):
        d = []
        for m in range(1, k):
            if k % m == 0:
                d.append(m)
        return d

    tot = 0
    for line in lines:
        start, end = line.split('-')
        for n in range(int(start), int(end) + 1):
            str_n = str(n)
            m = len(str_n)
            for k in divisors(m):
                if str_n == (m//k)*str_n[:k]:
                    tot += n
                    break
        
    print(f"PART 2: {tot}")

    