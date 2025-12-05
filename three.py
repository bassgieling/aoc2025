import numpy as np

if __name__ == "__main__":
    with open("in/3.txt") as f:
        lines = f.read().splitlines()
    print(lines)
    
    tot = 0
    for line in lines:
        n = len(line)
        print(f"assessing line {line} of length {n}")
        nums = [int(k) for k in line]
        idx_max_left = np.argmax(nums[:-1])
        idx_max_right = np.argmax(nums[idx_max_left+1:])
        largest_number = line[idx_max_left] + line[idx_max_left + 1 + idx_max_right]
        print(f"largest number found is {largest_number}")
        tot += int(largest_number)

    print("PART 1: ", tot)

    
    def get_max_ids(nums, k, rel_idx):
        # take largest number starting from left
        # look right of that rightmost number and recurse on that part of array
        # if not enough numbers found, recurse on the left
        if k > 0 and len(nums) > 0:
            id = np.argmax(nums)
            ids = [rel_idx + id] + get_max_ids(nums[id+1:], k-1, rel_idx+id+1)
            if len(ids) < k:
                ids = get_max_ids(nums[:id], k - len(ids), rel_idx) + ids
            return ids
        else:
            return []

    tot = 0
    for line in lines:
        n = len(line)
        print(f"assessing line {line} of length {n}")
        nums = [int(k) for k in line]
        ids = get_max_ids(nums, 12, 0)

        largest_number = ''
        for id in np.sort(ids):
            largest_number += line[id]
        print(f"largest number found is {largest_number}")
        tot += int(largest_number)
    
    print("PART 2: ", tot)

