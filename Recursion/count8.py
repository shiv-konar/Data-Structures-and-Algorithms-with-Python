#encoding=utf8
'''

Given a non-negative int n, compute recursively (no loops) the count of the occurrences of 8 as a digit,
except that an 8 with another 8 immediately to its left counts double, so 8818 yields 4.
Note that mod (%) by 10 yields the rightmost digit (126 % 10 is 6),
while divide (/) by 10 removes the rightmost digit (126 / 10 is 12).

count8(8) → 1
count8(818) → 2
count8(8818) → 4

http://codingbat.com/prob/p192383
'''
def count8(n):
    if n <= 9 and n % 8 == 0:  #check if we have reached the first digit starting from the units place and if the first digit is 7
        return 1
    elif n <=9 and n % 8 != 0:  #check if we have reached the first digit starting from the units place and if the first digit is not 7
        return 0
    else:  #check if the units place digit is a 7 or not
        if (n % 10) % 8 == 0 and (n % 100) % 8 == 0:
            return 2 + count8(n / 10)
        elif (n % 10) % 8 == 0:
            return 1 + count8(n / 10)
        else:
            return 0 + count8(n / 10)

print count8(8)
print count8(818)
print count8(8818)
print count8(8888)