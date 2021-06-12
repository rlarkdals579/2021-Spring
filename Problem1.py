# Name : Kangmin Kim
# NetID KangKim
# SBUID : 111329652

from collections import Counter

print('type your string : ')

def is_nice(s):
    if s.isalpha():
        d = Counter(Counter(s).values())
        if len(d) == 1:
            return 'HARD YES'
        else:
            return 'HARD NO'
    else:
        return 'Please type strings with alphabets only'

print(is_nice(input()))