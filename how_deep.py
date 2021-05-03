# https://py.checkio.org/en/mission/how-deep/

# You are given a tuple that consists of integers and other tuples, which in turn can also contain tuples.
# Your task is to find out how deep this structure is or how deep the nesting of these tuples is.

# Input: Tuple of tuple of tuple...
# Output: Int.

# Example: 
# how_deep((1, 2, 3)) == 1
# how_deep((1, 2, (3,))) == 2


# how_deep = lambda structure: 1 + max((how_deep(s) for s in structure if type(s) is not int), default=0)

def how_deep(t: tuple) -> int:
    depth = 1
    for i in t:
        tmp_depth = 1
        if isinstance(i, tuple):
            tmp_depth += how_deep(i)
        if depth < tmp_depth:
            depth = tmp_depth
    return depth


# Test
print(how_deep((1,(2,),(3,))))