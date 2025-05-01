# 9.1.1_fibonacci.py
# This is the function should take a number 
# Return a list containing a Fibonacci sequence of number entered
# Aurthor: Akshay Pastagiya

import logging
#logging.basicConfig(lavel = logging.DEBUG)
number = 11
def fibonacci(number):
    a = 0
    b = 1
    fibonacciSequence = [0]
    # we have one in the list already so number - 1 times
    # this is not the most efficient code
    # could have used yield
    for i in range(1,number):
        fibonacciSequence.append(b)
        # this is funky code make a = b and b = a + b
        a , b = b, a + b
    logging.debug("%d: %s",number, fibonacciSequence)
    if number == 0:
        return []
    if number < 0:
        raise ValueError('number must be > 0')
    return [fibonacciSequence]

if __name__ == '__main__':
    # write down the test cases for testing
    print("all good")
    try:
        fibonacci(-1)
    except ValueError:
        # we want this exception to be thrown
        # so this is an example where we want to do nothing
        pass
    else:
        # if the exception was not thrown we should throw
        # Assertion error
        assert False, 'fibonacci missing ValueError'
        # or
        #raise AssertionError("fibonacci no valueError ")
    return7 = [0,1,1,2,3,5,8]
    return11 = [0,1,1,2,3,5,8,13,21,34,55]
    assert fibonacci(7) == return7, 'incorrect return for 7'
    assert fibonacci(11) == return11, 'incorrect return for 11'
    assert fibonacci(0) == [], 'incorrect return value for 0'
    assert fibonacci(1) == [0], 'incorrect return value for 1'