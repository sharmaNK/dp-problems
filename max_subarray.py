'''
    Find max sum of continous subarray for given array.

    Input: 2,-1,2,3,4,-5
    Output: 10
'''
import sys

a = sys.argv[1].split(',')

cnt = 0
input_array = [int(i) for i in a]

local_max, final_max = 0, 0

for j in input_array:
    local_max += j
    final_max = max(final_max, local_max)

    if local_max <= 0:
        local_max = 0
        continue

print final_max
