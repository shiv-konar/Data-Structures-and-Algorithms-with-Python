def gcdIter(a, b):
    '''
    a, b: positive integers

    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    testValue = min(a, b)

    # Keep looping until testValue divides both a & b evenly
    while (a % testValue == 0 and b % testValue == 0) or testValue == 1:
        testValue -= 1

    return testValue

print gcdIter(35,140)