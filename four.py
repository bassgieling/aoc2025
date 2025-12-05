import numpy as np

def find_removable_paper(input_grid, filter_size):
    total = 0
    n = np.shape(input_grid)[0] - 2
    m = np.shape(input_grid)[1] - 2
    filter = np.ones((filter_size, filter_size))
    removable = np.zeros_like(input_grid)
    for i in range(n):
        for j in range(m):
            if input_grid[i+1, j+1] == 1. \
                and np.tensordot(filter, input_grid[i:i+filter_size, j:j+filter_size]) < 5:
                    total += 1
                    removable[i+1, j+1] = 1.
    return total, removable

if __name__ == "__main__":
    with open("in/4.txt") as f:
        lines = f.read().splitlines()
    
    n = len(lines)
    m = len(lines[0])
    shape = (n + 2, m + 2)
    grid = np.zeros(shape)
    for i, line in enumerate(lines):
        for j, spot in enumerate(line):
            if spot == '@':
                grid[i+1, j+1] = 1.
        
    tot, removed = find_removable_paper(grid, 3)

    print("PART 1: ", tot)

    tot_tot = tot
    while tot > 0:
        grid = grid - removed
        tot, removed = find_removable_paper(grid, 3)
        tot_tot += tot

    print("PART 2: ", tot_tot)