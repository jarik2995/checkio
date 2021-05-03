# https://py.checkio.org/en/mission/reverse-every-ascending/

# Create and return a new iterable that contains the same elements as the argument iterable items,
# but with the reversed order of the elements inside every maximal strictly ascending sublist.
# This function should not modify the contents of the original iterable.

# Input: Iterable
# Output: Iterable

# Example:
# reverse_ascending([1, 2, 3, 4, 5]) == [5, 4, 3, 2, 1]
# reverse_ascending([5, 7, 10, 4, 2, 7, 8, 1, 3]) == [10, 7, 5, 4, 8, 7, 2, 3, 1]

def reverse_ascending(els: list) -> list:
    result = []
    tmp = []
    if len(els) <= 1:
        return els
    for i in range(0, len(els)-1):
        tmp.append(els[i])
        if els[i] >= els[i+1]:
            result.append(tmp[::-1])
            tmp = []
    tmp.append(els[-1])
    result.append(tmp[::-1])
    return [ el for sub in result for el in sub ]

# Test
print(reverse_ascending([]))