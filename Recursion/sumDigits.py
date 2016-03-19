#encoding=utf8

'''

Given a non-negative int n, return the sum of its digits recursively (no loops).
Note that mod (%) by 10 yields the rightmost digit (126 % 10 is 6), while divide (/) by 10 removes the rightmost digit (126 / 10 is 12).

sumDigits(126) → 9
sumDigits(49) → 13
sumDigits(12) → 3

http://codingbat.com/prob/p163932
'''

def sumDigits(n):
    if n <= 9:
        return n  #base-case, implies we have reached the first digit, starting backwards from the units place
    else:
        return n % 10 + sumDigits(n / 10)  # add the last digit recursively

print "sumDigits(%d) -> %d" %(126, sumDigits(126))
print "sumDigits(%d) -> %d" %(49, sumDigits(49))
print "sumDigits(%d) -> %d" %(12, sumDigits(12))
print "sumDigits(%d) -> %d" %(126982734, sumDigits(126982734))

