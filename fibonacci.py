'''
	Return fibonacci No. for given no. M
'''

'''
	To run: python denominations.py 6
	Output: 8
'''

import sys

m = int(sys.argv[1])
def fib(n):
    if n == 0 or n == 1:
        return n

    return fib(n-1) + fib(n-2)

print fib(m)
