# https://py.checkio.org/en/mission/lightbulb-operating/

# Input: Four arguments and only the first one is required. 
#        The first one (els) is a list of datetime objects (instead of datetime object there can be a tuple of two datetime and int),
#        the second (start_watching) and the third ones (end_watching) is the datetime objects. 
#        The forth argument (operating) - timedelta object - how long the lamp can work.

# Output: A number of seconds as an integer.

# Example
# sum_light([
#     datetime(2015, 1, 12, 10, 0, 0),
#     datetime(2015, 1, 12, 10, 0, 30),
#     (datetime(2015, 1, 12, 10, 0, 30), 2),
#     (datetime(2015, 1, 12, 10, 1, 0), 2),
# ], operating=timedelta(seconds=20)) == 40


from datetime import datetime, timedelta
from typing import List, Optional, Union, Tuple
from collections import defaultdict

# Solution 1
# def transform(els: List[Union[datetime, Tuple[datetime,int]]], operating: datetime):
#     tels = []
#     state = {}
#     last = {}
#     skip = {}
#     for el in els:
#         state[el[1]] = not state.get(el[1],False)
#         if state[el[1]]:
#             tels.append(el)
#             last[el[1]] = el[0]
#         elif skip.get(el[1],False):
#             continue
#         elif el[0] - last[el[1]] <= operating:
#             tels.append(el)
#         else:
#             tels.append((last[el[1]] + operating,el[1]))
#             skip[el[1]] = True
#     return tels

# Solution 2
def transform(els: List[Union[datetime, Tuple[datetime,int]]], operating: datetime, end_watching: Optional[datetime] = None):
    nels = []
    tels = defaultdict(list)
    for el in els:
        if isinstance(el,datetime):
            tels[1].append(el)
        else:
            tels[el[1]].append(el[0])
    for n,oels in tels.items():
        t = operating
        if len(oels) % 2 != 0:
            oels.append(end_watching)
        for i in range(0, len(oels), 2):
            nels.append((oels[i],n))
            print(oels)
            if operating is None:
                nels.append((oels[i+1],n))
            else:
                nels.append((min(oels[i+1],oels[i]+operating),n))
                t-=(oels[i+1] - oels[i])
                if t.total_seconds() <= 0:
                    break
    return sorted(nels, key=lambda x: x[0])
        

def sum_light(els: List[Union[datetime, Tuple[datetime, int]]],
        start_watching: Optional[datetime] = None,
        end_watching: Optional[datetime] = None,
        operating: Optional[timedelta] = None) -> int:
    duration = 0
    els = transform(els, operating, end_watching)
    state = {}
    for i in range(0, len(els)-1):
        n1 = els[i][1]
        n2 = els[i+1][1]
        t1 = els[i][0] if start_watching is None or els[i][0] > start_watching else start_watching
        t2 = els[i+1][0] if end_watching is None or els[i+1][0] < end_watching else end_watching
        state[n1] = not state.get(n1,False)
        if any(state.values()):
            if operating is None:
                delta = (t2 - t1).total_seconds()
            else:
                delta = min(t2-t1,operating).total_seconds()
            duration += max(delta,0)

    return duration

# Test

print(sum_light(els=[
datetime(2015, 1, 12, 10, 0, 0),
datetime(2015, 1, 12, 10, 10, 10),
datetime(2015, 1, 12, 11, 0, 0)
],
start_watching=datetime(2015, 1, 12, 11, 5, 0),
end_watching=datetime(2015, 1, 12, 11, 10, 0)))