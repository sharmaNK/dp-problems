memoization = {}
def longestPalindrome(n, s):
    if n<=1:
        return n

    if s in memoization:
        return memoization[s]

    if s[0] == s[n-1]:
        memoization[s] = max(longestPalindrome(n-2, s[1:n])+2, longestPalindrome(n-1, s[0:n-1]),
                             longestPalindrome(n-1, s[1: n]))
        return memoization[s]
    else:
        memoization[s] = max(longestPalindrome(n-1, s[0:n-1]), longestPalindrome(n-1, s[1: n]))
        return memoization[s]

print longestPalindrome(3, 'aaa')
