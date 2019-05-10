
# Gets the number of ways a certain number of steps
# can be climbed, given a set of possible 'moves' (i.e.
# a set containing the number of steps that be climbed
# in a single iteration)
def getNumWaysToClimb(numSteps, possibleSteps = {1, 2}):
    count = 0

    if numSteps < 0:
        count = 0
    elif numSteps == 0:
        count = 1
    else:
        for possibleStep in possibleSteps:
            count = count + getNumWaysToClimb(numSteps - possibleStep, possibleSteps)
    
    return count

def test_numWaysToClimb():
    assert(getNumWaysToClimb(1) == 1)
    assert(getNumWaysToClimb(2) == 2)
    assert(getNumWaysToClimb(3) == 3)
    assert(getNumWaysToClimb(4) == 5)

    assert(getNumWaysToClimb(1, {1, 3, 5}) == 1)
    assert(getNumWaysToClimb(2, {1, 3, 5}) == 1)
    assert(getNumWaysToClimb(3, {1, 3, 5}) == 2)
    assert(getNumWaysToClimb(4, {1, 3, 5}) == 3)

