#!/usr/bin/python3
'''
Example:- Give input like = 5 7 
            then it prints a pattern of 5*7 size
'''
n,m = map(int, input().split())
pattern = [('.|.'*(2*i + 1)).center(m, '-') for i in range(n//2)]
print('\n'.join(pattern + ['WELCOME'.center(m, '-')] + pattern[::-1]))
