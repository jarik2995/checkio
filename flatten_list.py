# https://py.checkio.org/en/mission/flatten-list/

# There is a list which contains integers or other nested lists which may contain yet more lists and integers which then…
# you get the idea. You should put all of the integer values into one flat list.
# The order should be as it was in the original list with string representation from left to right.

# Input data: A nested list with integers.
# Output data: The one-dimensional list with integers.

# Example:
# flat_list([1, 2, 3]) == [1, 2, 3]
# flat_list([1, [2, 2, 2], 4]) == [1, 2, 2, 2, 4]
# flat_list([[[2]], [4, [5, 6, [6], 6, 6, 6], 7]]) == [2, 4, 5, 6, 6, 6, 6, 6, 7]
# flat_list([-1, [1, [-2], 1], -1]) == [-1, 1, -2, 1, -1]

# Solution 1
def flat_list(els: list) -> list:
    flatten = []
    for el in els:
        if isinstance(el, list):
            flatten += flat_list(el)
        else:
            flatten.append(el)
    return flatten

# Solution 2, crazy
def flat_list_crazy(array):
    return [int(i) for i in str(array).replace('[', '').replace(']', '').replace(',', '').split()]

# Test
print(flat_list([[[2]], [4, [5, 6, [6], 6, 6, 6], 7]]))