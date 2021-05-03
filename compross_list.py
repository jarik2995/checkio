# https://py.checkio.org/en/mission/compress-list/

# A given list should be "compressed" in a way so, instead of two (or more) equal elements, staying one after another,
# there is only one in the result Iterable (list, tuple, iterator ...).

# Input: List
# Output: "COMPRESSED" Iterable

# Example
# compress([
#   5, 5, 5,
#   4, 5, 6,
#   6, 5, 5,
#   7, 8, 0,
#   0]) == [5, 4, 5, 6, 5, 7, 8, 0]
# compress([1, 1, 1, 1, 2, 2, 2, 1, 1, 1]) == [1, 2, 1]

# Solution 1
def compress(els: list) -> list:
    i = 0
    while i < len(els)-1:
        if els[i] == els[i+1]:
            del els[i]
            i-=1
        i+=1
    return els

# Test
print(compress_v2([1, 1, 1, 1, 2, 2, 2, 1, 1, 1]))