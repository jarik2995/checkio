# https://py.checkio.org/en/mission/lightbulb-intro/

# Input: A list of datetime objects
# Output: A number of seconds as an integer.

### example
# sum_light([
#     datetime(2015, 1, 12, 10, 0 , 0),
#     datetime(2015, 1, 12, 10, 10 , 10),
# ]) == 610

# sum_light([
#     datetime(2015, 1, 12, 10, 0 , 0),
#     datetime(2015, 1, 12, 10, 10 , 10),
#     datetime(2015, 1, 12, 11, 0 , 0),
#     datetime(2015, 1, 12, 11, 10 , 10),
# ]) == 1220

# sum_light([
#     datetime(2015, 1, 12, 10, 0 , 0),
#     datetime(2015, 1, 12, 10, 0 , 1),
# ]) == 1

from datetime import datetime
from typing import List

def sum_light(els: List[datetime]) -> int:
    duration = 0
    for i in range(0, len(els), 2):
        duration += (els[i+1] - els[i]).total_seconds()
    return int(duration)
        


# Test
print(
    sum_light([
datetime(2015, 1, 12, 10, 0, 0),
datetime(2015, 1, 12, 10, 10, 10),
datetime(2015, 1, 12, 11, 0, 0),
datetime(2015, 1, 12, 11, 10, 10)
])
)