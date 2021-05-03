# https://py.checkio.org/en/mission/frequency-sorting/

# Your mission is to sort the list by the frequency of numbers included in it.
# If a few numbers have an equal frequency - they should be sorted according to their natural order.

# Input: Chaotic list of numbers.
# Output: The list of numbers in which they are sorted by their frequency.

# Example
# frequency_sorting([5, 3, 8, 11, 5, 6, 6, 5]) == [5, 5, 5, 6, 6, 3, 8, 11]

# Pythonic way
def frequency_sorting(els: list) -> list:
    return sorted(sorted(els), key=lambda x: -els.count(x))

# Custom
from collections import defaultdict
def frequency_sorting_custom(els: list) -> list:
    count = defaultdict(lambda: 1)
    els_m = [] # sorted list for multiple el
    els_s = [] # sorted lsit for single el

    # sort list
    for i in range(0, len(els)):
        for j in range(0,len(els)-i-1):
            if els[j] > els[j+1]:
                els[j], els[j+1] = els[j+1], els[j]
    
    # count multiple el
    for i in range(0, len(els)-1):
        if els[i] == els[i+1]:
            count[els[i]] += 1
    # split list in single & multi el 
    for el, c in count.items():
        els_m.append([el]*c)
    for i in range(0, len(els)):
        if not count.get(els[i]):
            els_s.append(els[i])

    # sort multi el list by freq
    for i in range(0, len(els_m)):
        for j in range(0, len(els_m)-i-1):
            print(els_m[j])
            if len(els_m[j]) < len(els_m[j+1]):
                els_m[j], els_m[j+1] = els_m[j+1], els_m[j]
    els_m = [ el for sub_els in els_m for el in sub_els ]
    
    return els_m + els_s

# Test
#print(frequency_sorting([5, 3, 8, 11, 5, 6, 6, 5]))
#print(frequency_sorting_custom([5, 3, 8, 11, 5, 6, 6, 5]))
print(frequency_sorting_custom([3,4,11,13,11,4,4,7,3])
)