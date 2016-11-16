'''
	This is a common coin change problem.
	For given infinite supply of coins for given denominations like [1,5,10].
	Find no. of ways to make change for given no. N
'''

'''
	To run: python denominations.py 9
	Output: 2
'''
import sys

N = int(sys.argv[1])

ar = [1, 5, 10, 25]

def count(x, i):
    if x < 0:
        return 0

    if x == 0:
        return 1
    
    if i == len(ar):
        return 0

    return count(x - ar[i], i) + count(x, i+1)

print count(N, 0)
