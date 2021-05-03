# https://py.checkio.org/en/mission/sort-except-zero/

# Sort the numbers in an array. But the position of zeros should not be changed.

# Input: A List.
# Output: An Iterable (tuple, list, iterator ...).

# Example
# except_zero([5, 3, 0, 0, 4, 1, 4, 0, 7]) == [1, 3, 0, 0, 4, 4, 5, 0, 7]
# except_zero([0, 2, 3, 1, 0, 4, 5]) == [0, 1, 2, 3, 0, 4, 5]

def except_zero(els: list) -> list:
    # remember index of 0
    zeros = [i for i in range(0,len(els)) if els[i]==0]


    # buble sort
    for i in range(0, len(els)):
        for j in range(0, len(els)-i-1):
            if els[j] > els[j+1]:
                els[j], els[j+1] = els[j+1], els[j]
    # or els.sort() can be used

    # reordering 0
    for i in range(0,len(zeros)):
        els.insert(zeros[i]-i+len(zeros),0)
        els.pop(0)
    return els

# Test
print(except_zero([5, 3, 0, 0, 4, 1, 4, 0, 7]))