# https://py.checkio.org/en/mission/remove-all-after/

# Input: List and the border element.
# Output: Iterable (tuple, list, iterator ...).

# Example
# remove_all_after([1, 2, 3, 4, 5], 3) == [1, 2, 3]
# remove_all_after([1, 1, 2, 2, 3, 3], 2) == [1, 1, 2]

# Solution 1
def remove_all_after(els: list, el: int) -> list:
    for i in range(0, len(els)):
        if els[i] == el:
            els = els[:i+1]
            break
    return els

# Solution 2
def remove_all_after_v2(els: list, el: int) -> list:
    return els[:els.index(el)+1] if el in els else els

print(remove_all_after_v2([1, 2, 3, 4, 5], 3))