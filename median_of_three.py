# https://py.checkio.org/en/mission/median-of-three/

# Given an iterable of ints , create and return a new iterable whose first two elements are the same as in items,
# after which each element equals the median of the three elements in the original list ending in that position.

# Input: Iterable of ints.
# Output: Iterable of ints.

# Example:
# list(median_three([1, 2, 3, 4, 5, 6, 7])) == [1, 2, 2, 3, 4, 5, 6]
# list(median_three([1])) == [1]
# list(median_three([-1, 0, 1])) == [-1, 0, 0]

def median_three(els: list) -> list:
    medians = els[:2]
    for i in range(2, len(els)):
        median = sorted(els[i-2:i+1])[1]
        medians.append(median)
    return medians

# Test
print(median_three([5,2,9,1,7,4,6,3,8]))