# https://py.checkio.org/en/mission/lightbulb-more/

# Input: Five arguments and only the first one is required. 
#        The first one (els) is a list of datetime objects (instead of datetime object there can be a tuple of two datetime and int),
#        the second (start_watching) and the third ones (end_watching) are the datetime objects. The forth argument (operating) - 
#        timedelta object - how long the lamp can work. The 5th argument is a positive non-zero int.
# Output: A number of seconds as an integer.
#### Example
# sum_light([
#     (datetime(2015, 1, 12, 10, 0, 10), 3),
#     datetime(2015, 1, 12, 10, 0, 20),
#     (datetime(2015, 1, 12, 10, 0, 30), 3),
#     (datetime(2015, 1, 12, 10, 0, 30), 2),
#     datetime(2015, 1, 12, 10, 0, 40),
#     (datetime(2015, 1, 12, 10, 0, 50), 2),
# ], req=2) == 20

# sum_light([
#     (datetime(2015, 1, 12, 10, 0, 10), 3),
#     datetime(2015, 1, 12, 10, 0, 20),
#     (datetime(2015, 1, 12, 10, 0, 30), 3),
#     (datetime(2015, 1, 12, 10, 0, 30), 2),
#     datetime(2015, 1, 12, 10, 0, 40),
#     (datetime(2015, 1, 12, 10, 0, 50), 2),
# ], req=3) == 0

# sum_light([
#     (datetime(2015, 1, 12, 10, 0, 10), 3),
#     datetime(2015, 1, 12, 10, 0, 20),
#     (datetime(2015, 1, 12, 10, 0, 50), 3),
#     (datetime(2015, 1, 12, 10, 0, 30), 2),
#     datetime(2015, 1, 12, 10, 0, 40),
#     (datetime(2015, 1, 12, 10, 0, 50), 2),
# ], req=3) == 10


def lightbulb(els, start_watching=None, end_watching=None, operating=None, req=1):
    elsT = []    
    switchStates = {}
    switchLastTime = {}
    switchSkip = {}

    # transform array to elsT
    for el in els:

        # convert all to tuples
        if isinstance(el, datetime):
            switchNumber = 1
            switchTime = el
        
        else:
            switchNumber = el[1]
            switchTime = el[0]
        
        # cut datetime based on operating time
        if operating is not None:
            if not switchStates.get(switchNumber, False):
                switchStates[switchNumber] = True
                switchLastTime[switchNumber] = switchTime
            
            elif switchStates.get(switchNumber) and not switchSkip.get(switchNumber, False):
                deltaSwitchTime = switchTime - switchLastTime[switchNumber]
                if deltaSwitchTime >= operating:
                    switchTime = switchLastTime[switchNumber] + operating
                    switchSkip[switchNumber] = True
            else:
                continue

        elsT.append((switchTime, switchNumber))  

    illPrev = False
    illStartTime = None
    illDurationTotal = 0
    switchStates = {}
    for el in sorted(elsT, key=lambda x: x[0]):
        switchNumber = el[1]
        switchTime = el[0]
        
        # switch ON/OFF or create if not exist
        switchStates[switchNumber] = not switchStates.get(switchNumber, False)
        
        # calculate time room is illuminated
        illNow = sum(switchStates.values()) >= req
        if illNow and not illPrev:
            illStartTime = switchTime if start_watching is None else max(switchTime, start_watching)
        
        elif illPrev and not illNow and (start_watching is None or switchTime > start_watching):
            illEndTime = switchTime if end_watching is None else min(switchTime, end_watching)
            illDurationTotal += max(int((illEndTime - illStartTime).total_seconds()),0)
            
        illPrev = illNow

    # use case when switch not turned off
    if illNow:
        illDurationTotal += max(int(((illStartTime.max - illStartTime) if end_watching is None else (end_watching - illStartTime)).total_seconds()),0)
    
    return illDurationTotal


# Test
from datetime import datetime, timedelta

print(lightbulb(els=[
[datetime(2015, 1, 12, 10, 0, 10), 3],
datetime(2015, 1, 12, 10, 0, 20),
[datetime(2015, 1, 12, 10, 0, 30), 3],
[datetime(2015, 1, 12, 10, 0, 30), 2],
datetime(2015, 1, 12, 10, 0, 40),
[datetime(2015, 1, 12, 10, 0, 50), 2],
[datetime(2015, 1, 12, 10, 1, 20), 2],
[datetime(2015, 1, 12, 10, 1, 40), 2]
],
start_watching=datetime(2015, 1, 12, 10, 0, 20),
operating=timedelta(seconds=100)))