'''
	This is a hacker rank dp problem. Here is the link:
	https://www.hackerrank.com/challenges/candies
	Problems goes like:

	Alice is a kindergarden teacher. She wants to give some candies to the children in her class. 
	All the children sit in a line ( their positions are fixed), and each  of them has a rating
	score according to his or her performance in the class.
	Alice wants to give at least 1 candy to each child.
	If two children sit next to each other, then the one with the higher rating must get more candies.
	Alice wants to save money, so she needs to minimize the total number of candies given to the children.
'''


'''
	To run: python candies.py 
'''
import sys                                                                                                                 
 
a = sys.argv[1].split(',')

def candy(i):
    if i == len(a) - 1 or i == 0:
        return 1
    if a[i] < a[i-1]:
        return candy(i-1) + 2

    if a[i]

