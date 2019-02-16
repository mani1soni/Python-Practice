#!/usr/bin/python3
'''
john works at  clothing store. He has a large pile of socks that he must pair by color for sale. Given an array of integers representing the color of each soc, determine how many pairs of socks with matching colors there are.
For Example, there are n = 7 socks with colors ar = [1,2,1,2,1,3,2]. There is one pair of color 1 and one of color 2.
and there are three odd socks left, one of each color. The number of pairs is 2.

Example: - Sample Input = 9
                          10 20 20 10 10 10 30 50 10 20
           Sample Output = 3
'''
from collections import Counter as count
n = int(input())
socks = count(input().split())
print(sum(map(lambda x: x//2, socks.values())))


