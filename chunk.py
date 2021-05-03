# https://py.checkio.org/en/mission/chunk/

# Split a list into smaller lists of the same size (chunks).
# The last chunk can be smaller than the default chunk-size.
# If the list is empty, then you shouldn't have any chunks at all.

# Input: Two arguments. A List and chunk size.
# Output: An Iterable with chunked Iterable.

# Example
# chunking_by([5, 4, 7, 3, 4, 5, 4], 3) == [[5, 4, 7], [3, 4, 5], [4]]
# chunking_by([3, 4, 5], 1) == [[3], [4], [5]]


def chunking_by(els: list, size: int) -> list:
    return [els[i:i+size] for i in range(0,len(els),size)]

# Test
print(chunking_by([], 1))