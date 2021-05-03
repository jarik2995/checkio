# https://py.checkio.org/en/mission/replace-last/

# Input: List.
# Output: Iterable.

# replace_last([2, 3, 4, 1]) == [1, 2, 3, 4]
# replace_last([1, 2, 3, 4]) == [4, 1, 2, 3]
# replace_last([1]) == [1]
# replace_last([]) == []

def replace_last(els: list) -> list:
    return els[-1:] + els[:-1]

# Test
print(replace_last([]))