'''
    Given list of patterns with wild carts (*),
    you need to determine which one of these pattern matches
    the given path.
    Wildcard can be replaced by any word/char

    In case of tie: prefer the pattern whose leftmost wildcard
    appears in a field further to the right

    Patterns are ',' separated and paths are '/' separated.

    E.g. :
    Patterns = ['*,b,* ', 'a,*,*', 'w,x,*,*']
    Path = '/a/b/c/'
    Output: 'a,*,*'

    Explaination: Both '*,b,* ', 'a,*,*' could be solution
    but 'a,*,*' has farthest '*'
'''

'''
    Solution:
    A possible brute force solution could be to match
    each path with all the patterns,
    Get all the possible solutions and then apply tie resolver.

    This is standard O(n^2) solution.

    A better solution could be to pre-process all the patterns
    and break them by level.
    E.g.: for ['*,b,* ', 'a,*,*', 'w,x,*,*']
    Level 0: has keys ['*', 'a', 'w']
    Level 1: has keys ['b', '*', 'x']
    Level 2: has keys ['*', '*', '*']
    Level 3: has keys ['*']

    And then match path by each level.
    for Path: ['a', 'b', 'c']
    we will check at level 0 which pattens has 'a' or '*'
    then we will check at level 1 which pattens has 'b' or '*'
    then we will check at level 2 which pattens has 'c' or '*'
    and keep on taking intersecion at each level.

'''

'''
    List of patterns are given, a pattern like
    [['*', 'b', '*'], ['a','*', '*']]
    spliting string by ','.

    This method will create a dict by parsing these patterns
    into levels and all the keys presents at that level
'''


def create_input_dict(patterns):
    input_dict = {}
    i = 0
    for pattern in patterns:
        level = 0
        for ele in pattern:
            ele = ele.strip()
            if level not in input_dict:
                input_dict[level] = {}
            if ele in input_dict[level]:
                input_dict[level][ele] += [i]
            else:
                input_dict[level][ele] = [i]
            level += 1

        i += 1
    return input_dict


'''
    This method determine all the possible solutions
    for given path by matching all levels of path
    with input_dict
'''


def get_possible_solutions(input_dict, path):
    level = 0
    possible_soln = set(range(M))

    for ele in path:
        ele = ele.strip()
        level_dict = input_dict.get(level)
        if not level_dict:
            level_soln = set()
        elif not (level_dict.get(ele) or
                  level_dict.get('*')):
            level_soln = set()
        else:
            level_soln = set(level_dict.get(ele, []) + level_dict.get('*', []))

        possible_soln = possible_soln.intersection(level_soln)

        level += 1

    return list(possible_soln)


'''
    This is a tie breaker method,
    which determines which pattern has farthest wildcard
'''


def find_farthest(patterns):
    max_wild_index = 0
    max_wild_index_pattern = 0

    for pattern in patterns:
        if '*' not in pattern:
            return pattern

        wild_index = pattern.index('*')

        if wild_index > max_wild_index:
            max_wild_index = wild_index
            max_wild_index_pattern = pattern

    return max_wild_index_pattern


if __name__ == "__main__":

    M = int(raw_input())
    patterns = []
    for i in range(M):
        pattern = raw_input().split(',')
        patterns.append(pattern)

    input_dict = create_input_dict(patterns)

    N = int(raw_input())

    for i in range(N):
        path = raw_input().strip('/').split('/')
        possible_soln = get_possible_solutions(input_dict, path)

        actual_soln = []
        for soln in possible_soln:
            if len(patterns[soln]) == len(path):
                actual_soln.append(patterns[soln])

        total_solns = len(actual_soln)

        if total_solns == 0:
            print 'NO MATCH'
        elif total_solns == 1:
            print ','.join(actual_soln[0])
        else:
            print ','.join(find_farthest(actual_soln))
