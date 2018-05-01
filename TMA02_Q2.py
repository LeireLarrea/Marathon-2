"""The Marathon ADT.

For TMA02 Question 2 of M269 17J.
"""


class Marathon:

    # Creator
    # -------
    
    def __init__(self):
        """Set up this marathon without any runners."""
        global marathon
        marathon = []
        
        global finishersTimes
        finishersTimes = []
        
        global startTime
        startTime = 0
        
        global finishersList
        finishersList = []
        
        global finishers_up_to
        finishers_up_to = 0
        
    # Inspectors
    # ----------
    
    
   
    # These are called anytime.
    
    def registered(self, runner):
        """Return True if runner has registered, otherwise False."""
        if runner in marathon:
            return True
        else:
            return False

    def finishers(self):
        """Return the number of starting who finished the race so far."""
        return len(finishersList)
    
    def finished(self, runner):
        """Return True if runner has finished the race, otherwise False."""
        if runner in finishersList:
            return True
        else:
            return False
        
    # These inspectors are called after the race ends.
    
    def finishers_up_to(self, time):
        """Return how many runners finished in the given time or less.
        
        Assume the unit of time is seconds.
        """
        time = calculateTime(time)
        count = 0
        for each in finishersTimes:
            if each <= time:
                count = count+1
        return count
    
    def place(self, runner):
        """Return in which place the runner finished."""
        return (finishersList.index(runner)) + 1
        
    def name(self, place):
        """Return the name of the runner finishing in the given place."""
        return finishersList[place - 1]
    
    def time(self, place):
        """Return the time of the runner finishing in the given place."""
        return finishersTimes[place - 1]
    
    # Modifiers
    # ---------
    
    # This modifier is called before the race starts.
    def register(self, runner):
        """Register the runner. Return nothing."""
        marathon.append(runner)
        
        
    
    # This modifier is called after the race starts and before it ends.
    def finish(self, runner, time):
        """Record that the runner just finished the race in the given time.
    
        Return nothing. Assume the unit of time is seconds.
        """
        time = time - startTime
        finishersTimes.append(calculateTime(time))
        finishersList.append(runner)

# Tests
# -----
# The following tests are minimal and don't cover several possibilities. 
# You should add more tests to reassure yourself your code is correct.

def test(name, actual, expected):
    """Print a message if the actual and expected values differ."""
    if actual != expected:
        print(name, ': expected', expected, 'but got', actual)
        
def calculateTime(item):
    if item == T1:
        time = 60 * 60
    if item == T3:
        time = 3 * T1
    if item == T3_30:
        time = T3 + 30*60
    if item == T4:
        time = 4 * T1
    return time

T1 = 60 * 60        # 1h
T3 = 3 * T1         # 3h
T3_30 = T3 + 30*60  # 3h 30min
T4 = 4 * T1         # 4h

# The Milton Keynes marathon
mk = Marathon()
mk.register('jane')
mk.register('john')
mk.register('anne')

mk.finish('anne', T3)
mk.finish('jane', T3_30)


test('finishers', mk.finishers(), 2)
test('up to 4h', mk.finishers_up_to(T4), 2)
test('up to 3h', mk.finishers_up_to(T3), 1)
test('gold', mk.name(1), 'anne')
test('silver', mk.name(2), 'jane')
test('winning time', mk.time(1), T3)

print('All tests have run.')
mk.registered('jane')
mk.registered('thomas')