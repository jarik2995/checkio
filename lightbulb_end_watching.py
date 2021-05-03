# https://py.checkio.org/en/mission/lightbulb-end-watching/

# Input: Three arguments and only the first one is required. The first one is a list of datetime objects, the second and the third ones are the datetime objects.
# Output: A number of seconds as an integer.

from datetime import datetime
from typing import List, Optional

def sum_light(els: List[datetime], start_watching: Optional[datetime] = None, end_watching: Optional[datetime] = None):
    if len(els) % 2 != 0:
        els.append(end_watching)
    duration = 0
    for i in range(0, len(els), 2):
        start = els[i] if start_watching is None or els[i] > start_watching else start_watching
        stop = els[i+1] if end_watching is None or els[i+1] < end_watching else end_watching
        duration += max((stop - start).total_seconds(),0)

    return int(duration) 


# Test
print(sum_light(
    [
datetime(2015, 1, 12, 10, 0, 0),
datetime(2015, 1, 12, 10, 10, 10),
datetime(2015, 1, 12, 11, 0, 0),
datetime(2015, 1, 12, 11, 10, 10)
],
datetime(2015, 1, 12, 11, 0, 0)
)) 