'''
	This is the solution of hacker rank problem:
	https://www.hackerrank.com/challenges/red-john-is-back
'''
import sys

N = int(sys.argv[1])

def count(n):
    if n<0:
        return 0
    if n == 0:
        return 1

    return count(n-1) + count(n-4)

print count(N)
