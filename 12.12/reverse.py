import sys
from sys import argv
from IPython import embed

MAX_VALUE = sys.maxsize
MIN_VALUE = -sys.maxsize - 1

(x) = argv

def reverse(x):
    rev = 0
    while x != 0:
        pop = x % 10
        x = x / 10
        
        if (rev > MAX_VALUE) / 10 or (rev == MAX_VALUE / 10 and pop > 7):
            return 0
        if (rev < MIN_VALUE) / 10 or (rev == MIN_VALUE / 10 and pop < -8):
            return 0
        rev = rev * 10 + pop
        print('value of rev',rev)
        
    return rev
