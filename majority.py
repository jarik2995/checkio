# https://py.checkio.org/en/mission/majority/

# Input: A List of booleans.
# Output: A Boolean.

# is_majority([True, True, False, True, False]) == True
# is_majority([True, True, False]) == True

def is_majority(els: list) -> bool:
    return els.count(True) > els.count(False)

print(is_majority([True, False, True]))