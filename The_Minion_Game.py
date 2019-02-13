#!/usr/bin/python3

#Game_Rules
'''
There are two players kevin and stuart
1. Both players are given the same string, S.
2. Both players have to make substrings using the letters of the string S.
3. Stuart has to make words starting with consonants.
4. kevin has to make words starting with vowels.
5. The game ends when both players have made all possible substrings.

Scoring:--> A player gets +1 point for each occurance of the substring in the string S.
For example: string S = BANANA
kevin's vowel beginning word = ANA
Here, ANA occurs twice in BANANA Hence, kevin will get 2 points.
'''
def minion_game(s):
    vowels = 'AEIOU'
    kevsc = 0
    stusc = 0
    for i in range (len(s)):
        if s[i] in vowels:
            kevsc += (len(s) - i)
        else:
            stusc += (len(s)-i)
    if kevsc > stusc:
        print("Kevin", kevsc)
    elif kevsc < stusc:
        print("Stuart", stusc)
    else:
        print("Draw")
if __name__ == '__main__':
    s = input()
    minion_game(s)

