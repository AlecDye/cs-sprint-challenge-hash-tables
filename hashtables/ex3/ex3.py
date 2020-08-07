"""
use hashtable

Goal: Find the intersections (if any) of all input arrays

input: list of arrays
[
    [1, 2, 3, 4, 5],
    [12, 7, 2, 9, 1],
    [99, 2, 7, 1,]
]

output:
[1, 2]
output can be in any order
"""
# hash table
# cache goes inside func scope or else test data stacks


def intersection(arrays):
    cache = {}
    # loop through arrays?
    for i in arrays:
        # check if number is in cache
        # yes? -> increment by 1
        if i in cache:
            cache[i] += 1
        # no? (not in cache) -> initialize to 1
        else:
            cache[i] = 1
    # return nums from cache? not entire cache?
    return


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
