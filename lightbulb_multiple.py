# https://py.checkio.org/en/mission/multiple-lightbulbs/

# Input: Three arguments and only the first one is required. 
#        The first one is a list of datetime objects (instead of datetime object there can be a tuple of two datetime and int),
#        the second and the third ones are the datetime objects.
# Output: A number of seconds as an integer.

from datetime import datetime
from typing import List, Optional, Union, Tuple

def sum_light(els: List[Union[datetime, Tuple[datetime, int]]],
            start_watching: Optional[datetime] = None,
            end_watching: Optional[datetime] = None) -> int:
    if len(els) % 2 != 0:
        els.append(end_watching)
    els = [(el, 1) if isinstance(el, datetime) else el for el in els]
    state = {}
    duration = 0
    for i in range(0, len(els)-1):
        n1 = els[i][1]
        t1 = els[i][0] if start_watching is None or els[i][0] > start_watching else start_watching
        n2 = els[i+1][1]
        t2 = els[i+1][0] if end_watching is None or els[i+1][0] < end_watching else end_watching
        state[n1] = not state.get(n1,False)
        if any(state.values()):
            duration += max((t2-t1).total_seconds(), 0)
    return int(duration)

# Test

print(sum_light(
    [
datetime(2015, 1, 12, 10, 0, 0),
datetime(2015, 1, 12, 10, 10, 10),
datetime(2015, 1, 12, 11, 0, 0),
datetime(2015, 1, 12, 11, 10, 10)
]
))
