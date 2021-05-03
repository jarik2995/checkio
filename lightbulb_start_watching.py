# https://py.checkio.org/en/mission/lightbulb-start-watching/

# Input: Two arguments and only the first one is required. The first one is a list of datetime objects and the second one is a datetime object.
# Output: A number of seconds as an integer.

### example
# sum_light([
#     datetime(2015, 1, 12, 10, 0, 0),
#     datetime(2015, 1, 12, 10, 0, 10),
# ],
# datetime(2015, 1, 12, 10, 0, 5)) == 5

# sum_light([
#     datetime(2015, 1, 12, 10, 0, 0),
#     datetime(2015, 1, 12, 10, 0, 10),
# ], datetime(2015, 1, 12, 10, 0, 0)) == 10

# sum_light([
#     datetime(2015, 1, 12, 10, 0, 0),
#     datetime(2015, 1, 12, 10, 10, 10),
#     datetime(2015, 1, 12, 11, 0, 0),
#     datetime(2015, 1, 12, 11, 10, 10),
# ], datetime(2015, 1, 12, 11, 0, 0)) == 610

from datetime import datetime
from typing import List, Optional

def sum_light(els: List[datetime], start_watching: Optional[datetime] = None) -> int:
    duration = 0
    for i in range(0, len(els), 2):
        start = els[i] if start_watching is None or start_watching < els[i] else start_watching
        stop = els[i+1]
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